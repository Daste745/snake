from . import Canvas
from collections import deque


class Snake(object):
    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self.length = 1
        self.tail_path = deque(["up" * (self.length + 1)])
        self.snake = [(self.canvas.center_coordinates[0] - 1, self.canvas.center_coordinates[1]),
                      (self.canvas.center_coordinates[0] + self.length, self.canvas.center_coordinates[1])]
        for j, i in enumerate(self.snake):
            self.canvas[i[0]][i[1]] = "^" if j == 0 else "$"
        self.canvas.center = "@"
        # Create a linked list, which consists of canvas coordinates
        # for i in range(length + 2):
        #     self.snake.append(canvas.center_coordinates)

    def __str__(self):
        string = "<-".join(str(i) for i in self.snake)
        return f"Snake, length: {self.length}:\n{string}"

    def __call__(self, direction: str):
        head, tail = self.snake
        self.tail_path.append(direction)
        tail_move_direction = self.tail_path.popleft()

        # Move head and body
        if direction == "up":
            if self.canvas[head[0] - 1][head[1]] in ["@", "$"]:
                exit("died!")

            self.canvas.move_cell(head, (head[0] - 1, head[1]))
            self.canvas[head[0]][head[1]] = "@"
            self.snake[0] = (head[0] - 1, head[1])

        elif direction == "down":
            if self.canvas[head[0] + 1][head[1]] in ["@", "$"]:
                exit("died!")

            self.canvas.move_cell(head, (head[0] + 1, head[1]))
            self.canvas[head[0]][head[1]] = "@"
            self.snake[0] = (head[0] + 1, head[1])

        elif direction == "left":
            if self.canvas[head[0]][head[1] - 1] in ["@", "$"]:
                exit("died!")

            self.canvas.move_cell(head, (head[0], head[1] - 1))
            self.canvas[head[0]][head[1]] = "@"
            self.snake[0] = (head[0], head[1] - 1)

        elif direction == "right":
            if self.canvas[head[0]][head[1] + 1] in ["@", "$"]:
                exit("died!")

            self.canvas.move_cell(head, (head[0], head[1] + 1))
            self.canvas[head[0]][head[1]] = "@"
            self.snake[0] = (head[0], head[1] + 1)

        # Move tail
        if tail_move_direction == "up":
            self.canvas.move_cell(tail, (tail[0] - 1, tail[1]))
            self.snake[1] = (tail[0] - 1, tail[1])

        elif tail_move_direction == "down":
            self.canvas.move_cell(tail, (tail[0] + 1, tail[1]))
            self.snake[1] = (tail[0] + 1, tail[1])

        elif tail_move_direction == "left":
            self.canvas.move_cell(tail, (tail[0], tail[1] - 1))
            self.snake[1] = (tail[0], tail[1] - 1)

        elif tail_move_direction == "right":
            self.canvas.move_cell(tail, (tail[0], tail[1] + 1))
            self.snake[1] = (tail[0], tail[1] + 1)
