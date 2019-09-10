import jsondesign.schema_store
from sample_store import SCHEMA
#import pytest


#@pytest.fixture(scope='session')  
def create_store():

    # How to retrieve a doc. A custom way. Pass this function to jsondesign.Schema_Store
    def custom_retrieval_function(uri):   
        SCHEMA = {'foo' : {'foo_bar': 5, 'foo_baz': [1, 2, True] }, 'bar' : {'bar_baz' : 4} }
        return SCHEMA[uri]

    # create a schema store
    schema_store = jd.schema_store.Schema_Store(getter = custom_retrieval_function)
    return schema_store


def get_object(schema_store):

    foo = schema_store.get_object('foo')
    bar = schema_store.get_object('bar')
    assert foo == {'foo_bar': 5, 'foo_baz': [1, 2, True] }
    assert bar == {'bar_baz' : 4}



