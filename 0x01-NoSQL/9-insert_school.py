#!/usr/bin/env python3
"""Create a document via python"""


def insert_school(mongo_collection, **kwargs):
    """
    insert_school - Function to insert documents
    @mongo_collection: Mongo collection object
    Return: _id of new documents
    """
    mongo_creation = mongo_collection.insert_one(kwargs)
    return mongo_creation.inserted_id
