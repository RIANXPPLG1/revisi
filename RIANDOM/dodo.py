import turtle

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")

    # Membuat objek turtle
    flower = turtle.Turtle()
    flower.shape("turtle")
    flower.color("red")
    flower.speed(10)

    # Menggambar kelopak bunga
    for _ in range(36):
        flower.forward(100)
        flower.right(45)
        flower.forward(100)
        flower.right(135)
        flower.forward(100)
        flower.right(45)
        flower.forward(100)
        flower.right(170)

    # Menggambar tengah bunga
    flower.color("yellow")
    flower.right(90)
    flower.forward(200)

    window.exitonclick()

draw_flower()
