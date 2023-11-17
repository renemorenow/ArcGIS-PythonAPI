from arcgis import GIS
import json, sys

#service: https://sampleserver6.arcgisonline.com/arcgis/rest/services/USA/MapServer

def search_item(conn,layer_name):
    search_results = conn.content.search(layer_name, item_type='Web Map')
    proper_index = [i for i, s in enumerate(search_results) if '"'+layer_name+'"' in str(s)]
    found_item = search_results[proper_index[0]]
    get_item = conn.content.get(found_item.id)
    return get_item

def update_wm_layerdef(item):
    item_data = item.get_data()

    print("*******************ORIGINAL DEFINITION*********************")
    print(json.dumps(item_data, indent=4, sort_keys=True))
    # Open JSON file containing symbology update
    with open('/path/to/webmaplyr.json') as json_data:
        data = json.load(json_data)

    # Set the item_properties to include the desired update
    item_properties = {"text": json.dumps(data)}

    # 'Commit' the updates to the Item
    item.update(item_properties=item_properties)

    # Print item_data to see that changes are reflected
    new_item_data = item.get_data()
    print("***********************NEW DEFINITION**********************")
    print(json.dumps(new_item_data, indent=4, sort_keys=True))

def main():
    conn = GIS("https://machine.domain.com/portal", 
               "admin", "password")
    
    # Search for item, get item data)
    item = search_item(conn, 'wm_lyrsym')
    update_wm_layerdef(item)


if __name__ == '__main__':
    sys.exit(main())
