/// @description Insert description here
// You can write your code in this editor

draw_self();
draw_set_color(c_black);

draw_set_halign(fa_center);
draw_set_valign(fa_center);
draw_text(x, y, "Simulate Local");


for (var _x = 0; _x < ds_grid_width(tempmap); _x++){
	for (var _y = 0; _y < ds_grid_height(tempmap); _y++){
		
		
		var val = tempmap[# _x, _y]

		
		if(val < -200){ continue; }
		if(val <= -150){ draw_set_color(c_yellow); }
		
		// Define the color endpoints
		var cold_color = c_blue; // Blue for cold
		var hot_color = c_red;  // Red for hot

		// Interpolate the color based on the value
		var interpolated_color = interpolate_color(val, -40, 40, cold_color, hot_color);

		// Set the interpolated color
		draw_set_color(interpolated_color);
	
		if(global.floorplan[# _x, _y] == 1){draw_set_color(c_black);}
		// Draw the rectangle
		draw_rectangle(_x * 10, _y * 10, _x * 10 + 10, _y * 10 + 10, false);

		

		
		draw_set_color(c_lime);
		draw_set_font(fntTiny);
		if(_x mod 5 == 0 && _y mod 2 == 0) draw_text(_x*10 + 5, _y*10 + 5, string(val));
		draw_set_color(c_black)
	}	
}