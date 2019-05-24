from objects import Canvas, Snake
from pynput.keyboard import Listener, Key
import os

canvas = Canvas(40, 60)
snake = Snake(canvas, length=15)


def game_tick():
    os.system("clear")
    # print(snake.action_queue)
    if snake.action_queue:
        snake.make_iteration()
    print(canvas)


def on_keypress(key: Key):
    if key.name in ["up", "down", "left", "right"]:
        snake.queue_action(key.name)
        game_tick()


if __name__ == "__main__":
    os.system("clear")

    with Listener(on_press=on_keypress) as listener:
        listener.join()
