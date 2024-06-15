/// @description Initialize Empty Grid
global.show_floorplan = true;

room_persistent = false;
floorplan = ds_grid_create(room_width / 10, room_height / 10);
ds_grid_clear(floorplan, 0);

global.selection_mode = SINGULAR;
global.left_click_pos = [-1, -1];
global.right_click_pos = [-1, -1];
