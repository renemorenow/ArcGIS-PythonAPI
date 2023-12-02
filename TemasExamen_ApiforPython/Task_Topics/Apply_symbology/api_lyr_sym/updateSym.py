from arcgis import GIS
import json, sys

def search_layer(conn,layer_name):
    search_results = conn.content.search(layer_name, item_type='*')
    proper_index = [i for i, s in enumerate(search_results) if '"'+layer_name+'"' in str(s)]
    found_item = search_results[proper_index[0]]
    get_item = conn.content.get(found_item.id)
    return get_item

def update_layer_def(item):
    item_data = item.get_data()
    if item_data is not None:
        # Here note we are changing a specific part of the Layer Definition
        layer_def = item_data['layers'][3]['layerDefinition']
        print("*******************ORIGINAL DEFINITION*********************")
        print(json.dumps(item_data, indent=4, sort_keys=True))

        # Open JSON file containing symbology update
        with open('/path/to/drawingInfo.json') as json_data:
            data = json.load(json_data)

        # Set the drawingInfo equal to what is in JSON file
        layer_def['drawingInfo'] = data


        # Set the item_properties to include the desired update
        item_properties = {"text": json.dumps(item_data)}

        # 'Commit' the updates to the Item
        item.update(item_properties=item_properties)

        # Print item_data to see that changes are reflected
        new_item_data = item.get_data()
        print("***********************NEW DEFINITION**********************")
        print(json.dumps(new_item_data, indent=4, sort_keys=True))
    
    else:
        print("There is no Layer Definition at the moment..creating one...")
        create_layer_def(item)

def create_layer_def(item):   
    with open('/path/to/complete.json') as json_data:
        data = json.load(json_data)

    # Set the item_properties to include the desired update
    item_properties = {"text": json.dumps(data)}

    # 'Commit' the updates to the Item
    item.update(item_properties=item_properties)

    # Print item_data to see that changes are reflected
    item_data = item.get_data()
    print("*********************CREATED DEFINITION************************")
    print(json.dumps(item_data, indent=4, sort_keys=True))   
    
def main():
    conn = GIS("https://machine.domain.com/portal", 
               "admin", "password")
    
    # Search for item, get item data)
    item = search_layer(conn, 'earl_api_usalyraw')
    # Attempt to update Layer Definition
    update_layer_def(item)

if __name__ == '__main__':
    sys.exit(main())
