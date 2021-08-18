import turtle 

turtle.bgcolor('black')

turtle.color("black")     

turtle.pensize(3) 

turtle.speed(180)


for colores in ("blue", "blue4", "firebrick4", "firebrick", "BlueViolet", "DarkOrchid4", "AliceBlue"):

   for x in range(30):
    turtle.speed(180)
    turtle.color(colores)
    turtle.circle(100)
    turtle.left(10)

