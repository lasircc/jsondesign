"""
Library utils
"""


def explore_paths(schema):
    """
    Explore a schema and extract its features path recursively
    """
    print('\n\n_______Foo_______\n')

    # Get current schema
    #print(schema)

    properties = schema['allOf'][0]['properties']

    for k in properties:
        print(k)
        print (properties[k])
 
        if type(properties[k]) == dict: # do not explore list of required properties
     
            a = {k: properties[k]['type'] }
            print(a)
            if properties[k]['type'] == 'object':
                return explore_paths(properties[k])

            




foo = {
    "$id": "las://schema/student",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "allOf": [
        {
            "properties": {
                "features": {
                    "type": "object",
                    "allOf": [
                        {
                            "properties": {
                                "student_id": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "student_id"
                            ]
                        }
                    ]
                }
            }
        },
        {
            "$id": "las://schema/person",
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "allOf": [
                    {
                        "properties": {
                            "features": {
                                "type": "object",
                                "allOf": [
                                    {
                                        "properties": {
                                            "firstName": {
                                                "type": "string"
                                            },
                                            "lastName": {
                                                "type": "string"
                                            },
                                            "address": {
                                                "$id": "las://schema/address",
                                                "$schema": "http://json-schema.org/draft-07/schema#",
                                                "type": "object",
                                                "allOf": [
                                                    {
                                                        "properties": {
                                                            "features": {
                                                                "type": "object",
                                                                "allOf": [
                                                                    {
                                                                        "properties": {
                                                                            "street_address": {
                                                                                "type": "string"
                                                                            },
                                                                            "city": {
                                                                                "type": "string"
                                                                            },
                                                                            "state": {
                                                                                "type": "string"
                                                                            }
                                                                        },
                                                                        "required": [
                                                                            "city",
                                                                            "state",
                                                                            "street_address"
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        }
                                                    }
                                                ]
                                            }
                                        },
                                        "required": [
                                            "firstName",
                                            "lastName"
                                        ]
                                    }
                                ]
                            }
                        }
                    }
            ]
        }
    ]
}


explore_paths(foo)
