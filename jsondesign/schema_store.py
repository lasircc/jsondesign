"""
An interface with a schema repository
"""

import jsonref

class Schema_Store(object):

    def __init__(self, getter):
        self.getter = getter

    def get_object(self, uri, **kwargs):
        return self.getter(uri, **kwargs)

    def resolve(self, schema, **kwargs):
        result = jsonref.JsonRef.replace_refs(schema, loader=self.get_object)
        return result


