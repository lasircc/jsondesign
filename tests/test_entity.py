import jsondesign.entity as ey
from sample_data import SCHEMA, DEREFERENCED_SCHEMA


def test_create_object():
    """
    Create an object representation of an Address
    """
    e = ey.Object(uri='las://schema/address')
    simple_string = ey.String()
    features = {'street_address': simple_string, 'city': simple_string, 'state': simple_string}
    e.set_feature(features)

    e.add_required_features('street_address')
    # entity.add_required_features prevents duplicates
    e.add_required_features('street_address', 'city', 'state')

    print('>>>>> testing object schema')
    # Match the creaded object against a target schema (i.e., las://schema/address)
    assert e.schema == next(item for item in SCHEMA if item["$id"] == 'las://schema/address')
    print('>>>>> ok!')




def test_create_reference():
    """
    Create a reference as an extension of a Python dict
    """
    r = ey.ObjectReference('las://schema/foo')
    assert r == {'$ref': 'las://schema/foo'}




def test_append_reference():
    """
    Create a reference and append it to an object
    """
    e = ey.Object(uri='las://schema/person')
    simple_string = ey.String()
    address = ey.ObjectReference('las://schema/address')

    features = {'firstName': simple_string, 'lastName': simple_string, 'address': address}
    e.set_feature(features)
    e.add_required_features('firstName', 'lastName')
    # Match the creaded object against a target schema (i.e., las://schema/address)
    assert e.schema == next(item for item in SCHEMA if item["$id"] == 'las://schema/person')
    print('>>>>> ok!')




def test_extend_entity():
    """
    Create a Student schema extending person schema (i.e., inhertiance)
    """
    student = ey.Object(uri='las://schema/student')
    student_id = ey.String()
    features = {'student_id': student_id}
    student.set_feature(features)
    student.add_required_features('student_id')
    # Inheritance
    r = ey.ObjectReference('las://schema/person')
    student.extend(r)
    # Redundant inheritance. entity.extend() is protected against this kind of redundancy
    student.extend(r)
    assert student.schema == next(item for item in SCHEMA if item["$id"] == 'las://schema/student')
    print (student.schema)



def test_dereference(schema_store):
    """
    Get an object from the store and resolve all references
    """

    student = schema_store.get_object('las://schema/student')
    student.dereference(schema_store)
    # Match the creaded object against a dereferenced target schema (i.e., las://schema/address)
    assert student.schema == next(item for item in DEREFERENCED_SCHEMA if item["$id"] == 'las://schema/student')