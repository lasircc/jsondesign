


def test_get_object(schema_store):
    print ('>>>>> testing object retrieval')
    foo = schema_store.get_object('foo')
    bar = schema_store.get_object('bar')
    
    #  get_object() returns an entity.Object
    assert foo.schema == {
        "$id": "foo",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        'foo_bar': 5,
        'foo_baz': [1, 2, True]
    }
    assert bar.schema == {
        "$id": "bar",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        'bar_baz': 4
    }
    print ('>>>>> ok')
