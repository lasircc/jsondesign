import entity
import schema_store
from sample import SCHEMA
import jsonref





def custom_get_function(uri, resolve = False):
    if resolve == False:
        return SCHEMA[uri]
    else:
        pass


# create a schema store
schema_store = schema_store.Schema_Store(getter = custom_get_function)

# Get a Document from the store
schema_store.get_object('las://recording.json', resolve = False)

# Create an Aliquot
e = entity.Object(title = 'Aliquot')
weight =  entity.Numeric('integer')
barcode = entity.String()
features = {'weight': weight,'barcode': barcode }
e.setFeature(features)

# Define a reference to an Aliquot
features = {'foo': {'$ref': 'las://recording.json'} }
e.setFeature(features)

# print the json representation of an Aliquot
e.json()

# resolve reference against the current schema store
e.dereference(schema_store)

# the dereferenced object
e.json()



