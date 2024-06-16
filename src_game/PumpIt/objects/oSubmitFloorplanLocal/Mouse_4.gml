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
    if (!ds_map_exists(filled_cells_set, key)) {
        array_push(interior_cells, ac);
    }
}

// Clean up
ds_map_destroy(filled_cells_set);

// Result
cells = interior_cells;
