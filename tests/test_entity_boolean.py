import jsondesign.entity as ey


def test_boolean_creation():
    a = ey.Boolean()
    assert a.schema == { "type": "boolean" }