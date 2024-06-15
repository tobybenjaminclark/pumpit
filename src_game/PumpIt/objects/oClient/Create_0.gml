/// @description Insert description here
// You can write your code in this editor

/// @description Insert description here
// You can write your code in this editor
/// @description Insert description here
// You can write your code in this editor
/// @description Starts Server to CV Node
/// @author Toby Benjamin Clark
/// @date   16/01/2023

global.outgoing = ds_list_create();
global.response = "";
global.last_gpt = "Hi, I'm Heat Geek, how can I help?";

client_socket = network_create_socket(network_socket_tcp);
server_socket = network_connect_raw_async(client_socket, "127.0.0.1", 7783);
//create a buffer with which to send information
send_buffer = buffer_create(2048, buffer_fixed, 1);

if(server_socket < 0) show_message("Could not connect! Try turning on the server?");
else
{
    var t_buffer = buffer_create(256, buffer_grow, 1);
    buffer_seek(t_buffer, buffer_seek_start, 0);
    buffer_write(t_buffer , buffer_string, "Hello");
    network_send_packet(client_socket, t_buffer, buffer_tell(t_buffer));
    buffer_delete(t_buffer);
}

