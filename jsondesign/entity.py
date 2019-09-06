"""
TODO: description

"""


class Entity(object):
    """
    Pythonic representation of a data entity
    """

    def __init__(self, title, types):
        self.title = title
        self.types = list()
        self.features = list()
        self.setTypes(types)


    def __repr__(self):
        return f"<Pythonic Entity representation of a {self.title})>"


    def setTypes(self, types):
        if type(types) != list:
            raise Exception('Types must be a list')
        for t in types:
            self.types.append(t)


    def setFeature(self, feature):
        self.features.append(feature)


    def getFeature(self):
        """
        Retrieve all the features (inherited too)
        """
        
        for f in self.features:
            print (f)

        for t in self.types:
            print(f'inherited from {t.title}')
            t.getFeature()
