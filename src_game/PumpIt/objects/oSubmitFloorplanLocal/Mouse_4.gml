
tempmap = ds_grid_create(ds_grid_width(global.floorplan), ds_grid_height(global.floorplan));
for (var _x = 0; _x < ds_grid_width(tempmap); _x++) {
    for (var _y = 0; _y < ds_grid_height(tempmap); _y++) {
        tempmap[# _x, _y] = OUTSIDE_TEMP;
    }
}


// Initialize all_cells array
all_cells = [];
for (var _x = 0; _x < ds_grid_width(global.floorplan); _x++) {
    for (var _y = 0; _y < ds_grid_height(global.floorplan); _y++) {
        array_push(all_cells, [_x, _y]);
    }
}

// Perform flood fill and get the filled cells
cells = flood_fill(global.floorplan, 0, 0);

// Create a set for filled cells for faster lookup
var filled_cells_set = ds_map_create();
for (var i = 0; i < array_length(cells); i++) {
    var ec = cells[i];
    var key = string(ec[0]) + "," + string(ec[1]);
    ds_map_add(filled_cells_set, key, true);
}

// Determine the interior cells (cells not reached by flood fill)
interior_cells = [];
for (var _c = 0; _c < array_length(all_cells); _c++) {
    var ac = all_cells[_c];
    var key = string(ac[0]) + "," + string(ac[1]);
    if (!ds_map_exists(filled_cells_set, key)) 
	{
		if(global.floorplan[# ac[0], ac[1]] == 0){
			array_push(interior_cells, ac);
			tempmap[# ac[0], ac[1]] = INSIDE_TEMP;
		}
    }
}


// Get boundaries
emitters = ds_list_create();
interior_cells = [];
var correct_count = 0
for (var _c = 0; _c < array_length(all_cells); _c++) {
    var ac = all_cells[_c];
    var key = string(ac[0]) + "," + string(ac[1]);
    if (!ds_map_exists(filled_cells_set, key)) 
	{
		if(global.floorplan[# ac[0], ac[1]] == 0){
			
			array_push(interior_cells, ac);
			var directions = [
		        [1, 0],  // right
		        [-1, 0], // left
		        [0, 1],  // down
		        [0, -1]  // up
		    ];
	
			var x1 = ac[0];
			var y1 = ac[1];
			var hit_boundary = false;
			for (var i = 0; i < array_length(directions); i++) {
				var new_x = x1 + directions[i][0];
				var new_y = y1 + directions[i][1];
				if(global.floorplan[# new_x, new_y] == 1){
					hit_boundary = true;
				}
			}	
	
			if(hit_boundary){
				correct_count++;
				
				show_debug_message(string(ac[0]) + " " + string(ac[1]) + " : is boundary");
				if(random(1) < 0.1){
					tempmap[# ac[0], ac[1]] = -150;
					ds_list_add(emitters, ac);
				}
			}
		}
    }
}





var EMITTER_POWER = 15;
for(var _e = 0; _e < ds_list_size(emitters); _e++){
	var emit = emitters[| _e];
	var start_x = emit[0];
	var start_y = emit[1];
	var max_distance = 15;
	
	// Create a new DS grid with the same dimensions as global.floorplan
	var ds_grid = ds_grid_create(ds_grid_width(global.floorplan), ds_grid_height(global.floorplan));

	// Copy the contents of global.floorplan into the new_grid
	ds_grid_copy(ds_grid, global.floorplan);

	
	show_debug_message("Simulating emitter " + string(_e) + " at position " + string(start_x) + " " + string(start_y));
	
    // Check if the start position is a 'free' cell
    if (ds_grid[# start_x, start_y] != 0) {
        return [];
    }

    // Create a queue for BFS, storing [x, y, distance]
    var queue = ds_queue_create();
    ds_queue_enqueue(queue, [start_x, start_y, 0]);

    // List to store the flooded coordinates
    var flooded_coords = [];

    // Directions for moving in 4 possible ways (up, down, left, right)
    var directions = [
        [1, 0],  // right
        [-1, 0], // left
        [0, 1],  // down
        [0, -1]  // up
    ];

    // Mark the start cell as visited by changing its value (to prevent revisiting)
    ds_grid[# start_x, start_y] = -1;

    // BFS loop
    while (!ds_queue_empty(queue)) {
        // Get the current cell coordinates and distance
        var current = ds_queue_dequeue(queue);
        var x1 = current[0];
        var y1 = current[1];
        var distance = current[2];
		var skip = false;
		
		show_debug_message("Set temp at " + string(x1) + " " + string(y1) + " to " + string(((max_distance - distance) * 5)));
		tempmap[# x1, y1] = tempmap[# x1, y1] + ((max_distance - distance));

        // Add the current cell to the flooded list
        array_push(flooded_coords, [x1, y1]);

        // Stop further expansion if the distance limit is reached
        if (distance >= max_distance) {
            skip = true;
        }

        if(!skip){// Check all 4 directions
	        for (var i = 0; i < array_length(directions); i++) {
	            var new_x = x1 + directions[i][0];
	            var new_y = y1 + directions[i][1];

	            // Check if the new cell is within the grid bounds and is a 'free' cell
	            if (new_x >= 0 && new_x < ds_grid_width(ds_grid) && new_y >= 0 && new_y < ds_grid_height(ds_grid) && ds_grid[# new_x, new_y] == 0) {
	                // Mark the cell as visited and add to the queue with incremented distance
	                ds_grid[# new_x, new_y] = -1;
	                ds_queue_enqueue(queue, [new_x, new_y, distance + 1]);
	            }
	        }
		}
    }
	
	tempmap[# start_x, start_y] = -150;
    // Clean up the queue
    ds_queue_destroy(queue);

}

var EMITTER_POWER = 15;
for(var _e = 0; _e < ds_list_size(emitters); _e++){
	var emit = emitters[| _e];
	var start_x = emit[0];
	var start_y = emit[1];
	var max_distance = 15;
	tempmap[# start_x, start_y] = -150;
	
}
// Clean up	
ds_map_destroy(filled_cells_set);