"""
TODO: The Entity library

"""

import json

SCHEMA_VERSION = 'http://json-schema.org/draft-07/schema#'
BASE_URI = 'http://las.ircc.it/schemas/'



class Entity(object):

    def __init__(self, schema = None, type = None):
        self.schema = schema or dict()
        self.set_type(type)

    def set_type(self, type):
        self.schema['type'] = type

    def json(self):
        """ Print a JSON representatoin of the Entity"""
        print(json.dumps(self.schema, sort_keys=True, indent=4))




class Object(Entity):
    """
    Pythonic representation of a Complex Object
    """

    def __init__(self, schema = None, title = None):
        if schema:
            super().__init__(schema = schema)
        else:
            super().__init__(type = 'object')
            s = self.schema
            s['$schema'] = SCHEMA_VERSION
            s['$id'] = BASE_URI + title
            s['title'] = title
            s['properties'] = {'features': dict()}       



    def __repr__(self):
         return f"<Pythonic Object representation of a {self.schema['title']})>"


    def setFeature(self, features):
            for key, value in features.items():
                if type(value) == dict:
                    self.schema['properties']['features'][key] = value
                else:
                    self.schema['properties']['features'][key] = value.schema

    def dereference(self, schema_store):
        """
        dereference the object against a schema_store and update its schema representation
        """
        self.schema = schema_store.resolve(self.schema)
    

 


class String(Entity):

    def __init__(self):
        super().__init__(type = "string")

    def setMinLength(self, minLength):
        self.schema['minLength'] = minLength

    def setMaxLength(self, maxLength):
        self.schema['maxLength'] = maxLength

    def setRegex(self, pattern):
        self.schema['pattern'] = pattern

    def setFormat(self):
        pass


class Numeric(Entity):

    def __init__(self, numeric_type):
        if numeric_type in ['integer', 'number']:
            super().__init__(type = numeric_type)
        else:
            raise Exception('Numeric type must be integer or number')

    def setMultipleOf(self, multipleOf):
        self.schema['multipleOf'] = multipleOf

    def setMinimum(self, minimum, exclusive = False):
        if exclusive: # X > k
            self.schema['exclusiveMinimum'] = minimum
        else: # X >= k
            self.schema['minimum'] = minimum
    
    def setMaximum(self, maximum, exclusive = False):
        if exclusive: # X > k
            self.schema['exclusiveMaximum'] = maximum
        else: # X >= k
            self.schema['maximum'] = maximum


class Array(Entity):

    def __init__(self):
        super().__init__(type = "array")

    def setItemsConstraint(self, constraint):
        pass

    def setMinItems(self, minItems):
        self.schema['minItems'] = minItems

    def setMaxItems(self, maxItems):
        self.schema['maxItems'] = maxItems


class Boolean(Entity):

    def __init__(self):
        super().__init__(type = "boolean")


class Null(Entity):
    
    def __init__(self):
        super().__init__(type = "null")

