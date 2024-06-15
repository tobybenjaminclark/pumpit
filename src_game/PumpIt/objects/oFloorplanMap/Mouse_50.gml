/// @description Insert description here
// You can write your code in this editor

/// @description Insert description here
// You can write your code in this editor
/// @description Left Click

var _grid_x = floor(mouse_x / 10);
var _grid_y = floor(mouse_y / 10);

// Ensure the coordinates are within the grid bounds
if (_grid_x >= 0 && _grid_x < ds_grid_width(floorplan) && _grid_y >= 0 && _grid_y < ds_grid_height(floorplan)) {
    ds_grid_set(floorplan, _grid_x, _grid_y, global.current_value);
}
