from jsonschema import Draft7Validator
from jsondesign.schema_store import Schema_Store
from jsondesign.entity import *
from sample_store import SCHEMA
import jsonref


def custom_get_function(uri, resolve=False):
    if resolve == False:
        return SCHEMA[uri]
    else:
        pass


# create a schema store
st = Schema_Store(getter=custom_get_function)

# Create an Aliquot
e = Object(uri='las://schema/Aliquot')
weight = Numeric('integer')
barcode = String()
features = {'weight': weight, 'barcode': barcode}
e.setFeature(features)
print(e.schema)

# # Define a reference to an Aliquot
# features = {'foo': {'$ref': 'las://recording.json'} }
# e.setFeature(features)

# # print the json representation of an Aliquot
# e.json()

# # resolve reference against the current schema store
# e.dereference(st)

# # the dereferenced object
# e.json()


schema = {
  "_id": "http://example.com/schema/employee",
  "_schema": "http://json-schema.org/draft-07/schema#",
  "properties": {
    "features": {
      "type": "object",
        
      "allOf": [
        
        {
          "_id": "http://example.com/schemas/person",
          "type": "object",
          "properties": {
            "firstName": {
              "type": "string"
            },
            "lastName": {
              "type": "string"
            }
          },
          "required": [
            "firstName",
            "lastName"
          ]
        },
        
        {
          "$id": "http://example.com/schemas/person2",
          "type": "object",
          "properties": {
            "firstName": {
              "type": "string"
            },
            "lastName": {
              "type": "string"
            },
            "blueName": {
              "type": "string"
            }
          },
          "required": [
            "firstName",
            "lastName"
          ]
        },
        
        {
          "properties": {
            "foo": {
              "type": "string"
            },
            "bar": {
              "type":"string"
            },
          },
          "required" : ["foo"]
            
        }
      ]
    }
  },
  "required": [
    "features"
  ]
}

doc ={
  "features": {
    "firstName": "ciao",
    "lastName": "ciao",
    "foo" : "ci"
  }
}

Draft7Validator(schema).validate(doc)
print('Is valid')