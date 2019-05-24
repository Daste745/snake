from math import floor
from typing import List, Tuple


class Canvas(object):
    def __init__(self, size_y: int, size_x: int):
        self.size_x = size_x
        self.size_y = size_y

        self.empty_x = []
        self.canvas = []

        for i in range(size_x):
            self.empty_x.append("#")

        for i in range(size_y):
            self.canvas.append(self.empty_x[:])

    def __str__(self):
        string = ""
        max_value_length = max(len(str(i)) for i in self.flatten())

        for row in self.canvas:
            for i in row:
                string += str(i) + " " * (max_value_length - len(str(i)) + 1)
            string += "\n"

        return f"Canvas, {self.size_x}x{self.size_y}:\n{string}"

    def __setitem__(self, key, value):
        self.canvas[key] = value

    def __getitem__(self, item):
        return self.canvas[item]

    def flatten(self) -> List:
        flattened_list = []
        for row in self.canvas:
            for i in row:
                flattened_list.append(i)

        return flattened_list

    def move_cell(self, origin_coordinates, target_coordinates):
        origin_symbol = self.canvas[origin_coordinates[0]][origin_coordinates[1]]
        self.canvas[target_coordinates[0]][target_coordinates[1]] = origin_symbol
        self.canvas[origin_coordinates[0]][origin_coordinates[1]] = "#"

    @property
    def center_coordinates(self):
        middle_row = floor(self.size_y / 2)
        middle_col = floor(self.size_x / 2)
        return middle_row, middle_col

    @property
    def center(self):
        return self.canvas[self.center_coordinates[0]][self.center_coordinates[1]]

    @center.setter
    def center(self, value):
        self.canvas[self.center_coordinates[0]][self.center_coordinates[1]] = value
