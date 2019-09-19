import jsondesign.entity as ey


def test_get_object(schema_store):
    """
    testing object retrieval
    """ 

    #  get_object() returns an entity.Object
    address = schema_store.get_object('las://schema/address')
   
    assert address.schema == {
        "$id": "las://schema/address",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "allOf": [
            {
                "properties": {
                    'features': {
                        "type": "object",
                        "properties": {
                            "street_address": {"type": "string"},
                            "city":           {"type": "string"},
                            "state":          {"type": "string"}
                        },
                        "required": ["city", "state", "street_address"]
                    }
                }
            }
        ]
    }
    


def test_save_object(schema_store):

    e = ey.Object(uri='las://schema/address_foo')
    simple_string = ey.String()
    features = {'street_address': simple_string,
                'city': simple_string, 'state': simple_string}
    e.set_feature(**features)

    e.add_required_features('street_address')
    # entity.add_required_features prevents duplicates
    e.add_required_features('street_address', 'city', 'state')

    schema_store.save(e)

    # get the saved object from the store
    address_foo = schema_store.get_object('las://schema/address_foo')

    # compare with the one in memory
    assert address_foo.schema == e.schema