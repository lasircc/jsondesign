import jsondesign.entity as ey
from sample_data import SCHEMA, DEREFERENCED_SCHEMA


def test_create_object():
    """
    Create an object representation of an Address
    """
    e = ey.Object(uri='las://schema/address')
    simple_string = ey.String()
    features = {'street_address': simple_string,
                'city': simple_string, 'state': simple_string}
    e.set_feature(**features)

    e.add_required_features('street_address')
    # entity.add_required_features prevents duplicates
    e.add_required_features('street_address', 'city', 'state')

    # Match the creaded object against a target schema (i.e., las://schema/address)
    assert e.schema == next(
        item for item in SCHEMA if item["$id"] == 'las://schema/address')



def test_create_object_with_custom_features_field():
    """
    Create an object representation of an Address
    """
    e = ey.Object(uri='las://schema/foo', features_key='foobarbaz')
    simple_string = ey.String()
    custom_features = {'bar': simple_string}
    e.set_feature(**custom_features)

    assert e.schema == {
        "$id": "las://schema/foo",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "allOf": [
            {
                "properties": {
                    'foobarbaz': {
                        "type": "object",
                        "allOf": [
                            {
                                "properties": {
                                    "bar": {"type": "string"}
                                },
                                "required": []
                            }
                        ]
                    }
                }
            }
        ]
    }


def test_append_reference():
    """
    Create a reference and append it to an object
    """
    e = ey.Object(uri='las://schema/person')
    simple_string = ey.String()
    address = ey.ObjectReference('las://schema/address')

    features = {'firstName': simple_string,
                'lastName': simple_string, 'address': address}
    e.set_feature(**features)
    e.add_required_features('firstName', 'lastName')
    # Match the creaded object against a target schema (i.e., las://schema/address)
    assert e.schema == next(
        item for item in SCHEMA if item["$id"] == 'las://schema/person')


def test_extend_entity():
    """
    Create a Student schema extending person schema (i.e., inhertiance)
    """
    student = ey.Object(uri='las://schema/student')
    student_id = ey.String()
    student.set_feature(student_id=student_id)
    student.add_required_features('student_id')
    # Inheritance
    r = ey.ObjectReference('las://schema/person')
    student.extend(r)
    # Redundant inheritance. entity.extend() is protected against this kind of redundancy
    student.extend(r)
    assert student.schema == next(
        item for item in SCHEMA if item["$id"] == 'las://schema/student')


def test_dereference(schema_store):
    """
    Get an object from the store and resolve all references
    """

    student = schema_store.get_object('las://schema/student')
    dereferenced_schema = student.dereference(schema_store)
    # Match the creaded object against a dereferenced target schema (i.e., las://schema/address)
    assert dereferenced_schema == next(
        item for item in DEREFERENCED_SCHEMA if item["$id"] == 'las://schema/student')


"""

Get data

"""


def test_get_features(schema_store):
    student = schema_store.get_object('las://schema/student')
    assert student.get_features() == {"student_id": {"type": "string"}}


def test_get_required_features(schema_store):
    student = schema_store.get_object('las://schema/student')
    assert student.get_required_features() == ["student_id"]


def test_get_features_paths(schema_store):
    student = schema_store.get_object('las://schema/student')
    assert student.get_features_paths(schema_store) == [{'path': 'features', 'type': 'object'}, {'path': 'features.student_id', 'type': 'string', 'required': True}, {'path': 'features.firstName', 'type': 'string', 'required': True}, {'path': 'features.lastName', 'type': 'string', 'required': True}, {'path': 'features.address', 'type': 'object'}, {'path': 'features.address.features', 'type': 'object'}, {'path': 'features.address.features.street_address', 'type': 'string', 'required': True}, {'path': 'features.address.features.city', 'type': 'string', 'required': True}, {'path': 'features.address.features.state', 'type': 'string', 'required': True}]



"""

Modify existing objects

"""


def test_remove_feature(schema_store):
    """
    Get an object an remove a required feature (i.e., city)
    Besides, non-existing features are passed and ignored
    """
    address = schema_store.get_object('las://schema/address')

    address.remove_features('foo', 'city', 'bar')

    assert address.schema == {'$id': 'las://schema/address',
                              '$schema': 'http://json-schema.org/draft-07/schema#',
                              'type': 'object',
                              'allOf': [{'properties': {'features': {'type': 'object',
                                                                     "allOf": [{
                                                                             'properties': {'street_address': {'type': 'string'},
                                                                                            'state': {'type': 'string'}},
                                                                             'required': ['state', 'street_address']}]}}}]}


def test_remove_required_feature(schema_store):
    """
    Get an object an remove a required feature (i.e., city)
    Besides, non-existing features are passed and ignored
    """
    address = schema_store.get_object('las://schema/address')

    address.remove_required_features('foo', 'city', 'bar')

    assert address.schema == {'$id': 'las://schema/address',
                              '$schema': 'http://json-schema.org/draft-07/schema#',
                              'type': 'object',
                              'allOf': [{'properties': {'features': {'type': 'object',
                                                                    'allOf': [{
                                                                     'properties': {'street_address': {'type': 'string'},
                                                                                    'city': {'type': 'string'},
                                                                                    'state': {'type': 'string'}},
                                                                     'required': ['state', 'street_address']}]}}}]}
