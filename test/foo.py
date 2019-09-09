
def qal_uri_handler(uri):
    print (uri)
    return {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "definitions": {
        "Resource": {
            "additionalProperties": True,
            "properties": {
                "base_path": {
                    "type": "string"
                },
                "caption": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                },
                "uuid": {
                    "pattern": "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$",
                    "type": "string"
                }
            },
            "type": "object"
        }
    },
    "description": "The JSON Schema for QAL resources",
    "namespace": "qal",
    "properties": {
        "resources": {
            "items": {
                "$ref": "#/definitions/Resource"
            },
            "type": "array"
        }
    },
    "required": [
        "resources"
    ],
    "title": "QAL Resources",
    "type": "object",
    "version": "0.5"
}



_test_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "resource":
            {
                "$ref": "qal://resources.json#/definitions/Resource",
            }
    },
    "required": ["resource"],
}
_test_data = {
    "resource": {
        "uuid": "d03b44af-2887-4038-93fd-fbba5cbf5362",
        "name": "test",
        "base_path":"",
        "caption": "",
        "type": "",
        "data": ""
    }

}
_resolver = RefResolver(base_uri="",
                        handlers={"qal":qal_uri_handler}, referrer=None, cache_remote=False)
jsonschema.validators.Draft4Validator(schema=_test_schema, resolver=_resolver).validate(_test_data) 



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        self.length = length
        self.width = length