import jsondesign.entity as ey


def test_string_creation():

    s = ey.String()
    assert s.schema == {"type": "string"}




def test_string_creation_with_description():

    s = ey.String()
    s.set_description("The person's last name.")
    assert s.schema == {"type": "string", "description": "The person's last name."} 




def test_length_constraints():

    s = ey.String()
    s.set_minLength(2)
    s.set_maxLength(3)
    assert s.schema == {"type": "string", "minLength": 2,
                        "maxLength": 3}




def test_regex():
    s = ey.String()
    s.set_regex("^(\\([0-9]{3}\\))?[0-9]{3}-[0-9]{4}$")
    assert s.schema == {"type": "string",
                        "pattern": "^(\\([0-9]{3}\\))?[0-9]{3}-[0-9]{4}$"}
