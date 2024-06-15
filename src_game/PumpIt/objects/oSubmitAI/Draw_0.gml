/// @description Insert description here
// You can write your code in this editor

draw_self();
draw_set_color(c_black);

draw_set_valign(fa_center);
draw_text(x, y, "Ask");

if(ds_list_size(global.outgoing) > 0){
	draw_text(x, y + 20, string(global.outgoing[| 0]))
}