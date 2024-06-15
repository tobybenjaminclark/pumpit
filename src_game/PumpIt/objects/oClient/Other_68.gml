/// @description Insert description here
// You can write your code in this editor
/// @description Handles Server Connection & Parses Hand Data
/// @author Toby Benjamin Clark
/// @date   16/01/2023
 
function is_prefix(str, prefix) {
    // Get the length of the prefix
    var prefix_len = string_length(prefix);
    
    // Extract the beginning part of the string with the same length as the prefix
    var start_of_string = string_copy(str, 1, prefix_len);
    
    // Compare the extracted part with the prefix
    return start_of_string == prefix;
}
 
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
		if(originalString != "" && string_length(originalString) > 5){
			global.response = "";
			global.response = string_replace(originalString,"\n","");
			global.response = string_replace(global.response,"\"","");
			if(is_prefix(global.response, "GPT")){
				
				var body = global.response;
				var text_index = 0;

				// Maximum line length
				var max_line_length = 75;

				// Length of the body text
				var body_length = string_length(body);

				// Iterate through the text
				while (text_index < body_length) {
				    // Calculate the end index for the current segment
				    var end_index = min(text_index + max_line_length, body_length);

				    // Find the nearest space within the current line segment
				    var space_index = -1;
				    for (var i = end_index; i > text_index; i--) {
				        if (string_char_at(body, i) == " ") {
				            space_index = i;
				            break;
				        }
				    }

				    // Ensure we do not insert a newline if it results in very short segments
				    if (space_index != -1 && (space_index != body_length - 1)) {
				        body = string_insert("\n", body, space_index);
				        body = string_delete(body, space_index + 1, 1); // Remove the space character
				        text_index = space_index + 1; // Move index to after the newline
				    } else if (end_index < body_length) {
				        // If no suitable space is found, and it's not the end of the string, insert a newline at the max line length
				        body = string_insert("\n", body, end_index);
				        text_index = end_index + 1; // Move index to after the newline
				    } else {
				        text_index = body_length; // Move index to the end of the text
				    }

				    // Update the body length
				    body_length = string_length(body);
				}

				var _bi = string_length(body);
				var _in_loop = true;
				while (_bi > 0 && _in_loop){
					_bi--;
					if string_char_at(body, _bi) == "\n" {
						body = string_insert(" ", body, _bi);
						body = string_delete(body, _bi + 1, 1);
						_in_loop = false;
					}
				}

				global.last_gpt = string_replace(body, "GPT", "");
			}
		}
		show_debug_message("RESPONSE:" + global.response);
        
		try
		{
			jsonData = json_parse(originalString)
		
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
		

		buffer_write(send_buffer, buffer_string, senddata);
		network_send_raw(server_socket, send_buffer, buffer_get_size(send_buffer));
		buffer_delete(send_buffer);
		send_buffer = buffer_create(512, buffer_fixed, 1);
		
		
    }
}