import jsondesign.schema_store
import pytest
from sample_store import SCHEMA


@pytest.fixture(scope='session')  
def schema_store():
    # How to retrieve a doc. A custom way. Pass this function to jsondesign.Schema_Store
    def custom_retrieval_function(uri):   
            return SCHEMA[uri]

    # create a schema store
    schema_store = jsondesign.schema_store.Schema_Store(getter = custom_retrieval_function)
    return schema_store