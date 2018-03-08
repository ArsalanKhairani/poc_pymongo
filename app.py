# coding=utf-8

from flask import Flask
app = Flask(__name__)

from pymongo import MongoClient

# IF I ENABLE THESE TWO LINES - ERROR: ServerSelectionTimeoutError
conn = MongoClient('127.0.0.1', 27017, username='admin', password='admin', serverSelectionTimeoutMS=1000)
print list(conn['poc_pymongo'].test_collection.find())

@app.route('/')
def hello_world():

    # THIS WORKS FINE.
    conn = MongoClient('127.0.0.1', 27020, username='admin', password='admin', serverSelectionTimeoutMS=1000)
    print list(conn['poc_pymongo'].test_collection.find())

    return 'Hello, World!'
