import turtle
import tkinter as tk
import math

def draw_sunflower():
    # Limpiar la pantalla y dibujar el girasol
    turtle.clear()
    turtle.title("Girasol")
    turtle.bgcolor('black')

    turtle.fillcolor('green')
    turtle.begin_fill()
    turtle.pencolor('black')
    turtle.forward(7)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.end_fill()

    turtle.speed(0)
    turtle.fillcolor('brown')
    s = 137.508 * (math.pi / 180.0)
    for i in range(160 + 40):
        r = 4 * math.sqrt(i)
        f = i * s
        o = r * math.cos(f)
        p = r * math.sin(f)
        turtle.penup()
        turtle.goto(o, p)
        turtle.setheading(i * 137.508)
        turtle.pendown()
        if i < 160:
            turtle.stamp()
        else:
            turtle.fillcolor('yellow')
            turtle.begin_fill()
            turtle.right(20)
            turtle.forward(46)
            turtle.left(40)
            turtle.forward(70)
            turtle.left(140)
            turtle.forward(70)
            turtle.left(40)
            turtle.forward(70)
            turtle.end_fill()
    turtle.hideturtle()

# Configurar la ventana principal
root = tk.Tk()
root.title("Propuesta")

# Crear el lienzo de Turtle
canvas = turtle.ScrolledCanvas(root)
canvas.pack(fill=tk.BOTH, expand=tk.YES)

# Configurar Turtle
screen = turtle.TurtleScreen(canvas)
screen.bgcolor('black')

# Crear una tortuga para el mensaje
message_turtle = turtle.RawTurtle(screen)
message_turtle.hideturtle()
message_turtle.penup()
message_turtle.color('white')
message_turtle.goto(0, 50)
message_turtle.write("¿Quieres ser mi novia?", align="center", font=("Arial", 24, "bold"))

# Crear el botón
button = tk.Button(root, text="Sí", command=draw_sunflower)
button.pack()

root.mainloop()
