from objects import Canvas, Snake
from time import sleep
import os

if __name__ == "__main__":
    canvas = Canvas(40, 60)
    snake = Snake(canvas)
    os.system("clear")

    for i in ["up", "up", "left", "left", "down", "down", "right", "right"]:
        snake(i)
        print(snake.tail_path)
        print(canvas)
        sleep(1)
        os.system("clear")
