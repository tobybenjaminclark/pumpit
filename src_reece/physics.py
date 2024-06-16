# This is where you can write physics stuff!
# Test again
import numpy as np
import time


thermal_conductivity = 0.024
def heat_flux(temp_gradient):
    heat_flux = thermal_conductivity * temp_gradient

# do physix
def energy_flow(K, area, temp_grad):
    energy_flow = -K * area * temp_grad
    return energy_flow

def therm_conduct():
    SHC = 1005
    density = 1.225
    vol_heat_cap =  density    #SHC is specific heat capacity, atm is standard atmospheric pressure
    boltzmann = 1.381 * (10**-23)
    mean_free_path = 10**-7

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
    average = total / len(temp_gradients)
    return average

print("hello")
grid_size = (10,10)     #x by y
grid = np.full(grid_size, 20)
heat_pump = (1,1)   #x, y
hp_start_temp =  50
hp_final_temp = 50
hp_step = 0
grid[heat_pump[0]][heat_pump[1]] = hp_start_temp
gradient_grid = np.zeros(grid_size)
start = time.time()
for i in range(100):
    for x in range(0,grid_size[0]):
        for y in range(0,grid_size[1]):
            if not( x == heat_pump[0] and y == heat_pump[1]):
                gradient_grid[x,y] = calc_temp_gradient((x,y))
                if x == 0 or x == grad_size[0] or y == 0 or y == grad_size[1]:  # wall tile
                    grid += wall_heat_loss()
    grid += gradient_grid

end = time.time()

print(grid)
print(f"elapsed time: {end - start}")


def barrier(barrier_type, outside_temp, inside_temp, wall_thickness = 0.2):
    if barrier_type == 1:
        k = 1.31    #brick
    if barrier_type == 2:   #https://reprap.org/wiki/Thermal_Conductivity
        k = 0.48    #plaster gypsum
    if barrier_type == 3:
        k = 1.05    #glass
    if barrier_type == 4:
        k = 0.17    #wood
    heat_flux = k * ((inside_temp - outside_temp)/wall_thickness)   #k is thermal heat capacity
    return heat_flux