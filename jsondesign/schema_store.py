"""
An interface with a schema repository
"""

class Schema_Store(object):

    def __init__(self, get):
        self.get = get

    def get_object(self):
        self.get()

