from arcgis import GIS
from arcgis.features import FeatureLayerCollection
import json, sys


def search_layer(conn,layer_name):
    search_results = conn.content.search(layer_name, item_type='Feature Layer')
    proper_index = [i for i, s in enumerate(search_results) if '"'+layer_name+'"' in str(s)]
    found_item = search_results[proper_index[0]]
    flc = FeatureLayerCollection.fromitem(found_item)
    return flc


def update_layer_def(layer):
    # Open JSON file containing symbology update
    with open('/path/to/hosted_drawinfo_lyr.json') as json_data:
        data = json.load(json_data)
    
    layer.manager.update_definition(data)

    print("*******************UPDATED DEFINITION**********************")
    print(layer.properties)

    
def main():
    conn = GIS("https://machine.domain.com/portal", 
               "admin", "password")
    
    # Search for item, get item data)
    flc = search_layer(conn, 'layerdef')
    layer = flc.layers[1]
    print(layer.properties)
    update_layer_def(layer)

if __name__ == '__main__':
    sys.exit(main())
