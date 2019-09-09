import entity


e = entity.Object('Aliquot')
weight =  entity.Numeric('integer')
barcode = entity.String()
features = {'weight': weight,'barcode': barcode }
e.setFeature(features)

# a = entity.Object('AnotherSubStuff')
# barcode = entity.String()
# e.setFeature({'foo':a})



e.json()



