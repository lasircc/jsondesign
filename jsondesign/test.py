import entity
import json
import utils

e = entity.Object('Aliquot')
weight =  entity.Numeric('integer')
barcode = entity.String()
features = {'weight': weight,'barcode': barcode }
e.setFeature(features)
e.json()



