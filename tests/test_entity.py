import jsondesign.entity as ey
from sample_store import SCHEMA


def test_create_object():

    reference = {'type': 'object', '$schema': 'http://json-schema.org/draft-07/schema#', '$id': 'las://schema/Aliquot', 'title': 'Aliquot', 'properties': {'features': {'weight': {'type': 'integer'}, 'barcode': {'type': 'string'}}}}

    # Create an Aliquot
    e = ey.Object(title = 'Aliquot')
    weight =  ey.Numeric('integer')
    barcode = ey.String()
    features = {'weight': weight,'barcode': barcode }
    e.setFeature(features)
    print ('>>>>> testing object schema')
    assert e.schema == reference
    print ('>>>>> ok!')
    

    


