function bfs_bordering_walls(ds_grid, start_x, start_y) {
    // Check if the start position is a 'free' cell
    if (ds_grid[# start_x, start_y] != 0) {
        return ds_list_create(); // Return an empty DS list if the start cell is not 'free'
    }

    // Create a queue for BFS
    var queue = ds_queue_create();
    ds_queue_enqueue(queue, [start_x, start_y]);

    // Create a DS list to store the cells bordering a wall
    var bordering_cells = ds_list_create();

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
        // Get the current cell coordinates
        var current = ds_queue_dequeue(queue);
        var x1 = current[0];
        var y1 = current[1];

        // Check all 4 directions for neighboring walls
        var is_bordering_wall = false;
        for (var i = 0; i < array_length(directions); i++) {
            var new_x = x1 + directions[i][0];
            var new_y = y1 + directions[i][1];

            // Check if the new cell is within the grid bounds
            if (new_x >= 0 && new_x < ds_grid_width(ds_grid) && new_y >= 0 && new_y < ds_grid_height(ds_grid)) {
                // If the neighboring cell is a boundary, mark the current cell as bordering a wall
                if (ds_grid[# new_x, new_y] != 0) {
                    is_bordering_wall = true;
                }
                // If the neighboring cell is a free cell, add it to the queue if it hasn't been visited yet
                else if (ds_grid[# new_x, new_y] == 0) {
                    ds_grid[# new_x, new_y] = -1; // Mark as visited
                    ds_queue_enqueue(queue, [new_x, new_y]);
                }
            }
        }

        // If the current cell is bordering a wall, add it to the list
        if (is_bordering_wall) {
            ds_list_add(bordering_cells, [x1, y1]);
        }
    }

    // Clean up the queue
    ds_queue_destroy(queue);

    // Return the DS list of cells bordering walls
    return bordering_cells;
}