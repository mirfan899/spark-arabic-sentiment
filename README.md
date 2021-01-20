## Installation Process
Spark is Java based, You need to install java on your system to run the spark.

Download apache spark and place it some directory you want to place it. Uncompress it and save it as `spark` directory.

Add Environment variables for spark in `.bashrc` if you are using linux or Unix based OS. For example I have downloaded the spark
in irfan directory. Now add these lines to `.bashrc` file. 
```textmate
export SPARK_HOME=/home/irfan/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
export PYSPARK_PYTHON=python3
```

Test your installation of spark by running the command in terminal
```shell script
pyspark
```
It will start the python shell in spark.


## Install requirements.
you need to install Python packages to run the training.

```shell script
pip3 install -r requirements.txt
```

Now you are good to go.

## Start spark server
Run the `start_server.sh` to start the spark. It will automatically train the model on startup and provide you with api access to
find the sentiment of given tweet using API.

## Test server
```shell script
# json request
curl -X POST -d '{"sentence":"التعلم الرقمي من خلال التسجيل الرقمي افتتاح الموقع قري"}' -H "Content-Type: application/json" http://0.0.0.0:5432/analyse
```

If you want to test it with Pycharm you can run the `api_test.http` file

## Note
POSTMAN has encoding issues with arabic type language such as Urdu etc so you have to use the curl or Pycharm to test it. Or
You can integrate it with your app or website.


## Create database to store user tweets
```python
import findspark
findspark.init("/home/irfan/spark")
import pyspark as ps
from pyspark.sql import SQLContext
sc = ps.SparkContext('local[2]')
sqlContext = SQLContext(sc)
csv_file = "./user_tweets.csv"
sqlContext.sql("CREATE DATABASE IF NOT EXISTS Sentiment;")
sqlContext.sql("use sentiment")
df = (sqlContext.read.format("csv")
  .option("inferSchema", "true")
  .option("header", "true")
  .load(csv_file))

schema="tweet varchar(512)"

sqlContext.sql("use sentiment;")
df.write.saveAsTable("user_tweets", schema=schema)
# df.write.format("csv").saveAsTable("user_tweets", schema=schema)
df = sqlContext.read.load("spark-warehouse/sentiment.db/user_tweets")
df_sfo = sqlContext.sql("SELECT * FROM user_tweets")
tbl = sqlContext.read.format("parquet").load("spark-warehouse/sentiment.db/user_tweets")
tbl.sql_ctx.sql("INSERT INTO user_tweets  VALUES ('{}')".format('قراءة المزيد')).show()
```
