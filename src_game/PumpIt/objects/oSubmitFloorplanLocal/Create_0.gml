/// @description Insert description here
// You can write your code in this editor
randomize();
randomize();
randomize();
randomize();

var width = ds_grid_width(global.floorplan)
var height =  ds_grid_height(global.floorplan)
tempmap = ds_grid_create(width,height);

for (var _x = 0; _x < ds_grid_width(tempmap); _x++){
	for (var _y = 0; _y < ds_grid_height(tempmap); _y++){
		tempmap[# _x, _y] = -255
	}	
}

cells = [];