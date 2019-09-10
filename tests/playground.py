from jsondesign.schema_store import Schema_Store
from jsondesign.entity import *
from sample_store import SCHEMA
import jsonref





def custom_get_function(uri, resolve = False):
    if resolve == False:
        return SCHEMA[uri]
    else:
        pass


# create a schema store
st = Schema_Store(getter = custom_get_function)

# Get a Document from the store
st.get_object('las://recording.json', resolve = False)

# Create an Aliquot
e = Object(title = 'Aliquot')
weight =  Numeric('integer')
barcode = String()
features = {'weight': weight,'barcode': barcode }
e.setFeature(features)
print (e.schema)

# Define a reference to an Aliquot
features = {'foo': {'$ref': 'las://recording.json'} }
e.setFeature(features)

# print the json representation of an Aliquot
e.json()

# resolve reference against the current schema store
e.dereference(st)

# the dereferenced object
e.json()



