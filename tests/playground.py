from jsonschema import Draft7Validator
from jsondesign.schema_store import Schema_Store
from jsondesign.entity import Object, String
from sample_data import SCHEMA

import copy



# create a schema store
def custom_retrieval_function(uri):
        return copy.deepcopy(next(item for item in SCHEMA if item["$id"] == uri))

schema_store = Schema_Store(getter = custom_retrieval_function)





# Create an object
o = Object(uri='las://schema/address')
simple_string =String()
features = {'street_address': simple_string, 'city': simple_string, 'state': simple_string}
o.set_feature(**features)

o.add_required_features('street_address')
# entity.add_required_features prevents duplicates
o.add_required_features('street_address', 'city', 'state')





# load from store
address = schema_store.get_object('las://schema/address')

address2 = schema_store.get_object('las://schema/address')