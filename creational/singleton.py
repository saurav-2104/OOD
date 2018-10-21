"""
 Provide one and only one object of a particular type.
"""

"""
Use case:
Implement a CacheClient which provides an interface to fetch cached data.
"""


class Cache:
    __instance = None

    @staticmethod
    def get_instance():
        if Cache.__instance is None:
            Cache()
        return Cache.__instance

    def __init__(self):
        if Cache.__instance is not None:
            raise ReferenceError('Cannot instantiate a singleton class.')
        else:
            Cache.__instance = self


if __name__ == '__main__':
    print(Cache.get_instance())
    print(Cache.get_instance())
    print(Cache())
