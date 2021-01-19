import json
import logging
from flask import Blueprint
from analyser import SentimentAnalyser

main = Blueprint('main', __name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from flask import Flask, request, jsonify


@main.route("/analyse", methods=["POST"])
def analyse():
    print(request.data)
    data = json.loads(request.data.decode("utf8"))
    print(data)
    if data:
        logger.debug("Analysing sentiment %s", data)
        sentiment = sentiment_analyser.get_sentiment(data["sentence"])
        return jsonify(sentiment)
        # return json.dumps(data, ensure_ascii=False)
    return jsonify({"Status": 404, "Message": "Please provide the sentence you want to analyse for sentiment."})


@main.route("/status", methods=["POST", "GET"])
def status():
    # get the ratings from the Flask POST request object
    sentence = request.data
    print(sentence)

    return json.dumps({"status": 200})


def create_app(spark_context, sql_context, dataset_path):
    global sentiment_analyser

    sentiment_analyser = SentimentAnalyser(spark_context, sql_context, dataset_path)

    app = Flask(__name__)
    app.register_blueprint(main)
    return app
