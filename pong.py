#Juego de Ping Pong en python#
import turtle

#Ventana

wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Raqueta_1
raqueta_1 = turtle.Turtle()
raqueta_1.speed(0)
raqueta_1.shape("square")
raqueta_1.color("white")
raqueta_1.shapesize(stretch_wid=5, stretch_len=1)
raqueta_1.penup()
raqueta_1.goto(-350,0)

#Raqueta_2
raqueta_2 = turtle.Turtle()
raqueta_2.speed(0)
raqueta_2.shape("square")
raqueta_2.color("white")
raqueta_2.shapesize(stretch_wid=5, stretch_len=1)
raqueta_2.penup()
raqueta_2.goto(350,0)

#Pelota 
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
pelota.dx = .2
pelota.dy = .2

#Funciones de movimineto para las raquetas 
def raqueta_1_up():
    y = raqueta_1.ycor()
    y += 20
    raqueta_1.sety(y)

def raqueta_1_down():
    y = raqueta_1.ycor()
    y -=20
    raqueta_1.sety(y)

def raqueta_2_up():
    y = raqueta_2.ycor()
    y += 20
    raqueta_2.sety(y)

def raqueta_2_down():
    y = raqueta_2.ycor()
    y -=20
    raqueta_2.sety(y)

#Mapeo del tecaldo

wn.listen()
wn.onkeypress(raqueta_1_up, 'w')
wn.onkeypress(raqueta_1_down, 's')
wn.onkeypress(raqueta_2_up, 'Up')
wn.onkeypress(raqueta_2_down, 'Down')

#Main Game Loop
while True:
    wn.update()
    
    #Movimiento de la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    #Marco de la pantalla
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1

    if pelota.xcor() > 390:
        pelota.setx(390)
        pelota.dx *= -1

    if pelota.xcor() < -390:
        pelota.setx(-390)
        pelota.dx *= -1