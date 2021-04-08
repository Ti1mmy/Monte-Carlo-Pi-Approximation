# Area = pi * r**2
# Draw circle with radius 1, and randomly plot points inside 1 quadrant
# Highlight all dots with distance < 1 from (0,0)


import arcadeplus as arcade
import random
import math

WIDTH = 800
HEIGHT = 800
circle_points = []
outside_points = [[WIDTH, HEIGHT]]
window = arcade.open_window(WIDTH, HEIGHT, "Monte Carlo Pi Approximation")


def setup():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)
    arcade.run()

@window.event
def update(delta_time):
    global pi
    for i in range(200):
        points = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
        if math.sqrt(points[0]**2 + points[1]**2) <= WIDTH:
            circle_points.append(points)
        else:
            outside_points.append(points)
    pi = 4*(len(circle_points)/(len(outside_points) + len(circle_points)))

@window.event
def on_draw():
    arcade.start_render()
    arcade.draw_points(outside_points, (0, 0, 0), 2)
    arcade.draw_points(circle_points, (255, 0, 0), 2)
    arcade.draw_rectangle_filled(0, 0, 300, 40, arcade.color.WHITE)
    arcade.draw_text(f'pi={pi}', 0, 0, arcade.color.BLACK)


if __name__ == '__main__':
    setup()