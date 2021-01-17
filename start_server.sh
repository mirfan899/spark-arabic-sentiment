#!/bin/bash
spark-submit --master local --total-executor-cores 2 --executor-memory 4g server.py
