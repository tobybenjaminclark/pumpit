/// @description Draws Floorplan Grid

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