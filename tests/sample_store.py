SCHEMA = [

    {
        "$id": "las://schema/car",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            'features': {
                "type": "object",
                "engine": {"$ref": "las://schema/engine"},
                "color": {"type": "string"},
                "manufacturer": {"$ref": "las://schema/manufacturer"}
            }

        }
    },

    {
        "$id": "las://schema/engine",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            'features': {
                "type": "object",
                "color": {"type": "string"},
                "manufacturer": {"$ref": "las://schema/manufacturer"},
            }
        }
    },
    {
        "$id": "las://schema/manufacturer",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            'features': {
                "type": "object",
                "name": {"type": "string"},
                "vat_number": {"type": "string"}
            }
        }
    },
    {
        "$id": "foo",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        'foo_bar': 5,
        'foo_baz': [1, 2, True]
    },
    {
        "$id": "bar",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        'bar_baz': 4
    }
]

