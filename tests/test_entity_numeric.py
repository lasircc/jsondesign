import jsondesign.entity as ey



def test_integer_creation():

    s = ey.Numeric("integer")
    assert s.schema == {"type": "integer"}




def test_number_creation():
    s = ey.Numeric("number")
    assert s.schema == {"type": "number"}




def test_multipleOf():
    s = ey.Numeric("integer")
    s.set_multipleOf(10)
    assert s.schema == {"type": "integer", "multipleOf" : 10 }




def test_exclusive_range():
    # 0 < x < 10
    s = ey.Numeric("integer")
    s.set_minimum(0)
    s.set_maximum(10)
    assert s.schema == {"type": "integer", "exclusiveMinimum" : 0, "exclusiveMaximum" : 10 }




def test_inclusive_range():
    # 0 < x < 10
    s = ey.Numeric("integer")
    s.set_minimum(0, exclusive=False)
    s.set_maximum(10, exclusive=False)
    assert s.schema == {"type": "integer", "minimum" : 0, "maximum" : 10 }