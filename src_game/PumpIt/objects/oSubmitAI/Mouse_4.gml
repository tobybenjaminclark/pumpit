/// @description Insert description here
// You can write your code in this editor

// Create a map to hold request data
var request_map = ds_map_create();

// Add data to the map
ds_map_add(request_map, "type", "GPT");
ds_map_add(request_map, "prompt", global.input_text);

// Convert the map to JSON string
var json_request = json_encode(request_map);

// Clean up the map
ds_map_destroy(request_map);

ds_list_add(global.outgoing, json_request);