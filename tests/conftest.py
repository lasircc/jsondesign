import jsondesign.schema_store
import pytest
from sample_data import SCHEMA
import copy


@pytest.fixture(scope='session')  
def schema_store():
    # How to retrieve a doc. A custom way. Pass this function to jsondesign.schema_store.Schema_Store
    def custom_retrieval_function(uri):
        return copy.deepcopy(next(item for item in SCHEMA if item["$id"] == uri))

    def custom_save_function(schema):
        SCHEMA.append(schema)

    # create a schema store
    schema_store = jsondesign.schema_store.Schema_Store(getter = custom_retrieval_function, saver = custom_save_function)
    return schema_store