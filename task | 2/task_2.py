import turtle


def draw_pythagoras_fractal_tree(turtle, size, order):
    angle = 45
    if order == 0:
        return
    else:
        turtle.forward(size)
        turtle.right(angle)

        draw_pythagoras_fractal_tree(turtle, size * 0.7, order - 1)
        turtle.left(2 * angle)

        draw_pythagoras_fractal_tree(turtle, size * 0.7, order - 1)
        turtle.right(angle)
        turtle.backward(size)


def drawing(order):
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.pendown()
    draw_pythagoras_fractal_tree(t, size=100, order=order)
    turtle.exitonclick()


def main():
    while True:
        try:
            fractal = int(input("Enter Pythagoras fractal: "))
            break
        except ValueError:
            print("Incorrect input")
    drawing(order=fractal)


if __name__ == "__main__":
    main()