import jsondesign.entity as ey
from sample_store import SCHEMA


def test_create_object():


    # Create an Aliquot
    e = ey.Object(uri='las://schema/Aliquot')
    weight = ey.Numeric('integer')
    barcode = ey.String()
    features = {'weight': weight, 'barcode': barcode}
    e.setFeature(features)
    print('>>>>> testing object schema')

    assert e.schema == {'type': 'object', '$schema': 'http://json-schema.org/draft-07/schema#', '$id': 'las://schema/Aliquot',
                 'properties': {'features': {'weight': {'type': 'integer'}, 'barcode': {'type': 'string'}}}}

    print('>>>>> ok!')




def test_append_refrence():
    r = ey.ObjectReference('las://schema/foo')
    assert r == {'$ref': 'las://schema/foo'}




# def test_create_reference():

#     r = ey.ObjectReference('las://schema/foo')

#     e = ey.Object(uri='las://schema/Aliquot')
#     weight = ey.Numeric('integer')
#     barcode = ey.String()
#     features = {'weight': weight, 'barcode': barcode, 'foo' : r}
#     e.setFeature(features)

#     assert e.schema == {'type': 'object', '$schema': 'http://json-schema.org/draft-07/schema#', '$id': 'las://schema/Aliquot',
#                  'properties': {'features': {'weight': {'type': 'integer'}, 'barcode': {'type': 'string'},'foo': {'$ref': 'las://schema/foo'}}}}




# def test_dereference(schema_store):
#     # get an object from the test store
#     car = schema_store.get_object('las://schema/car')
#     car.dereference(schema_store)
#     assert car.schema == {
#         '$id': 'las://schema/car',
#         '$schema': 'http://json-schema.org/draft-07/schema#',
#         'type': 'object', 'properties': {
#             'engine': {
#                 '$id': 'las://schema/engine',
#                 '$schema': 'http://json-schema.org/draft-07/schema#',
#                 'type': 'object',
#                 'properties': {
#                     'color': {
#                         'type': 'string'
#                     },
#                     'manufacturer': {
#                         '$id': 'las://schema/manufacturer',
#                         '$schema': 'http://json-schema.org/draft-07/schema#',
#                         'type': 'object', 'properties': {
#                                 'name': {
#                                     'type': 'string'
#                                 },
#                             'vat_number': {
#                                     'type': 'string'
#                                     }
#                         }
#                     }
#                 }
#             },
#             'color': {
#                 'type': 'string'
#             },
#             'manufacturer':
#             {
#                 '$id': 'las://schema/manufacturer',
#                 '$schema': 'http://json-schema.org/draft-07/schema#',
#                 'type': 'object',
#                 'properties': {
#                     'name': {
#                         'type': 'string'
#                     },
#                     'vat_number': {
#                         'type': 'string'
#                     }
#                 }
#             }
#         }
#     }




# def test_dereference_extended_schema(schema_store):

#     car = schema_store.get_object('las://schema/car')
#     r = ey.ObjectReference('las://schema/engine')
#     car.extend(r)
#     car.dereference(schema_store)
#     print(car.schema)

