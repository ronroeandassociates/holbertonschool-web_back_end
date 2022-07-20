#!/usr/bin/env python3
# 11 Where can I learn Python?
# a Python function that returns the list of school having a specific topic:
'''
Prototype: def schools_by_topic(mongo_collection, topic):
mongo_collection will be the pymongo collection object
topic (string) will be topic searched
'''

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    '''returns the list of schools having a specific topic'''
    if mongo_collection is None:
        return []

    return mongo_collection.find({'topics': topic})
