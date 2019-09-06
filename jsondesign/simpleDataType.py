


class SimpleDataType(object):
    """
    Built-in feature class
    """
    pass


class String(SimpleDataType):

    def __init__(self, name):
        self.name = name
        self.length = None
        self.format = None
        self.regex = None

    def setLength(self):
        pass

    def setFormat(self):
        pass

    def setRegex(self):
        pass