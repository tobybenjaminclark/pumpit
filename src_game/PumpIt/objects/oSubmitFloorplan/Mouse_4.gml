/// @description Insert description here
// You can write your code in this editor

// Create a map to hold request data
var request_map = ds_map_create();

var str = ""
var width = ds_grid_width(global.floorplan);
var height = ds_grid_height(global.floorplan);
for (var y1 = 0; y1 < height; y1++) {
    for (var x1 = 0; x1 < width; x1++) {
        var value = ds_grid_get(global.floorplan, x1, y1);
        str = str + string(value);
    }
	str = str + "R";
}

// Add data to the map
ds_map_add(request_map, "type", "FLOORPLAN");
ds_map_add(request_map, "data", str);

// Convert the map to JSON string
var json_request = json_encode(request_map);

show_debug_message(string(json_request));

ds_list_add(global.outgoing, string(json_request));