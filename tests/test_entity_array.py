import jsondesign.entity as ey


def test_array_creation():
    a = ey.Array()
    assert a.schema == { "type": "array" }




def test_array_simple_items():
    """
    Create an array of strings
    """
    a = ey.Array()
    s = ey.String()
    a.set_ItemsType(s)
    assert a.schema == { "type": "array", "items" : {"type": "string" }}




def test_array_complex_items():
    """
    Create an array of objects through refrences
    """
    a = ey.Array()
    r = ey.ObjectReference('las://schema/foo')
    a.set_ItemsType(r)
    assert a.schema == { "type": "array", "items" : {"$ref": "las://schema/foo" }}