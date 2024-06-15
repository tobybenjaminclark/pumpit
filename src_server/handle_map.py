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

        return self.map, self.heatmap


        
        
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
            Cell.WALL: 'purple',
            Cell.WINDOW: 'blue',
            Cell.DOOR: 'brown',
            Cell.LIVING_ROOM: 'green',
            Cell.KITCHEN: 'yellow',
            Cell.BATHROOM: 'aqua',
            Cell.BEDROOM: 'purple',
            Cell.OTHER: 'gray'
        }
        return color_map.get(cell, 'white')

m = MapHandler()