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