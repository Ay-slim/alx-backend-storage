#!/usr/bin/env python3
"""Write string to Redis"""


from typing import Union
import redis
import uuid


class Cache:
    """Cache class to store data with Redis"""

    def __init__(self) -> None:
        """
        Initializes an instance of the Cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store - Method to store data and return key
        @data: Arg of type str, bytes, int, or float
        Returns: String (key)
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
