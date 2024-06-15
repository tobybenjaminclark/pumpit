/// @description Draws Floorplan Grid
if(!global.show_floorplan) return;

if(global.selection_mode == LINE && global.left_click_pos[0] != -1 && global.left_click_pos[1] != -1){
	
	var p1 = global.left_click_pos;
	var p2 = [mouse_x, mouse_y];
	
	// Calculate the differences
	var dx = p2[0] - p1[0];
	var dy = p2[1] - p1[1];

	// Calculate the Euclidean distance
	var distance = sqrt((dx * dx) + (dy * dy));


	draw_set_color(c_black);
	draw_set_font(fntSmallCool);
	distance = round(((distance / 10) / 5) * 10) / 10
	draw_text(p1[0] + (dx/2) + 10, p1[1] + (dy/2) + 10, string(distance) + "m");
	draw_line(p1[0], p1[1], mouse_x, mouse_y);
	
}

for (var _x = 0; _x < ds_grid_width(floorplan); _x += 1) {
    for (var _y = 0; _y < ds_grid_height(floorplan); _y += 1) {
        if (ds_grid_get(floorplan, _x, _y) == 1) {
            draw_sprite(sprWallTile, 0, _x * 10, _y * 10);
        }
		if (ds_grid_get(floorplan, _x, _y) == 2) {
            draw_sprite(sprWindowTile, 0, _x * 10, _y * 10);
        }
    }
}