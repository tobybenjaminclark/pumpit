# This is where you can write physics stuff!
# Test again
import numpy as np


def energy_flow(K, area, temp_grad):
    energy_flow = -K * area * temp_grad
    return energy_flow

def therm_conduct(lamb):
    pass

def calc_temp_gradient(coordinate):     #coordinate is [y, x] in room
    init_temp = grid[coordinate[0]][coordinate[1]]  # gets the temp based on the coordinate
    temp_gradients = []
    for y in range(coordinate[0]-1,coordinate[0]+2):
        if -1 < y < len(grid) and y != coordinate[0]:
            neighbour_temp = grid[y][coordinate[1]]
            temp_diff = neighbour_temp - init_temp
            temp_gradients.append(temp_diff)
    for x in range(coordinate[1]-1,coordinate[1]+2):
        if -1 < x < len(grid[coordinate[0]]) and x != coordinate[1]:
            neighbour_temp = grid[coordinate[0]][x]
            temp_diff = neighbour_temp - init_temp
            temp_gradients.append(temp_diff)
    total = 0
    for i in temp_gradients:
        total += i
    average = total / 4
    return average

grid_size = (5,5)
grid = np.full(grid_size, 20+273.15)
grid[3][3] = 273.15 + 50
gradient_grid = np.zeros(grid_size)
print(gradient_grid)
for n in range(20):
    for x in range(0,grid_size[0]):
        for y in range(0,grid_size[1]):
            gradient_grid[x,y] = calc_temp_gradient((x,y))
print(grid)
print(gradient_grid)
