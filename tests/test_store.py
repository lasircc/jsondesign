


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
    