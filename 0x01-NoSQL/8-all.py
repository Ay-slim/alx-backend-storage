#!/usr/bin/env python3
"""All documents lists module"""


def list_all(mongo_collection):
    """
    list_all - Function to return mongo documents
    @mongo_collection: Mongo collection object
    Return: Empty list or list of documents
    """
    if mongo_collection.count_documents({}) == 0:
        return []
    return mongo_collection.find()
