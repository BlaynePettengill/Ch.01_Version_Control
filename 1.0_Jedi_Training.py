'''
1.0 Jedi Training (17pts)  Name:________________


1. Define Forking (1pt): 
forking is creating a copy of a public file onto your GitHub account
2. Define Cloning (1pt): 
cloning is copying a file from GitHub onto the computer
3. Define Branching (1pt):
branching is making a seprate copy of a branch making it so you can
test stuff out with out messing with the orignal branch
4. Define Committing (1pt): 
committing is making a hard save of your files that have been updated since your last commit
5. Define Merging (1pt): 
merging is combining
6. Define Pushing (1pt):

7. Define Pull Request (1pt):


8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle

tina = turtle.Turtle()
tony = turtle.Turtle()
screen=turtle.Screen()

tina.ht()
tony.ht()

tina.speed(20)
tony.speed(10)

tina.color('green')
tony.color('black')
screen.bgcolor('black')

tina.shape('turtle')
tony.shape('turtle')

tina.penup()
tina.goto(0,-75)
tony.pu()
tony.goto(200,200)
tony.pd()
tina.pendown()

#Green grass
tina.begin_fill()
tina.goto(200,-75)
tina.goto(200,-200)
tina.goto(-200,-200)
tina.goto(-200,-75)
tina.goto(0,-75)
tina.end_fill()

#blue sky
tina.color('sky blue')
tina.begin_fill()
tina.goto(200,-75)
tina.goto(200,200)
tina.goto(-200,200)
tina.goto(-200,-75)
tina.goto(0,-75)
tina.end_fill()

#brown building base
tina.color('brown')
tina.begin_fill()
tina.goto(125,-75)
tina.goto(125,100)
tina.goto(-50,100)
tina.goto(-50,-75)
tina.goto(50,-75)
tina.end_fill()

#triangle
tina.color('black')
tina.pu()
tina.goto(125,100)
tina.pd()
tina.begin_fill()
tina.goto(37.5,150)
tina.goto(-50,100)
tina.end_fill()

#Door
tina.pu()
tina.goto(-25,-75)
tina.pd()
tina.begin_fill()
tina.goto(25,-75)
tina.goto(25,25)
tina.goto(-25,25)
tina.goto(-25,-75)
tina.end_fill()
tina.goto(15,-25)
tina.dot(5,'white')

#Window
tina.pu()
tina.goto(50,0)
tina.pd()
tina.begin_fill()
tina.goto(50,50)
tina.goto(100,50)
tina.goto(100,0)
tina.goto(50,0)
tina.end_fill()
#Window pane 1
tina.color('white')
tina.pu()
tina.goto(55,5)
tina.pd()
tina.begin_fill()
tina.goto(55,22.5)
tina.goto(72.5,22.5)
tina.goto(72.5,5)
tina.goto(55,5)
tina.end_fill()
#Window pane 2
tina.pu()
tina.goto(77.5,5)
tina.pd()
tina.begin_fill()
tina.goto(77.5,22.5)
tina.goto(95,22.5)
tina.goto(95,5)
tina.goto(77.5,5)
tina.end_fill()
#Window pane 3
tina.pu()
tina.goto(77.5,27.5)
tina.pd()
tina.begin_fill()
tina.goto(77.5,45)
tina.goto(95,45)
tina.goto(95,27.5)
tina.goto(77.5,27.5)
tina.end_fill()
#Window pane 4
tina.pu()
tina.goto(55,27.5)
tina.pd()
tina.begin_fill()
tina.goto(55,45)
tina.goto(72.5,45)
tina.goto(72.5,27.5)
tina.goto(55,27.5)
tina.end_fill()
#sun
tina.pu()
tina.goto(-150,150)
tina.pd()
tina.dot(75,'yellow')
#Blackout



#signiture
tina.color('white')
tina.pu()
tina.goto(80,-195)

tina.write('Blayne Pettengill',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
