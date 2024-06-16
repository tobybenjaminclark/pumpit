/// @description Insert description here
// You can write your code in this editor

draw_self();
draw_set_color(c_black);

draw_set_halign(fa_center);
draw_set_valign(fa_center);
draw_text(x, y, "Simulate Local");

for (var i = 0; i < array_length(cells); i++){
	draw_set_color(c_lime);
	draw_rectangle(cells[i][0]*10, cells[i][1]*10,cells[i][0]*10 + 10, cells[i][1]*10 + 10, false);
}

for (var _x = 0; _x < ds_grid_width(tempmap); _x++){
	for (var _y = 0; _y < ds_grid_height(tempmap); _y++){

		
		var val = tempmap[# _x, _y]
		if(val < -200){ continue; }
		if(val <= 13){ draw_set_color(c_aqua); }
		else if(val > 13){ draw_set_color(c_red); }
		
		if(global.floorplan[# _x, _y] == 1) draw_set_color(c_black);
		draw_rectangle(_x*10, _y*10, _x*10 + 10, _y*10 + 10, false);
	}	
}