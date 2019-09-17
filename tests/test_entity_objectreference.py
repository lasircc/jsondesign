import jsondesign.entity as ey

def test_create_reference():
    """
    Create a reference as an extension of a Python dict
    """
    r = ey.ObjectReference('las://schema/foo')
    assert r == {'$ref': 'las://schema/foo'}