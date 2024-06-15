from enum import Enum
import tkinter as tk
from threading import Thread
import math
import numpy as np
from itertools import combinations
import itertools


# SPACING BETWEEN PUMPS ON WALL
SPACING_OF_PUMPS = 3

class Cell(Enum):
    WALL = 1
    WINDOW = 2
    DOOR = 3
    LIVING_ROOM = 4
    KITCHEN = 4
    BATHROOM = 4
    BEDROOM = 4
    OTHER = 4
    HEAT = 5


class MapHandler():

    def __init__(self):
        self.map = self.create_test_map()
        self.heatmap = self.create_test_heatmap()
        self.handle_maps()


        self.display = True
        if(self.display): 
            self.thread = Thread(target=self.display_map)
            self.thread.start()

        
        
        
        


    def handle_maps(self):
        
        boundaries = self.find_room_boundaries(self.map)
        print(f"boundaries: {boundaries}")

        for room in boundaries:
            possible_pump_positions = self.find_pump_positions(room)
            print("pumps: ", possible_pump_positions)
            for p in possible_pump_positions:
                self.map[p[1]][p[0]] = Cell.HEAT.value
    

        print(boundaries)

        
        """possible_pump_positions = self.find_pump_positions(lengths)
        print(possible_pump_positions)

        for position in possible_pump_positions:
            self.map[position[1]][position[0]] = Cell.HEAT.value

        
        instances = self.permute_heatmaps(possible_pump_positions)
        print(len(instances))"""

        

        return self.map, self.heatmap
    


    def permute_heatmaps(self, possible_pump_positions):
        all_combinations = []
        list_length = len(possible_pump_positions)
        
        # Generate combinations of all possible lengths
        for r in range(1, list_length + 1):
            all_combinations.extend(list(combinations(possible_pump_positions, r)))
        
        return all_combinations
    
    def find_pump_positions(self, boundaries):
            
            print(boundaries)
            

            positions = []  # Initialize an empty list to store the positions
            coordinates = []

            start_x = boundaries[0][0]
            start_y = boundaries[0][1]
            end_x = boundaries[1][0]
            end_y = boundaries[1][1]

            x_change = end_x - start_x
            y_change = end_y - start_y

            x_intervals = int(x_change // SPACING_OF_PUMPS) + 2
            y_intervals = int(y_change // SPACING_OF_PUMPS) + 2
            
            lengths = [x_change+1, y_change+1]

            print("lengths: ",lengths)

            positions_x = np.linspace(start_x, end_x, x_intervals)[1:-1]
            positions_x_start = [(math.floor(x), start_y) for x in positions_x]
            positions_x_end = [(math.floor(x), end_y) for x in positions_x]
            positions_y = np.linspace(start_y, end_y, y_intervals)[1:-1]
            positions_y_start = [(start_x, math.floor(y)) for y in positions_y]
            positions_y_end = [(end_x, math.floor(y)) for y in positions_y]



            print("positions x: ", positions_x)
            print("positions y: ", positions_y)

            vals = [positions_x_start, positions_x_end, positions_y_start, positions_y_end]
            vals = list(itertools.chain(*vals))

            print(f"vals: {vals}")

            return vals
    

    
            x = 0
            l = []


            for l in lengths[x]:
                # Calculate the length of the current interval
                start = l[0][not x]
                end = l[1][not x]
                length = end - start

                # Calculate the number of intervals that can fit within the length
                n_intervals = int(length // SPACING_OF_PUMPS)

                positions = np.linspace(start, end, n_intervals + 2)
                positions = positions[1:-1]

                
                print(len(positions))

                for pos in positions:
                    coord = [l[0][0], l[0][1]]
                    coord[not x] = math.floor(pos)
                    coordinates.append(tuple(coord))

            return coordinates


    def find_room_boundaries(self, matrix):
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        visited = [[False] * cols for _ in range(rows)]
        boundaries = []

        def dfs(row, col):
            min_row, max_row, min_col, max_col = row, row, col, col
            stack = [(row, col)]
            while stack:
                r, c = stack.pop()
                visited[r][c] = True
                # Check adjacent cells (up, down, left, right)
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                        if matrix[nr][nc] == 4:
                            stack.append((nr, nc))
                            visited[nr][nc] = True
                            min_row = min(min_row, nr)
                            max_row = max(max_row, nr)
                            min_col = min(min_col, nc)
                            max_col = max(max_col, nc)
            boundaries.append([(min_col, min_row), (max_col, max_row)])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 4 and not visited[i][j]:
                    dfs(i, j)

        return boundaries


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
                            horizontal_result.append(((i, start), (i, end - 1), (0, end-start-1)))
                        start = end
                    else:
                        start += 1

                # find the midpoints of each of these pairs

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
                            vertical_result.append(((start, j), (end - 1, j), (end-start-1, 0)))
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
            Cell.OTHER.value: 'gray',
            Cell.HEAT.value: "pink"
        }
        return color_map.get(cell, 'white')

m = MapHandler()