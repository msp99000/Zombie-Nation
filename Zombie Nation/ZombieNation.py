'''
     *****************************
     * Z O M B I E   N A T I O N *
     *****************************
     ******* DOCUMENTATION *******
     *****************************

     ZOMBIE NATION 🧟 is an interactive GUI game built on top of Python's Turtle module.
     Developer: 'STUDENT NAME'
     Reviewer: 'REVIEWER NAME'

     The game consists of two characters:
     1. Bob the turtle
     2. Zombini the zombie 🧟

     "Bob" the turtle out of nowhere enters the 'ZOMBIE NATION', unfortunately! to eventually lead to nothing besides
      a whole new level of intimidation. "Bob" encounters "Zombini" who's been starving since long.
      All he can think right now is run-for-his-life. "Bob" learns quickly that "Zombini" is weak and might not be
      able to carry the chase for longer than ~ 30 secs. "Bob" somehow needs to survive for at least 30 secs to save his life.

      ******************
      **** CONTROLS ****
      ******************

      In this game, the player will be controlling the turtle with the help of arrow keys.
      The player is recommended to stay as far as possible from the zombie.
      The player needs to avoid collision with the zombie. If the zombie somehow succeeds in hitting the same co-ordinates as the players recent position, the player loses the game.
      The speed of zombie increases every 10 secs. The zombie will be fastest in his last cycle.
      To win this game, the player will need to avoid zombie collision for at least 30 secs.
      Scores are calculate on the basis of time.
      If the score goes past 50, the player wins.

      Last modification date: 08/03/2021
'''


'''
    To begin with, I have imported few libraries which include time, turtle and random.
    time library will provide time methods which will help control out game.
    turtle module provides all basic methods which help in building and interacting with the GUI
    random is used generating random numbers
'''

import time
from turtle import *
from random import randint

'''
   Here I generated a screen to work with.
   Defined some basic variables to get started with:
   1. Bob
   2. Zombini
   3. Boundary (To create a boundary or end points)
   4. 'new_score' reads the updated score on top left side of screen
   5. 'total_time' reads the updated time on top left side of the screen 
   6. 'img' and 'img2' stores a list of images to be used for GUI
'''

screen = Screen()
screen.colormode(255)

bob = Turtle()
bob.hideturtle()

zomboni = Turtle()
zomboni.hideturtle()

boundary = Turtle(visible=False)

new_score = Turtle(visible=False)

total_time = Turtle(visible=False)

img = ['0.1.gif','0.2.gif','0.3.gif','0.gif','10.gif','11.gif','12.gif','13.gif','14.gif',
       '15.gif','16.gif','17.gif','18.gif','19.gif','20.gif','21.gif','22.gif',
       '23.gif','24.gif','25.gif','26.gif']

img2 = ['winner/0.gif','winner/1.gif','winner/2.gif','winner/3.gif','winner/4.gif','winner/5.gif',
        'winner/6.gif','winner/7.gif','winner/8.gif','winner/9.gif','winner/10.gif','winner/11.gif',
        'winner/12.gif','winner/13.gif','winner/14.gif','winner/15.gif','winner/16.gif','winner/17.gif',
        'winner/18.gif','winner/19.gif','winner/20.gif','winner/21.gif','winner/22.gif','winner/23.gif',
        'winner/24.gif','winner/25.gif','winner/26.gif','winner/27.gif','winner/28.gif','winner/29.gif',
        'winner/30.gif','winner/31.gif','winner/32.gif','winner/33.gif','winner/34.gif','winner/35.gif',
        'winner/36.gif']

for x in range(21):
    screen.addshape(img[x])

for x in range(37):
    screen.addshape(img2[x])

'''
    'welcome_screen()' contains a setup for an introductory screen which appears at the beginning of the game.
'''
def welcome_screen():
    screen.setup(900,650)
    screen.title("Z O M B I E   N A T I O N")
    for x in range(21):
        screen.update()
        screen.bgpic(img[x])
        time.sleep(0.1)
    time.sleep(0.5)
    screen.clear()

# Displaying the welcome screen
welcome_screen()

'''
    'arena_create()' contains code for creation of a player field. This sets up screen after the welcome screen.
    This function adds images to GUI and characters we aim to use in this game.
'''
def arena_create():
    screen.update()
    bob.showturtle()
    zomboni.showturtle()
    screen.title("Z O M B I E   N A T I O N")
    imbob = 'turtle.gif'
    imzomboni = 'zombie.gif'
    screen.setup(650, 650)
    screen.register_shape(imbob)
    screen.register_shape(imzomboni)
    screen.addshape('a.gif')
    screen.addshape('b.gif')
    screen.addshape('c.gif')
    screen.addshape('d.gif')
    zomboni.speed(0)
    zomboni.penup()
    zomboni.shape(imzomboni)
    zomboni.setpos(280, 280)
    zomboni.speed(1)
    bob.speed(0)
    bob.penup()
    bob.shape(imbob)

'''
    'arena_draw_boundary()' draws a boundary line at the screen endpoints. This boundary line helps us decide
    functions of the turtle and other functions in the game itself.
'''
def arena_draw_boundary():
    boundary.pensize(3)
    boundary.penup()
    boundary.speed(0)
    boundary.goto(-325, -325)
    boundary.pendown()
    for x in range(4):
        boundary.fd(650)
        boundary.lt(90)

