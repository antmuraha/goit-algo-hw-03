from turtle import Turtle
import turtle as t


def koch_curve(inst: Turtle, order, size):
    if order == 0:
        inst.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(inst, order - 1, size / 3)
            inst.left(angle)


def draw_snowflake(order, size=300):
    window = t.Screen()
    window.bgcolor("white")

    inst = t.Turtle()
    inst.speed(0)
    inst.penup()
    inst.goto(-size / 2, size / 2)
    inst.pendown()

    for angle in [0, -120, -120]:
        inst.left(angle)
        koch_curve(inst, order, size)

    window.mainloop()


if __name__ == "__main__":
    default = 3
    order = input(
        f"Please input Koch snowflake order (default {default}):")
    try:
        order = int(order)
        if order < 0:
            order = default
    except:
        order = default

    draw_snowflake(order)
