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
		global.response = originalString;
        
		
		try
		{
			
			jsonData = json_parse(originalString)
		
			show_debug_message(jsonData);
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
		

		var senddata = ""
		if(ds_list_size(global.outgoing) > 0){
			show_message("sent other")
			senddata = global.outgoing[| 0];
			ds_list_delete(global.outgoing, 0);
		}
		
		show_debug_message(senddata);
		buffer_write(send_buffer, buffer_string, senddata);
		network_send_raw(server_socket, send_buffer, buffer_get_size(send_buffer));
		buffer_delete(send_buffer);
		send_buffer = buffer_create(512, buffer_fixed, 1);
		
		
    }
}