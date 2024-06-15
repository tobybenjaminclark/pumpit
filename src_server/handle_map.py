from enum import Enum
import tkinter as tk
from threading import Thread

class Cell(Enum):
    WALL = 1
    WINDOW = 2
    DOOR = 2
    LIVING_ROOM = 3
    KITCHEN = 4
    BATHROOM = 5
    BEDROOM = 6
    OTHER = 7


class MapHandler():

    def __init__(self):
        self.map = self.create_test_map()
        self.heatmap = self.create_test_heatmap()

        self.display = False
        if(self.display): 
            self.thread = Thread(target=self.display_map)
            self.thread.start()

        
        
        


    def handle_maps(self):

        # generate permutations of maps

        # run simulation on each

        # return the best, and the heatmap

        pos = self.find_possible_unit_positions()

        for x in range(0, len(pos) - 1, 2):
            #print(f"{pos[x]}{pos[x+1]}")
            pass


        return self.map, self.heatmap


    def find_possible_unit_positions(self):
        # find lengths of vertical and horizontal wall stretches


        wall_vals = []

        # if you find a start value, search until you find an end value





        for y in range(len(self.map)):

            counter = 0
            
            for x in range(len(self.map[y])):
                
                if self.map[y][x] == Cell.WALL.value:

                    if counter == 0:
                        wall_vals.append([x, y])
                    elif x == len(self.map[y]) - 1:
                        wall_vals.append([x, y])

                    counter +=1
                
                
                else:
                    if counter > 0:
                        counter = 0
                        # do not add singular length walls
                        if [x-1, y] in wall_vals:
                            wall_vals.remove([x-1,y])
                        else:
                            wall_vals.append([x-1, y])

        return wall_vals
        


            
        

                    
                
        
        
    def create_test_heatmap(self):

        return [[20] * 10] * 10

    def create_test_map(self):
        return [
            [Cell.WALL.value] * 10,
            [Cell.WALL.value, Cell.LIVING_ROOM.value, Cell.LIVING_ROOM.value, Cell.LIVING_ROOM.value, Cell.LIVING_ROOM.value, Cell.WALL.value, Cell.KITCHEN.value, Cell.KITCHEN.value, Cell.KITCHEN.value, Cell.WALL.value],
            [Cell.WALL.value, Cell.LIVING_ROOM.value, Cell.LIVING_ROOM.value, Cell.LIVING_ROOM.value, Cell.LIVING_ROOM.value, Cell.WALL.value, Cell.KITCHEN.value, Cell.KITCHEN.value, Cell.KITCHEN.value, Cell.WALL.value],
            [Cell.WALL.value, Cell.LIVING_ROOM.value, Cell.LIVING_ROOM.value, Cell.LIVING_ROOM.value, Cell.LIVING_ROOM.value, Cell.WALL.value, Cell.KITCHEN.value, Cell.KITCHEN.value, Cell.KITCHEN.value, Cell.WALL.value],
            [Cell.WALL.value, Cell.DOOR.value, Cell.WALL.value, Cell.WALL.value, Cell.WALL.value, Cell.WALL.value, Cell.WALL.value, Cell.WALL.value, Cell.DOOR.value, Cell.WALL.value],
            [Cell.WALL.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.WALL.value],
            [Cell.WALL.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.WALL.value],
            [Cell.WALL.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.WALL.value],
            [Cell.WALL.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.OTHER.value, Cell.WALL.value],
            [Cell.WALL.value] * 10
        ]

    

    def display_map(self):

        self.window = tk.Tk()
        
        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                color = self.get_color(cell)
                frame = tk.Frame(
                    master=self.window,
                    width=20,
                    height=20,
                    bg=color
                )
                frame.grid(row=i, column=j)

        self.window.mainloop()
        

    def get_color(self, cell):
        color_map = {
            Cell.WALL.value: 'purple',
            Cell.WINDOW.value: 'blue',
            Cell.DOOR.value: 'brown',
            Cell.LIVING_ROOM.value: 'green',
            Cell.KITCHEN.value: 'yellow',
            Cell.BATHROOM.value: 'aqua',
            Cell.BEDROOM.value: 'purple',
            Cell.OTHER.value: 'gray'
        }
        return color_map.get(cell, 'white')

m = MapHandler()