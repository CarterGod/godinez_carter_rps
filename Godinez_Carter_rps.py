# This file was created by: Carter Godinez

'''
Goals:
Create a working rock, paper, scissors game that visually displays results

'''

# import package
import turtle
from turtle import *

from random import randint
# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

# setup the width and height for rock
rock_w, rock_h = 256, 280

# setup the width and height for paper
paper_w, paper_h = 256, 204

# setup the width and height for scissors
scissors_w, scissors_h = 256, 170

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)


# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
# setup the paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')
# instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()
# setup the scissors image using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
# instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()


def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

def show_paper(x,y):
    # add the paper image as a shape
    screen.addshape(paper_image)
    # attach the paper_image to the paper_instance
    paper_instance.shape(paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()
    # set the position of the paper_instance
    paper_instance.setpos(x,y)

def show_scissors(x,y):
    # add the scissors image as a shape
    screen.addshape(scissors_image)
    # attach the scissors_image to the scissors_instance
    scissors_instance.shape(scissors_image)
    # remove the pen option from the scissors_instance so it doesn't draw lines when moved
    scissors_instance.penup()
    # set the position of the scissors_instance
    scissors_instance.setpos(x,y)

# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()
text.penup() 

# bring up options visually on screen
show_rock(-300, 0)
show_paper(0, 0)
show_scissors(300, 0)

# set up text telling player to select choice
text.setpos(0,150)
text.write("Choose rock or paper or scissors", False, "left", ("Arial", 24, "normal"))

# this function uses and x y value, an obj, and width and height 
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False


# define where the player clicks and generates a result
def mouse_pos(x, y):
    # define when player picks rock
    if collide(x,y,rock_instance, rock_w, rock_h):
        text.clear()
        text.write("you chose rock!!!", False, "left", ("Arial", 24, "normal"))
        # have computer randomly select a choice
        def computer_choice():
            choice = randint(0,2)
            # define what happens when computer selects rock
            if choice == 0:
                show_rock(-300,0)
                text.clear()
                # remove non selected items from screen
                paper_instance.hideturtle()
                scissors_instance.hideturtle()
                # print computer choice
                text.write("computer chose rock!!!", False, "left", ("Arial", 24, "normal"))
                text.setpos(0,-150)
                # print outcome
                text.write("it is a tie", False, "right", ("Arial", 24, "normal"))
            elif choice == 1:
                # define what happens when computer selects paper
                show_paper(0,0)
                text.clear()
                # remove non selected item from screen
                scissors_instance.hideturtle()
                # print computer choice
                text.write("computer chose paper!!!", False, "left", ("Arial", 24, "normal"))
                text.setpos(0,-150)
                # print outcome
                text.write("you lose", False, "right", ("Arial", 24, "normal"))
            elif choice == 2:
                # define what happens when computer selects scissors
                show_scissors(300,0)
                text.clear()
                # remove non selected item from screen
                paper_instance.hideturtle()
                # print computer choice
                text.write("computer chose scissors!!!", False, "left", ("Arial", 24, "normal"))
                text.setpos(0,-150)
                # print outcome
                text.write("you win", False, "right", ("Arial", 24, "normal"))
        computer_choice()
    # define when player picks paper
    elif collide(x,y,paper_instance, paper_w, paper_h):
        text.clear()
        text.write("you chose paper!!!", False, "left", ("Arial", 24, "normal"))
        # have computer randomly select a choice
        def computer_choice():
            choice = randint(0,2)
             # define what happens when computer selects rock
            if choice == 0:
                show_rock(-300,0)
                text.clear()
                # remove non selected item from screen
                scissors_instance.hideturtle()
                # print computer choice
                text.write("computer chose rock!!!", False, "left", ("Arial", 24, "normal"))
                text.setpos(0,-150)
                # print outcome
                text.write("you win", False, "right", ("Arial", 24, "normal"))
            # define what happens when computer selects paper
            elif choice == 1:
                show_paper(0,0)
                text.clear()
                # remove non selected items from screen
                rock_instance.hideturtle()
                scissors_instance.hideturtle()
                # print computer choice
                text.write("computer chose paper!!!", False, "left", ("Arial", 24, "normal"))
                text.setpos(0,-150)
                # print outcome
                text.write("it is a tie", False, "right", ("Arial", 24, "normal"))
            # define what happens when computer selects scissors
            elif choice == 2:
                show_scissors(300,0)
                text.clear()
                # remove non selected item from screen
                rock_instance.hideturtle()
                # print computer choice
                text.write("computer chose scissors!!!", False, "left", ("Arial", 24, "normal"))
                text.setpos(0,-150)
                # print outcome
                text.write("you lose", False, "right", ("Arial", 24, "normal"))
        computer_choice()
    # define when player selects scissors
    elif collide(x,y,scissors_instance, scissors_w, scissors_h):
        text.clear()
        text.write("you chose scissors!!!", False, "left", ("Arial", 24, "normal"))
        # have computer randomly select a choice
        def computer_choice():
            choice = randint(0,2)
            # define what happens when computer selects rock
            if choice == 0:
                show_rock(-300,0)
                text.clear()
                # remove non selected item from screen
                paper_instance.hideturtle()
                # print computer choice
                text.write("computer chose rock!!!", False, "left", ("Arial", 24, "normal"))
                text.setpos(0,-150)
                # print outcome
                text.write("you lose", False, "right", ("Arial", 24, "normal"))
            # define what happens when computer selects rock
            elif choice == 1:
                show_paper(0,0)
                text.clear()
                # remove non selected item from screen
                rock_instance.hideturtle()
                # print computer choice
                text.write("computer chose paper!!!", False, "left", ("Arial", 24, "normal"))
                text.setpos(0,-150)
                # print outcome
                text.write("you win", False, "right", ("Arial", 24, "normal"))
            # define what happens when computer selects scissors
            elif choice == 2:
                show_scissors(300,0)
                text.clear()
                # remove non selected items from screens
                rock_instance.hideturtle()
                paper_instance.hideturtle()
                # print computer choice
                text.write("computer chose scissors!!!", False, "left", ("Arial", 24, "normal"))
                text.setpos(0,-150)
                # print outcome
                text.write("it is a tie", False, "right", ("Arial", 24, "normal"))
        computer_choice()
    # tell player when they click outside of any hit box
    else:
        text.setpos(0,-150)
        text.write("Select a valid option", False, "left", ("Arial", 24, "normal"))



# user this to get mouse position
screen.onclick(mouse_pos)

# runs mainloop for Turtle - required to be last
screen.mainloop()