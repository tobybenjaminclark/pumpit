function flood_fill(ds_grid, start_x, start_y) {
    // Check if the start position is a 'free' cell
    if (ds_grid[# start_x, start_y] != 0) {
        return [];
    }

    // Create a queue for BFS
    var queue = ds_queue_create();
    ds_queue_enqueue(queue, [start_x, start_y]);

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
        // Get the current cell coordinates
        var current = ds_queue_dequeue(queue);
        var x1 = current[0];
        var y1 = current[1];

        // Add the current cell to the flooded list
        array_push(flooded_coords, current);

        // Check all 4 directions
        for (var i = 0; i < array_length(directions); i++) {
            var new_x = x1 + directions[i][0];
            var new_y = y1 + directions[i][1];

            // Check if the new cell is within the grid bounds and is a 'free' cell
            if (new_x >= 0 && new_x < ds_grid_width(ds_grid) && new_y >= 0 && new_y < ds_grid_height(ds_grid) && ds_grid[# new_x, new_y] == 0) {
                // Mark the cell as visited and add to the queue
                ds_grid[# new_x, new_y] = -1;
                ds_queue_enqueue(queue, [new_x, new_y]);
            }
        }
    }

    // Clean up the queue
    ds_queue_destroy(queue);

    // Return the list of flooded coordinates
    return flooded_coords;
}
