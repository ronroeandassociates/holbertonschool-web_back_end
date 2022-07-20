#!/usr/bin/env python3

# 9 Insert a document in Python
# a Python function that inserts a new document
# in a collection based on kwargs:
'''
Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
Returns the new _id
'''

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    '''
    Insert a new document in a collection
    '''
    if mongo_collection is None:
        return None
    return mongo_collection.insert_one(kwargs).inserted_id
