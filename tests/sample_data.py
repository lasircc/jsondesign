SCHEMA = [

    {
        "$id": "las://schema/person",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "allOf": [
            {
                "properties": {
                    'features': {
                        "type": "object",
                        "allOf": [
                            {
                                "properties": {
                                    "firstName":    {"type": "string"},
                                    "lastName":     {"type": "string"},
                                    "address":      {"$ref": "las://schema/address"}
                                },
                                "required": ["firstName", "lastName"]
                            }
                        ]
                    }
                }
            }
        ]
    },
    {
        "$id": "las://schema/student",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "allOf": [
            {
                "properties": {
                    'features': {
                        "type": "object",
                        "allOf": [
                            {
                                "properties": {
                                    "student_id": {"type": "string"}
                                },
                                "required": ["student_id"]
                            }
                        ]
                    }
                }
            },
            {"$ref": "las://schema/person"}
        ]
    },
    {
        "$id": "las://schema/professor",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "allOf": [
            {
                "properties": {
                    'features': {
                        "type": "object",
                        "allOf": [
                            {
                                "properties": {
                                    "faculty": {"type": "string"}
                                },
                                "required": ["faculty"]
                            }
                        ]
                    }
                }
            },
            {"$ref": "las://schema/person"}
        ]
    },
    {
        "$id": "las://schema/address",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "allOf": [
            {
                "properties": {
                    'features': {
                        "type": "object",
                        "allOf": [
                            {
                                "properties": {
                                    "street_address": {"type": "string"},
                                    "city":           {"type": "string"},
                                    "state":          {"type": "string"}
                                },
                                "required": ["city", "state", "street_address"]
                            }
                        ]
                    }
                }
            }
        ]
    },


    # {
    #     "$id": "las://schema/address",
    #     "$schema": "http://json-schema.org/draft-07/schema#",
    #     "type": "object",
    #     "allOf": [
    #         {
    #             "properties": {
    #                 "street_address": {"type": "string"},
    #                 "city":           {"type": "string"},
    #                 "state":          {"type": "string"}
    #             },
    #         }
    #     ]
    # },


    # {
    #     "$id": "las://schema/car",
    #     "$schema": "http://json-schema.org/draft-07/schema#",
    #     "type": "object",
    #     "properties": {
    #         'features': {
    #             "type": "object",
    #             "engine": {"$ref": "las://schema/engine"},
    #             "color": {"type": "string"},
    #             "manufacturer": {"$ref": "las://schema/manufacturer"}
    #         }

    #     }
    # },

    # {
    #     "$id": "las://schema/engine",
    #     "$schema": "http://json-schema.org/draft-07/schema#",
    #     "type": "object",
    #     "properties": {
    #         'features': {
    #             "type": "object",
    #             "color": {"type": "string"},
    #             "manufacturer": {"$ref": "las://schema/manufacturer"},
    #         }
    #     }
    # },
    # {
    #     "$id": "las://schema/manufacturer",
    #     "$schema": "http://json-schema.org/draft-07/schema#",
    #     "type": "object",
    #     "properties": {
    #         'features': {
    #             "type": "object",
    #             "name": {"type": "string"},
    #             "vat_number": {"type": "string"}
    #         }
    #     }
    # },
    # {
    #     "$id": "foo",
    #     "$schema": "http://json-schema.org/draft-07/schema#",
    #     "type": "object",
    #     'foo_bar': 5,
    #     'foo_baz': [1, 2, True]
    # },
    # {
    #     "$id": "bar",
    #     "$schema": "http://json-schema.org/draft-07/schema#",
    #     "type": "object",
    #     'bar_baz': 4
    # }
]

DEREFERENCED_SCHEMA = [
    {
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
]

INSTANCES = {
    # A student
    "a_student": {
        "features": {
            "student_id": "foo",
            "firstName": "foo2",
            "lastName": "Bob",
            "address": {
                "features": {
                    "city": "foo",
                    "state": "foo",
                    "street_address": "ao"
                }
            }
        }
    }
}
