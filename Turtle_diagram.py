import turtle


def multicolor_squares(square, size):
    """
    Making a square with different colors .
    """
    for color in ["blue", "green", "purple", "black"]:
        square.color(color)
        square.forward(size)
        square.left(90)


window = turtle.Screen()
window.title("Turtle & Functions")
window.bgcolor("black")

tess = turtle.Turtle()
tess.speed(4)
tess.pensize(3)

size = 20
for i in range(15):
    multicolor_squares(tess, size)
    size += 10
    tess.forward(10)
    tess.right(90)


window.mainloop()
