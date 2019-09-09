import entity
import schema_store
from sample import SCHEMA
import jsonschema





# def get(uri):

def ref_uri_handler(uri):
    print (uri)
    return SCHEMA[uri]

r = jsonschema.RefResolver(base_uri="",
                        handlers={"las":ref_uri_handler}, referrer=None, cache_remote=False)
                            
  


# store = schema_store.Schema_Store(get = get)





e = entity.Object('Aliquot')
weight =  entity.Numeric('integer')
barcode = entity.String()
features = {'weight': weight,'barcode': barcode }
e.setFeature(features)

# a = entity.Object('AnotherSubStuff')
# barcode = entity.String()
# e.setFeature({'foo':a})

e.json()



