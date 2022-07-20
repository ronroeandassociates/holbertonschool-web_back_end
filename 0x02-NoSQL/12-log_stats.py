#!/usr/bin/env python3
# 12 Log stats
# a Python script that provides some stats about Nginx logs stored in MongoDB:

from pymongo import MongoClient


def stats():
    # first line: x logs where x is the number of documents in this collection
    # connect to MongoDB
    client = MongoClient()
    # get the database
    db = client.logs
    # get Nginx collection from the database
    collection = db.nginx

    # Print number of total documents in the collection
    print(f"{collection.count_documents({})} logs")

    '''
    second line: Methods:
    5 lines with the number of documents with the method =
    ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
    (see example below - warning: it`s a tabulation before each line)
    one line with the number of documents with:
    method=GET
    path=/status
    '''

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    # Print Number of each method
    for method in methods:
        print(f"{collection.count_documents({'method': method})} {method}")
# TODO: FIX THIS format should be tab method  Method: xxx
    # Print number of documents with  method=GET and path=/status
    print(f"\t method {method}:" +
          f"{collection.count_documents({'method': 'GET', 'path': '/status'})}\
          GET /status")


if __name__ == "__main__":
    stats()
