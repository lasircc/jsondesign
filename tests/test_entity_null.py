import jsondesign.entity as ey


def test_null_creation():
    a = ey.Null()
    assert a.schema == { "type": "null" }