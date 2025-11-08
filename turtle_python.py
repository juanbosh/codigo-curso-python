import turtle
import time
import random

# --- 1. Configuración Inicial ---
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Serpiente Retro Artística")
screen.tracer(0) # Desactiva la actualización automática (para controlar el ritmo)

t = turtle.Turtle()
t.shape("square")
t.color("white")
t.speed(0)
t.penup()
t.goto(0, 0)
t.direction = "stop"
t.pensize(3)

# Lista para almacenar coordenadas visitadas (el cuerpo de la serpiente)
segmentos = []
colores_retro = ["#00FF00", "#FF00FF", "#FFFF00", "#00FFFF"] # Colores de videojuegos retro

# --- 2. Funciones de Control de Teclado ---
def ir_arriba():
    if t.direction != "down":
        t.direction = "up"
def ir_abajo():
    if t.direction != "up":
        t.direction = "down"
def ir_izquierda():
    if t.direction != "right":
        t.direction = "left"
def ir_derecha():
    if t.direction != "left":
        t.direction = "right"

# Mapear teclas
screen.listen()
screen.onkey(ir_arriba, "Up")
screen.onkey(ir_abajo, "Down")
screen.onkey(ir_izquierda, "Left")
screen.onkey(ir_derecha, "Right")

# --- 3. Función de Movimiento y Colisión ---
def mover_serpiente():
    
    # 3.1. Movimiento básico
    if t.direction == "up":
        t.sety(t.ycor() + 20)
    if t.direction == "down":
        t.sety(t.ycor() - 20)
    if t.direction == "left":
        t.setx(t.xcor() - 20)
    if t.direction == "right":
        t.setx(t.xcor() + 20)
        
    # 3.2. Detección de Colisión (Nostalgia)
    # Si la cabeza se acerca a alguna coordenada ya dibujada
    cabeza_pos = (round(t.xcor()), round(t.ycor()))
    if cabeza_pos in segmentos[:-1]: # Ignoramos la posición actual
        
        # Efecto "Game Over"
        t.color("red")
        t.write("¡COLISIÓN! Reiniciando...", align="center", font=("Courier", 24, "bold"))
        time.sleep(1.5)
        
        # Reiniciar para dibujar de nuevo
        t.clear()
        segmentos.clear()
        t.direction = "stop"
        t.goto(0, 0)
        t.pencolor("white")
        t.pensize(3)
        t.clear() # Limpiar el texto de colisión
        t.color("white")

    # 3.3. Dibujar el Rastro y Cambiar Color
    if t.direction != "stop":
        # Almacena la nueva posición (usando un tamaño de paso de 20)
        segmentos.append(cabeza_pos)
        
        # Para el rastro
        t.pencolor(random.choice(colores_retro))
        t.pendown()
        t.goto(t.xcor(), t.ycor()) # Redibuja para dejar el color
        t.penup()

# --- 4. Bucle Principal de Animación ---
while True:
    screen.update()
    mover_serpiente()
    time.sleep(0.15) # Controla la velocidad de la serpiente (ritmo del juego)

# screen.mainloop() # Esta línea nunca se alcanza en este diseño de bucle