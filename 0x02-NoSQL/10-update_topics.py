#!/usr/bin/env python3
# 10 Change school topics
# a Python function that changes all topics of a school
# document based on the name:
'''
Prototype: def update_topics(mongo_collection, name, topics):
mongo_collection will be the pymongo collection object
name (string) will be the school name to update
topics (list of strings) will be the list of topics approached in the school
'''

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    '''changes all topics in the school document'''
    if mongo_collection is None:
        return []

    return mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