'''
    'timer()' fetches the value of time elapsed which shows us the real time value on the screen.
    It takes 'x' as a positional argument which is the value of time elapsed.
'''
def timer(z):
    total_time.penup()
    total_time.speed(0)
    total_time.setpos(-310, 300)
    total_time.clear()
    total_time.write("TIME: {0}s".format(int(time.time() - z)), font=('candara', 10))
    return int(time.time()-z)

'''
    'score()' similarly fetches real time score updates. It takes two parameters 'x' and 'z'.
    'x' is the value of time elapsed while 'z' here is the time of beginning of the game.
'''
def score(x, z):
    new_score.penup()
    new_score.speed(0)
    new_score.setpos(-200, 300)
    new_score.clear()
    new_score.write("SCORE: {0}".format(1.75 * x), font=('candara', 10))
    return 1.75 * int(time.time()-z)

'''
    Below I defined four different functions which help move the turtle.
    1. 'go_forward()' sends the turtle forward by 50 px
    2. 'go_backward()' sends the turtle backward by 50 px
    3. 'go_up()' sends the turtle upwards bu 50 px
    4. 'go_down()' sends the turtle downwards by 50 px
'''
def go_forward():
	bob.setheading(0)
	bob.fd(50)

def go_backward():
	bob.setheading(0)
	bob.bk(50)

def go_up():
	bob.setheading(0)
	bob.lt(90)
	bob.fd(50)

def go_down():
	bob.setheading(0)
	bob.rt(90)
	bob.fd(50)

'''
    'bind_keyboard()' assigns hardware keys to control components in the game.
    Here, I'm assigning arrow keys to control the turtle.
'''
def bind_keyboard():
	onkey(go_up, "Up")
	onkey(go_down, "Down")
	onkey(go_forward, "Right")
	onkey(go_backward, "Left")

'''
   'is_collision()' returns a boolean value. This function tells the program if the collision between the turtle and zombie has taken place or not.
'''
def is_collision():
    if bob.distance(zomboni) < 70:
        return True
    else:
        False

'''
    'bounce_off_boundary()' controls the actions of the turtle if the turtle hits one of the boundary
'''
def bounce_off_boundary():
    if bob.xcor() >= 300:
        bob.setposition(-300, bob.ycor())
        bob.fd(10)

    if bob.xcor() <= -300:
        bob.setposition(300, bob.ycor())
        bob.bk(10)

    if bob.ycor() >= 300:
        bob.setposition(bob.xcor(), -300)
        bob.setheading(0)
        bob.lt(90)
        bob.fd(10)

    if bob.ycor() <= -300:
        bob.setposition(bob.xcor(), 300)
        bob.setheading(0)
        bob.rt(90)
        bob.fd(10)

'''
    'gameOver()' controls the actions after the collision of the turtle with the zombie has taken place.
    This function adds a soft animation when the collision takes place and the player loses the game.
'''
def gameOver():
    bob.hideturtle()
    for x in range(3):
        zomboni.shape('a.gif')
        time.sleep(0.1)
        zomboni.shape('b.gif')
        time.sleep(0.1)
        zomboni.shape('c.gif')
        time.sleep(0.1)
        zomboni.shape('d.gif')
        time.sleep(0.1)
    zomboni.hideturtle()
    clearscreen()
    screen.addshape('gameover.gif')
    gameover = Turtle(visible=False)
    gameover.color('green')
    gameover.penup()
    gameover.speed(0)
    gameover.setpos(-220, 180)
    screen.colormode(255)
    gameover.color(216, 226, 220)
    gameover.speed(1)
    im = ['brain3.gif', 'brain4.gif', 'brain5.gif',
          'brain6.gif', 'brain7.gif', 'brain8.gif']
    for x in range(6):
        screen.addshape(im[x])
    br = Turtle()
    br.penup()
    br.speed(0)
    br.setpos(-80, 260)
    for x in range(6):
        br.shape(im[x])
        time.sleep(0.1)
    br.hideturtle()
    gameover.write("THE ZOMBIE ATE YOUR BRAIN !", font=('candara', 20, 'bold'))
    time.sleep(0.5)
    screen.bgpic('gameover.gif')
    screen.mainloop()

'''
    'you_win()' controls the actions after the player has won the game viz survived 30 secs in the game.
    This function adds a soft animation at the ending of the game.
'''
def you_win():
    time.sleep(0.5)
    zomboni.shape('a.gif')
    time.sleep(0.1)
    zomboni.shape('b.gif')
    time.sleep(0.1)
    zomboni.shape('c.gif')
    time.sleep(0.1)
    zomboni.shape('d.gif')
    time.sleep(0.1)
    zomboni.hideturtle()
    screen.clear()
    for x in range(37):
        screen.update()
        screen.bgpic(img2[x])
        time.sleep(0.1)
    screen.mainloop()

'''
    'play()' function makes use of all the above defined functions in a manner which helps runs the GUI and enalbles the player to play the game.
'''
def play():
    start = time.time()
    arena_create()
    arena_draw_boundary()
    bind_keyboard()
    screen.listen()
    while True:
        screen.update()
        timer(start)
        score(timer(start), start)
        bounce_off_boundary()
        zomboni.goto(bob.pos())
        screen.tracer()
        sc = score(timer(start), start)
        if timer(start) >= 10:
            zomboni.speed(1.3)
        if timer(start) >= 20:
            zomboni.speed(1.5)
        if timer(start) >= 30:
            zomboni.speed(1.7)
        if sc > 50:
            you_win()
            break
        if is_collision():
            gameOver()
            break

play()
