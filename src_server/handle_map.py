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
        self.display = True
        if(self.display): 
            self.thread = Thread(target=self.display_map)
            self.thread.start()
        
        
        # actual code here
        while True:
            pass

        
        

    def create_test_map(self):
        return [
            [Cell.WALL] * 10,
            [Cell.WALL, Cell.LIVING_ROOM, Cell.LIVING_ROOM, Cell.LIVING_ROOM, Cell.LIVING_ROOM, Cell.WALL, Cell.KITCHEN, Cell.KITCHEN, Cell.KITCHEN, Cell.WALL],
            [Cell.WALL, Cell.LIVING_ROOM, Cell.LIVING_ROOM, Cell.LIVING_ROOM, Cell.LIVING_ROOM, Cell.WALL, Cell.KITCHEN, Cell.KITCHEN, Cell.KITCHEN, Cell.WALL],
            [Cell.WALL, Cell.LIVING_ROOM, Cell.LIVING_ROOM, Cell.LIVING_ROOM, Cell.LIVING_ROOM, Cell.WALL, Cell.KITCHEN, Cell.KITCHEN, Cell.KITCHEN, Cell.WALL],
            [Cell.WALL, Cell.DOOR, Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL, Cell.DOOR, Cell.WALL],
            [Cell.WALL, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.WALL],
            [Cell.WALL, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.WALL],
            [Cell.WALL, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.WALL],
            [Cell.WALL, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.OTHER, Cell.WALL],
            [Cell.WALL] * 10
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
            Cell.WALL: 'black',
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