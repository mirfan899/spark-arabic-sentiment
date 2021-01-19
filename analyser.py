import os
from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.ml.feature import IndexToString, StringIndexer
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.sql import Row
import logging
from preprocess import clean_tweet_ar


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SentimentAnalyser:
    """An Arabic Sentiment Analyser
    """
    def get_sentiment(self, tweet):

        rdd = self.sc.parallelize(clean_tweet_ar(tweet))
        tweet_rdd = rdd.map(lambda x: Row(tweet=x[0], target=x[1]))
        schema = self.sql_context.createDataFrame(tweet_rdd)
        return self.__predict_sentiment(schema)

    def __train_model(self):
        """Train the ALS model with the current dataset
        """
        logger.info("Training the ALS model...")
        lr = LogisticRegression(maxIter=100)
        self.model = lr.fit(self.train_set)
        logger.info("Sentiment Model built!")

    def __predict_sentiment(self, schema):
        """Gets predictions for a given (userID, movieID) formatted RDD
        Returns: an RDD with format (movieTitle, movieRating, numRatings)
        """
        test = self.pipelineFit.transform(schema)
        predict = self.model.transform(test)
        converter = IndexToString(inputCol="prediction", outputCol="predicted_label", labels=self.pipelineFit.stages[3].labels)
        converted = converter.transform(predict)
        return converted.select("predicted_label").collect()[0].asDict()

    def __init__(self, sc, sql_context, dataset_path):
        """Init the recommendation engine given a Spark context and a dataset path
        """

        logger.info("Starting up the Sentiment Analyser Engine:")

        self.sc = sc
        self.sql_context = sql_context
        # Load sentiment data for later use
        # logger.info("Loading Sentiment data...")
        # sentiment_file_path = os.path.join(dataset_path, 'arabic_tweets_labeled.csv')
        # sentiment_RDD = self.sql_context.read.format('com.databricks.spark.csv').options(header=True, inferSchema='true').load(sentiment_file_path)
        # sentiment_RDD = sentiment_RDD.dropna()
        #
        # tokenizer = Tokenizer(inputCol="tweet", outputCol="words")
        # hashtf = HashingTF(numFeatures=2 ** 16, inputCol="words", outputCol='tf')
        # idf = IDF(inputCol='tf', outputCol="features", minDocFreq=5)  # minDocFreq: remove sparse terms
        # label_stringIdx = StringIndexer(inputCol="target", outputCol="label")
        # pipeline = Pipeline(stages=[tokenizer, hashtf, idf, label_stringIdx])
        # sentiment_RDD.show()
        # pipelineFit = pipeline.fit(sentiment_RDD)
        # data = pipelineFit.transform(sentiment_RDD)
        # self.pipelineFit = pipelineFit
        # self.data = data
        # (train_set, test_set) = data.randomSplit([0.8, 0.2], seed=2000)
        #
        # self.train_set = train_set
        # self.test_set = test_set
        #
        # # Train the model
        # self.seed = 1245
        # self.iterations = 100
        # self.__train_model()
