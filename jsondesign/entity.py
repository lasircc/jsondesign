"""
TODO: description

"""

import json
import utils

SCHEMA_VERSION = 'http://json-schema.org/draft-07/schema#'
BASE_URI = 'http://las.ircc.it/schemas/'



class Entity(object):

    def __init__(self):
        pass

    def reprJSON(self):
        return vars(self)

    def printJSON(self):
        print(json.dumps(self, cls=utils.ComplexEncoder, sort_keys=True, indent=4))

    def __repr__(self):
        return vars(self)



class Object(Entity):
    """
    Pythonic representation of a data entity
    """

    def __init__(self, title):
        self.type = "object"
        self.schema = SCHEMA_VERSION
        self.id = BASE_URI + title
        self.title = title
        self.properties = {'features': dict()}



    # def __repr__(self):
    #     return f"<Pythonic Object representation of a {self.id})>"


    def setFeature(self, features):
            for key, value in features.items():
                self.properties['features'][key] = value
    



class SimpleDataType(Entity):
    """
    Built-in feature class
    """

    def __init__(self, type):
        self.type = type

    def enum(self):
        pass

    


class String(SimpleDataType):

    def __init__(self):
        super().__init__("string")

    def setMinLength(self, minLength):
        self.minLength = minLength

    def setMaxLength(self, maxLength):
        self.maxLength = maxLength

    def setRegex(self, pattern):
        self.pattern = pattern

    def setFormat(self):
        pass


class Numeric(SimpleDataType):

    def __init__(self, numeric_type):
        if numeric_type in ['integer', 'number']:
            super().__init__(numeric_type)
        else:
            raise Exception('Numeric type must be integer or number')

    def setMultipleOf(self, multipleOf):
        self.multipleOf = multipleOf

    def setMinimum(self, minimum, exclusive = False):
        if exclusive: # X > k
            self.exclusiveMinimum = minimum
        else: # X >= k
            self.minimum = minimum
    
    def setMaximum(self, maximum, exclusive = False):
        if exclusive: # X > k
            self.exclusiveMaximum = maximum
        else: # X >= k
            self.maximum = maximum


class Array(SimpleDataType):

    def __init__(self):
        super().__init__("array")

    def setItemsConstraint(self, constraint):
        pass

    def setMinItems(self, minItems):
        self.minItems = minItems

    def setMaxItems(self, maxItems):
        self.maxItems = maxItems


class Boolean(SimpleDataType):

    def __init__(self):
        super().__init__("boolean")


class Null(SimpleDataType):
    
    def __init__(self):
        super().__init__("null")

