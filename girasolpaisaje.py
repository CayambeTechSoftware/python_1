from turtle import RawTurtle, TurtleScreen
import tkinter as tk
import math
import random

# Crear la ventana principal de tkinter
root = tk.Tk()
root.title("Paisaje con Turtle")

# Configurar el tamaño de la ventana
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Crear un canvas de tkinter
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack(fill="both", expand=True)

# Crear el canvas de turtle sobre el canvas de tkinter
turtle_screen = TurtleScreen(canvas)

# Crear una tortuga para dibujar el paisaje
t = RawTurtle(turtle_screen)
t.speed(5)  # Ajustar la velocidad de la tortuga

# Función para dibujar el cielo
def draw_sky():
    t.penup()
    t.goto(-window_width // 2, window_height // 2)
    t.pendown()
    t.color('skyblue')
    t.begin_fill()
    for _ in range(2):
        t.forward(window_width)
        t.right(90)
        t.forward(window_height // 2)
        t.right(90)
    t.end_fill()

# Función para dibujar el suelo
def draw_ground():
    t.penup()
    t.goto(-window_width // 2, -window_height // 250)
    t.pendown()
    t.color('lightgreen')  # Color de césped claro
    t.begin_fill()
    for _ in range(2):
        t.forward(window_width)
        t.right(90)
        t.forward(window_height // 2)
        t.right(90)
    t.end_fill()

# Función para dibujar un girasol pequeño
def draw_small_sunflower(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Tallo del girasol
    t.color('green')
    t.pensize(2)
    t.goto(x, y - 30)
    
    # Flor del girasol
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor('yellow')
    t.begin_fill()
    t.circle(10)  # Cabeza del girasol
    t.end_fill()

    # Semillas
    t.penup()
    t.goto(x, y + 5)
    t.pendown()
    t.fillcolor('brown')
    t.begin_fill()
    t.circle(5)  # Semilla
    t.end_fill()

# Dibujar el cielo
draw_sky()

# Dibujar el suelo (pasto) con textura
draw_ground()

# Dibujar algunos pequeños girasoles en el suelo
for _ in range(50):  # Puedes ajustar la cantidad de girasoles
    x = random.randint(-window_width // 2 + 10, window_width // 2 - 10)
    y = random.randint(-window_height // 2 + 10, -50)
    draw_small_sunflower(x, y)

# Dibujar un sol
t.penup()
t.goto(-200, 150)
t.pendown()
t.color('yellow')
t.begin_fill()
t.circle(50)
t.end_fill()

# Dibujar algunas nubes
def draw_cloud(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('white')
    t.begin_fill()
    for _ in range(6):
        t.circle(20)
        t.right(60)
    t.end_fill()

draw_cloud(-300, 200)
draw_cloud(-250, 250)
draw_cloud(-200, 200)

# Dibujar el girasol en el paisaje
t.penup()
t.goto(0, -50)
t.pendown()

# Dibujar el tallo del girasol
t.fillcolor('green')
t.begin_fill()
t.pencolor('black')
t.forward(7)
t.right(90)
t.forward(300)
t.right(90)
t.forward(15)
t.right(90)
t.forward(300)
t.right(90)
t.end_fill()

# Dibujar el girasol
t.fillcolor('brown')
s = 137.508 * (math.pi / 180.0)
for i in range(160 + 40):
    r = 4 * math.sqrt(i)
    f = i * s
    o = r * math.cos(f)
    p = r * math.sin(f)
    t.penup()
    t.goto(o, p)
    t.setheading(i * 137.508)
    t.pendown()
    if i < 160:
        t.stamp()
    else:
        t.fillcolor('yellow')
        t.begin_fill()
        t.right(20)
        t.forward(46)
        t.left(40)
        t.forward(70)
        t.left(140)
        t.forward(70)
        t.left(40)
        t.forward(70)
        t.end_fill()
        t.hideturtle()

# Iniciar el bucle principal de tkinter
root.mainloop()
