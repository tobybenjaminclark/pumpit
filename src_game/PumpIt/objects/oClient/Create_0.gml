/// @description Insert description here
// You can write your code in this editor

client_socket = network_create_socket(network_socket_tcp);
server_socket = network_connect_raw_async(client_socket, "10.13.22.37", 9999);

if(server_socket < 0) show_message("Could not connect! Try turning on the server?");
else
{
    var t_buffer = buffer_create(256, buffer_grow, 1);
    buffer_seek(t_buffer, buffer_seek_start, 0);
    buffer_write(t_buffer , buffer_string, "Hello");
    network_send_packet(client_socket, t_buffer, buffer_tell(t_buffer));
    buffer_delete(t_buffer);
}