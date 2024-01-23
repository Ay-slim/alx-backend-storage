#!/usr/bin/env python3
"""Top students"""


def top_students(mongo_collection):
    """
    top_students - Function to return top students
    @mongo_collection: Mongo collection object
    Return: Empty list or list of documents
    """
    if mongo_collection.count_documents({}) == 0:
        return []

    return mongo_collection.aggregate([
            {
                '$project': {
                    'name': '$name',
                    'averageScore': {'$avg': '$topics.score'} 
                }
            },
            {'$sort': {'averageScore': -1}}
        ])
