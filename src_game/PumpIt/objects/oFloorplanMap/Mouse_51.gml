/// @description Insert description here
// You can write your code in this editor
if(!global.show_floorplan) return;

if(mouse_x >= 992){
	return;
}


if(global.selection_mode == LINE &&
	(global.left_click_pos[0] != -1)&&
	(global.left_click_pos[0] != -1)){

	global.right_click_pos = [mouse_x, mouse_y];
	var _grid_x1 = floor(global.left_click_pos[0]);
	var _grid_y1 = floor(global.left_click_pos[1]);
	
	var _grid_x2 = floor(global.right_click_pos[0]);
	var _grid_y2 = floor(global.right_click_pos[1]);

	var _points = bressenhams_line_algorithm(_grid_x1, _grid_y1, _grid_x2, _grid_y2);
	
	global.left_click_pos = [-1, -1];
	global.right_click_pos = [-1, -1];
	
	for(var _i = 0; _i < array_length(_points); _i++){
		// Ensure the coordinates are within the grid bounds
		show_debug_message(_grid_x1);
		show_debug_message(_grid_y1);
		show_debug_message(_grid_x2);
		show_debug_message(_grid_y2);
		show_debug_message(_points);
		var _grid_x = _points[_i][0]
		var _grid_y = _points[_i][1]
		_grid_x = floor(_grid_x / 10);
		_grid_y = floor(_grid_y / 10);
		
		if (_grid_x >= 0 && _grid_x < ds_grid_width(floorplan) && _grid_y >= 0 && _grid_y < ds_grid_height(floorplan)) {
		    ds_grid_set(floorplan, _grid_x, _grid_y, global.current_value);
		}	
	}

}

