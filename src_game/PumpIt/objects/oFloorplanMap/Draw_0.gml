/// @description Draws Floorplan Grid

if(global.selection_mode == LINE && global.left_click_pos[0] != -1 && global.left_click_pos[1] != -1){
	draw_set_color(c_black)
	draw_text(mouse_x + 10, mouse_y + 10, "Distance");
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