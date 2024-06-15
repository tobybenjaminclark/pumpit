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

        self.handle_maps()

        
        
        


    def handle_maps(self):

        # generate permutations of maps

        # run simulation on each

        # return the best, and the heatmap

        pos = self.find_walls_start_end(self.map)
        print(pos)

        return self.map, self.heatmap

    def find_walls_start_end(self,matrix):
        def horizontal_stretches(self,matrix):
            horizontal_result = []
            for i in range(len(matrix)):
                start = 0
                while start < len(matrix[i]):
                    if matrix[i][start] == 1:
                        end = start
                        while end < len(matrix[i]) and matrix[i][end] == 1:
                            end += 1
                        if end - start > 1:  # At least 2 consecutive 1s
                            horizontal_result.append(((i, start), (i, end - 1)))
                        start = end
                    else:
                        start += 1
            return horizontal_result

        def vertical_stretches(self,matrix):
            vertical_result = []
            for j in range(len(matrix[0])):
                start = 0
                while start < len(matrix):
                    if matrix[start][j] == 1:
                        end = start
                        while end < len(matrix) and matrix[end][j] == 1:
                            end += 1
                        if end - start > 1:  # At least 2 consecutive 1s
                            vertical_result.append(((start, j), (end - 1, j)))
                        start = end
                    else:
                        start += 1
            return vertical_result

        horizontal_result = horizontal_stretches(self,matrix)
        vertical_result = vertical_stretches(self,matrix)
        
        return horizontal_result, vertical_result
        
        
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