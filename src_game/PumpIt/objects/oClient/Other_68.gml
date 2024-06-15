/// @description Insert description here
// You can write your code in this editor
/// @description Handles Server Connection & Parses Hand Data
/// @author Toby Benjamin Clark
/// @date   16/01/2023
 
var n_id = ds_map_find_value(async_load, "id");
if(n_id == server_socket)
{
    var t = ds_map_find_value(async_load, "type");
    var socketlist = ds_list_create();
 
    if(t == network_type_connect)
    {
        var sock = ds_map_find_value(async_load, "socket");
        ds_list_add(socketlist, sock);
    }
 
    if(t == network_type_data)
    {
        var t_buffer = ds_map_find_value(async_load, "buffer"); 
        var cmd_type = buffer_read(t_buffer, buffer_string);
 
        // Original string
        var originalString = string(cmd_type);
		global.last_repsonse = originalString;
 
        jsonData = json_parse(originalString)
		
		show_debug_message(jsonData);
		
		try
		{
			
		
	        // Check if the struct has variable
	        if variable_struct_exists(jsonData, "map")
	        {
				show_debug_message(jsonData.map);
			}
		
			if variable_struct_exists(jsonData, "heatmap")
	        {
				show_debug_message(jsonData.heatmap);
			}
		
 
		}
		catch(_ex)
		{
		}
		
		
		buffer_seek(send_buffer, buffer_seek_start, 0);
		
		// toby - for some reason the last two chars are not sent over the socket
		// hack fix send two extra chars
		buffer_write(send_buffer, buffer_string, global.outgoing);
		network_send_raw(server_socket, send_buffer, buffer_get_size(send_buffer));
		global.last_outgoing = global.outgoing;
		global.outgoing = "EMPTY";
		
		
    }
}