#!/usr/bin/env python3
"""Write string to Redis"""


from typing import Union, Callable, Any
from functools import wraps
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """
    count_calls - Decorator to count calls
    @method: Callable method
    Returns: A callable
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    call_history - Decorator to store function i/o
    @method: Callable method
    Returns: A callable
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        if isinstance(self._redis, redis.Redis):
            i_key = method.__qualname__ + ":inputs"
            o_key = method.__qualname__ + ":outputs"
            self._redis.incr(method.__qualname__)
            o_val = method(self, *args, **kwargs)
            self._redis.rpush(i_key, str(args))
            self._redis.rpush(o_key, o_val)
        return o_val
    return wrapper


class Cache:
    """Cache class to store data with Redis"""

    def __init__(self) -> None:
        """
        Initializes an instance of the Cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store - Method to store data and return key
        @data: Arg of type str, bytes, int, or float
        Returns: String (key)
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get_str(self, val: bytes) -> str:
        """
        get_str - Function to parametize redis return byte
        @val: Bytes value to parametize
        Returns: String
        """
        return str(val)

    def get_int(self, val: bytes) -> int:
        """
        get_int - Function to parametize redis return byte
        @val: Bytes value to parametize
        Returns: Integer
        """
        return int(val)

    def get(self, key: str, fn: Callable = None) -> Union[
            str, bytes, int, float, None]:
        """
        get - Fetch stored value with the appropriate type
        @key: Key to fetch with
        @fn: Appropriate calling function
        """
        raw_bytes = self._redis.get(key)

        if fn is None or raw_bytes is None:
            return raw_bytes
        return fn(raw_bytes)

# cache = Cache()

# TEST_CASES = {
#     b"foo": None,
#     123: int,
#     "bar": lambda d: d.decode("utf-8")
# }

# for value, fn in TEST_CASES.items():
#     key = cache.store(value)
#     assert cache.get(key, fn=fn) == value
