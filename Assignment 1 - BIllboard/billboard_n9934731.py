
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9934731
#    Student name: Kevin Duong
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  BILLBOARD
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "paste_up".
#  You are required to complete this function so that when the
#  program is run it produces an image of an advertising billboard
#  whose arrangement is determined by data stored in a list which
#  specifies how individual paper sheets are to be pasted onto the
#  backing.  See the instruction sheet accompanying this file for
#  full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

sheet_width = 200 # pixels
sheet_height = 500 # pixels
backing_margin = 20 # pixels
backing_width = sheet_width * 4 + backing_margin * 2
backing_height = sheet_height + backing_margin * 2
canvas_top_and_bottom_border = 150 # pixels
canvas_left_and_right_border = 300 # pixels
canvas_width = (backing_width + canvas_left_and_right_border)
canvas_height = (backing_height + canvas_top_and_bottom_border)

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# set up the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(mark_centre_points = True):

    # Set up the drawing canvas
    setup(canvas_width, canvas_height)

    # Draw as fast as possible
    tracer(False)

    # Colour the sky blue
    bgcolor('sky blue')

    # Draw the ground as a big green rectangle (sticking out of the
    # bottom edge of the drawing canvas slightly)
    overlap = 5 # pixels
    grass_height = 100 # pixels
    penup()
    goto(-(canvas_width // 2 + overlap),
         -(canvas_height // 2 + overlap)) # start at the bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_height + overlap)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_height + overlap)
    end_fill()

    # Draw a nice warm sun peeking into the image
    penup()
    goto(-canvas_width // 2, canvas_height // 2)
    color('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height // 3)
    color('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Draw the billboard's wooden backing as four frames
    # and some highlighted coordinates
    #
    # Outer rectangle
    goto(- backing_width // 2, - backing_height // 2) # bottom left
    pencolor('sienna'); fillcolor('tan'); width(3)
    begin_fill()
    pendown()
    setheading(90) # face north
    forward(backing_height)
    right(90) # face east
    forward(backing_width)
    right(90) # face south
    forward(backing_height)
    right(90) # face west
    forward(backing_width)
    end_fill()

    # Inner rectangle
    penup()
    goto(- backing_width // 2 + backing_margin,
         - backing_height // 2 + backing_margin) # bottom left
    fillcolor('gainsboro')
    begin_fill()
    pendown()
    setheading(90) # face north
    forward(backing_height - backing_margin * 2)
    right(90) # face east
    forward(backing_width - backing_margin * 2)
    right(90) # face south
    forward(backing_height - backing_margin * 2)
    right(90) # face west
    forward(backing_width - backing_margin * 2)
    end_fill()

    # Draw lines separating the locations where the sheets go
    width(1); pencolor('dim grey')
    for horizontal in [-sheet_width, 0, sheet_width]:
        penup()
        goto(horizontal, sheet_height // 2)
        pendown()
        setheading(270) # point south
        forward(sheet_height)
         
    # Mark the centre points of each sheet's location, if desired
    if mark_centre_points:
        penup()
        points = [[[round(-sheet_width * 1.5), 0], 'Location 1'],
                  [[round(-sheet_width * 0.5), 0], 'Location 2'],
                  [[round(sheet_width * 0.5), 0], 'Location 3'],
                  [[round(sheet_width * 1.5), 0], 'Location 4']]
        for centre_point, label in points:
            goto(centre_point)
            dot(4)
            write('  ' + label + '\n  (' + str(centre_point[0]) + ', 0)',
                  font = ('Arial', 12, 'normal'))
     
    # Reset everything ready for the student's solution
    color('black')
    width(1)
    penup()
    home()
    setheading(0)
    tracer(True)


# End the program by hiding the cursor and releasing the canvas
def release_drawing_canvas():
    tracer(True)
    hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data------------------------------------------------------#
#
# The list in this section contains the data sets you will use to
# test your code.  Each of the data sets is a list specifying the
# way in which sheets are pasted onto the billboard:
#
# 1. The name of the sheet, from 'Sheet A' to 'Sheet D'
# 2. The location to paste the sheet, from 'Location 1' to
#    'Location 4'
# 3. The sheet's orientation, either 'Upright' or 'Upside down'
#
# Each data set does not necessarily mention all four sheets.
#
# In addition there is an extra value, either 'X' or 'O' at the
# start of each data set.  The purpose of this value will be
# revealed only in Part B of the assignment.  You should ignore it
# while completing Part A.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#
# Note that your solution must work for all the data sets below
# AND ANY OTHER DATA SETS IN THE SAME FORMAT!
#

data_sets = [
    # These two initial data sets don't put any sheets on the billboard
    # Data sets 0 - 1
    ['O'],
    ['X'],
    # These data sets put Sheet A in all possible locations and orientations
    # Data sets 2 - 9
    ['O', ['Sheet A', 'Location 1', 'Upright']],
    ['O', ['Sheet A', 'Location 2', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright']],
    ['O', ['Sheet A', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 1', 'Upside down']],
    ['O', ['Sheet A', 'Location 2', 'Upside down']],
    ['O', ['Sheet A', 'Location 3', 'Upside down']],
    ['O', ['Sheet A', 'Location 4', 'Upside down']],
    # These data sets put Sheet B in all possible locations and orientations
    # Data sets 10 - 17
    ['O', ['Sheet B', 'Location 1', 'Upright']],
    ['O', ['Sheet B', 'Location 2', 'Upright']],
    ['O', ['Sheet B', 'Location 3', 'Upright']],
    ['O', ['Sheet B', 'Location 4', 'Upright']],
    ['O', ['Sheet B', 'Location 1', 'Upside down']],
    ['O', ['Sheet B', 'Location 2', 'Upside down']],
    ['O', ['Sheet B', 'Location 3', 'Upside down']],
    ['O', ['Sheet B', 'Location 4', 'Upside down']],
    # These data sets put Sheet C in all possible locations and orientations
    # Data sets 18 - 25
    ['O', ['Sheet C', 'Location 1', 'Upright']],
    ['O', ['Sheet C', 'Location 2', 'Upright']],
    ['O', ['Sheet C', 'Location 3', 'Upright']],
    ['O', ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down']],
    ['O', ['Sheet C', 'Location 2', 'Upside down']],
    ['O', ['Sheet C', 'Location 3', 'Upside down']],
    ['O', ['Sheet C', 'Location 4', 'Upside down']],
    # These data sets put Sheet D in all possible locations and orientations
    # Data sets 26 - 33
    ['O', ['Sheet D', 'Location 1', 'Upright']],
    ['O', ['Sheet D', 'Location 2', 'Upright']],
    ['O', ['Sheet D', 'Location 3', 'Upright']],
    ['O', ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet D', 'Location 1', 'Upside down']],
    ['O', ['Sheet D', 'Location 2', 'Upside down']],
    ['O', ['Sheet D', 'Location 3', 'Upside down']],
    ['O', ['Sheet D', 'Location 4', 'Upside down']],
    # These data sets place two sheets in various locations and orientations
    # Data sets 34 - 38
    ['O', ['Sheet D', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet B', 'Location 1', 'Upright']],
    ['O', ['Sheet D', 'Location 1', 'Upside down'],
          ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet B', 'Location 2', 'Upside down']],
    ['X', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upside down']],
    # These data sets place three sheets in various locations and orientations
    # Data sets 39 - 43
    ['O', ['Sheet A', 'Location 4', 'Upright'],
          ['Sheet B', 'Location 3', 'Upright'],
          ['Sheet C', 'Location 2', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down'],
          ['Sheet D', 'Location 3', 'Upside down'],
          ['Sheet A', 'Location 4', 'Upright']], 
    ['O', ['Sheet B', 'Location 4', 'Upright'],
          ['Sheet D', 'Location 2', 'Upside down'],
          ['Sheet C', 'Location 1', 'Upside down']], 
    ['X', ['Sheet A', 'Location 4', 'Upright'],
          ['Sheet D', 'Location 3', 'Upside down'],
          ['Sheet C', 'Location 2', 'Upright']],
    # These data sets place four sheets in various locations and orientations
    # Data sets 44 - 48
    ['O', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 2', 'Upright'],
          ['Sheet B', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 1', 'Upright'],
          ['Sheet A', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upside down']],
    ['O', ['Sheet C', 'Location 2', 'Upright'],
          ['Sheet B', 'Location 3', 'Upside down'],
          ['Sheet D', 'Location 1', 'Upside down'],
          ['Sheet A', 'Location 4', 'Upright']],
    ['X', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upside down'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upside down']],     
    # These data sets draw the entire image upside down
    # Data sets 49 - 50
    ['X', ['Sheet A', 'Location 4', 'Upside down'],
          ['Sheet B', 'Location 3', 'Upside down'],
          ['Sheet C', 'Location 2', 'Upside down'],
          ['Sheet D', 'Location 1', 'Upside down']],
    ['O', ['Sheet A', 'Location 4', 'Upside down'],
          ['Sheet B', 'Location 3', 'Upside down'],
          ['Sheet C', 'Location 2', 'Upside down'],
          ['Sheet D', 'Location 1', 'Upside down']],
    # These are the final, 'correct' arrangements of sheets
    # Data sets 51 - 52
    ['X', ['Sheet A', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']]
    ]

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "paste_up" function.
#

# Paste the sheets onto the billboard as per the provided data set

def paste_up(data_sets):
    s = 1
    # Locations to paste sheets
    def Location_1(): 
        goto(-400,-250)
            
    def Location_2():
        goto(-200,-250)

    def Location_3():
        goto(0,-250)

    def Location_4():
        goto(200,-250)

    # Given the data range from 0 - 52
    for i in range(len(data_sets)-1):

        # Assigning location functions to 'Location []' in data_sets
        if (data_sets[s][1]) == 'Location 1':
            Location_1()
        if (data_sets[s][1]) == 'Location 2':
            Location_2()
        if (data_sets[s][1]) == 'Location 3':
            Location_3()
        if (data_sets[s][1]) == 'Location 4':
            Location_4()

        # Defining upside down sheet functions
        def Sheet_1U():
            background_colour() 
            color('SteelBlue')
            setheading(180) # Flips the letters
            # Letter H
            if (data_sets[s][1]) == 'Location 1':
            # When assigned to location 1, letter coordinates go here
                goto(-215,62.5)
                Letter_HU1()
                goto(-315,-40)
                Letter_HU2()
            if (data_sets[s][1]) == 'Location 2':
            # When assigned to location 2, letter coordinates go here
                goto(-30,62.5)
                Letter_HU1()
                goto(-130,-40)
                Letter_HU2()
            if (data_sets[s][1]) == 'Location 3':
            # When assigned to location 3, letter coordinates go here
                goto(180,62.5)
                Letter_HU1()
                goto(80,-40)
                Letter_HU2()
            if (data_sets[s][1]) == 'Location 4':
            # When assigned to location 4, letter coordinates go here
                goto(370,62.5)
                Letter_HU1()
                goto(270,-40)
                Letter_HU2()
            # Resets coordinates for Graffiti if called
            home()
                
        def Sheet_2U():
            background_colour()
            color('SteelBlue')
            setheading(180)
            # Letter A
            if (data_sets[s][1]) == 'Location 1':
                goto(-210,62.5)
                Letter_AU1()
                goto(-346,5)  
                Letter_AU2()
            if (data_sets[s][1]) == 'Location 2':
                goto(-10,62.5)
                Letter_AU1()
                goto(-146,5)
                Letter_AU2()
            if (data_sets[s][1]) == 'Location 3':
                goto(190,62.5)
                Letter_AU1()
                goto(54,5)
                Letter_AU2()
            if (data_sets[s][1]) == 'Location 4':
                goto(390,62.5)
                Letter_AU1()
                goto(254,5)
                Letter_AU2()
            home()

        def Sheet_3U():
            background_colour()
            color('SteelBlue')
            setheading(180)
            # Letter L
            if (data_sets[s][1]) == 'Location 1':
                goto(-230,42.5)
                Letter_LU1()
                goto(-400,-62.6)
                Letter_LU2()
            if (data_sets[s][1]) == 'Location 2':
                goto(-30,42.5)
                Letter_LU1()
                goto(-200, -62.6)
                Letter_LU2()
            if (data_sets[s][1]) == 'Location 3':
                goto(170,42.5)
                Letter_LU1()
                goto(0, -62.6)
                Letter_LU2()
            if (data_sets[s][1]) == 'Location 4':
                goto(370,42.5)
                Letter_LU1()
                goto(200,-62.6)
                Letter_LU2()
            home()

        def Sheet_4U():
            background_colour()
            color('SteelBlue')
            setheading(180)
            # Letter O
            if (data_sets[s][1]) == 'Location 1':
                goto(-270,20)
                Letter_OU1()
                goto(-250,62.5)
                Letter_OU2()
            if (data_sets[s][1]) == 'Location 2':
                goto(-100,20)
                Letter_OU1()
                goto(-80,62.5)
                Letter_OU2()
            if (data_sets[s][1]) == 'Location 3':
                goto(100,20)
                Letter_OU1()
                goto(120,62.5)
                Letter_OU2()
            if (data_sets[s][1]) == 'Location 4':
                goto(300,20)
                Letter_OU1()
                goto(320,62.5)
                Letter_OU2()
            home()
            
        # Assigning Upside down sheet functions to 'Sheet[]' and
        # orientation in columns 1 and 3 respectively in data_sets
        if data_sets[s][2] == 'Upside down':
            if (data_sets[s][0]) == 'Sheet A':
                Sheet_1U()
            if (data_sets[s][0]) == 'Sheet B':
                Sheet_2U()
            if (data_sets[s][0]) == 'Sheet C':
                Sheet_3U()
            if (data_sets[s][0]) == 'Sheet D':
                Sheet_4U()

        # Defining upright sheet functions
        def Sheet_1():
            background_colour()
            color('SteelBlue')
            # Letter H
            if (data_sets[s][1]) == 'Location 1':
                goto(-350,-62.5)
                Letter_H1()
                goto(-250,40)
                Letter_H2()
            if (data_sets[s][1]) == 'Location 2':
                goto(-180,-62.5)
                Letter_H1()
                goto(-80,40)
                Letter_H2()
            if (data_sets[s][1]) == 'Location 3':
                goto(30,-62.5)
                Letter_H1()
                goto(130,40)
                Letter_H2()
            if (data_sets[s][1]) == 'Location 4':
                goto(230,-62.5)
                Letter_H1()
                goto(330,40)
                Letter_H2()
            home()
                
        def Sheet_2():
            background_colour()
            color('SteelBlue')
            # Letter A
            if (data_sets[s][1]) == 'Location 1':
                goto(-380,-62.5)
                Letter_A1()
                goto(-244,-5)
                Letter_A2()
            if (data_sets[s][1]) == 'Location 2':
                goto(-180,-62.5)
                Letter_A1()
                goto(-44,-5)
                Letter_A2()
            if (data_sets[s][1]) == 'Location 3':
                goto(10,-62.5)
                Letter_A1()
                goto(146,-5)
                Letter_A2()
            if (data_sets[s][1]) == 'Location 4':
                goto(210,-62.5)
                Letter_A1()
                goto(346,-5)
                Letter_A2()
            home()
            
        def Sheet_3():
            background_colour()
            color('SteelBlue')
            # Letter L
            if (data_sets[s][1]) == 'Location 1':
                goto(-370,-42.5)
                Letter_L1()
                goto(-200,62.6)
                Letter_L2()
            if (data_sets[s][1]) == 'Location 2':
                goto(-170,-42.5)
                Letter_L1()
                goto(0,62.6)
                Letter_L2()
            if (data_sets[s][1]) == 'Location 3':
                goto(30,-42.5)
                Letter_L1()
                goto(200, 62.6)
                Letter_L2()
            if (data_sets[s][1]) == 'Location 4':
                goto(230,-42.5)
                Letter_L1()
                goto(400,62.6)
                Letter_L2()
            home()

        def Sheet_4():
            background_colour()
            color('SteelBlue')
            # Letter O
            if (data_sets[s][1]) == 'Location 1':
                goto(-350,-20)
                Letter_O1()
                goto(-350,-62.5)
                Letter_O2()
            if (data_sets[s][1]) == 'Location 2':
                goto(-150,-20)
                Letter_O1()
                goto(-150,-62.5)
                Letter_O2()
            if (data_sets[s][1]) == 'Location 3':
                goto(50,-20)
                Letter_O1()
                goto(50,-62.5)
                Letter_O2()
            if (data_sets[s][1]) == 'Location 4':
                goto(250,-20)
                Letter_O1()
                goto(250,-62.5)
                Letter_O2()
            home()
                
        # Assigning Upright sheet functions to 'Sheet[]' and
        # orientation in columns 1 and 3 respectively in data_sets
        if data_sets[s][2] == 'Upright':
            if data_sets[s][0] == 'Sheet A':
                Sheet_1()
            if data_sets[s][0] == 'Sheet B':
                Sheet_2()
            if data_sets[s][0] == 'Sheet C':
                Sheet_3()
            if data_sets[s][0] == 'Sheet D':
                Sheet_4()
                
        s = s + 1

    # Defining the Graffito Function
    def Graffiti():
        Initial_K()
        Initial_D()

    # Graffiti Paste Condition
    if 'X' in data_sets:
        Graffiti()

#--------------------------------------------------------------------#


#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your billboard.  Do not change any of this code except
# where indicated by comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the centre points of each sheet on the backing
create_drawing_canvas()
    

#---START---#

def background_colour():
    color('Black','White')
    fillcolor('Black')
    pencolor('White')
    pensize(2)
    pendown()
    begin_fill()
    setheading(90)
    forward(500)
    right(90)
    forward(200)
    right(90)
    forward(500)
    right(90)
    forward(200)
    end_fill()
    pensize(1)
    penup()
    home()

def Initial_K():
    #Letter K
    color('Red')
    pensize(30)
    goto(-175,175)
    pendown()
    right(100)
    forward(150)
    left(135)
    forward(200)
    left(180)
    forward(200)
    left(90)
    forward(200)
    left(180)
    forward(200)
    left(135)
    forward(150)
    penup()
    pensize(1)
    home()

def Initial_D():
    #Letter D
    color('Red')
    pensize(30)
    goto(75,140)
    pendown()
    right(100)
    forward(300)
    left(90)
    forward(100)
    left(45)
    forward(130)
    left(45)
    forward(130)
    left(45)
    forward(120)
    left(45)
    forward(110)
    penup()
    pensize(1)

#---UPRIGHT LETTERS---#

def Letter_H1():
    # Half H
    begin_fill()
    pendown()
    left(90)
    forward(125)
    right(90)
    forward(35)
    right(90)
    forward(50)
    left(45)
    forward(5)
    left(45)
    forward(60)
    right(90)
    forward(20)
    right(90)
    forward(55)
    left(90)
    forward(52)
    right(90)
    forward(44)
    end_fill()
    penup()

def Letter_H2():
    # Half H
    begin_fill()
    pendown()
    left(90)
    forward(103)
    left(90)
    forward(35)
    left(90)
    forward(72)
    circle(30.5,100)
    end_fill()
    penup()

def Letter_A1():
    # Bottom A
    begin_fill()
    pendown()
    forward(35)
    left(45)
    forward(50)
    right(45)
    forward(35)
    right(45)
    forward(50)
    left(45)
    forward(35)
    left(125)
    forward(70)
    left(55)
    forward(100)
    left(58)
    forward(68)
    end_fill()
    penup()

def Letter_A2():
    # Top A
    begin_fill()
    pendown()
    right(115)
    forward(80)
    left(57)
    forward(15)
    left(60)
    forward(60)
    left(120)
    forward(15)
    left(60)
    forward(5)
    left(254)
    forward(28)
    left(47)
    forward(52)
    end_fill()
    penup()

def Letter_L1():
    # Letter L
    begin_fill()
    pendown()
    left(90)
    forward(105)
    right(90)
    forward(20)
    right(45)
    forward(40)
    right(45)
    forward(60)
    circle(25,50)
    left(40)
    forward(70)
    right(45)
    forward(15)
    right(45)
    forward(6)
    right(90)
    forward(125)
    right(55)
    forward(23)
    end_fill()
    penup()

def Letter_L2():
    # Letter O sticking out
    begin_fill()
    pendown()
    left(90)
    forward(60)
    left(90)
    forward(15)
    left(90)
    forward(50)
    left(55)
    forward(18)
    end_fill()
    penup()

def Letter_O1():
    # Dot
    begin_fill()
    pendown()
    circle(15)
    end_fill()
    penup()

def Letter_O2():
    # Exterior O
    begin_fill()
    pendown()
    forward(50)
    left(45)
    forward(70)
    right(45)
    forward(20)
    left(90)
    forward(15)
    left(90)
    forward(20)
    right(45)
    forward(86)
    left(45)
    forward(88)
    left(90)
    forward(20)
    left(90)
    forward(80)
    right(45)
    forward(70)
    left(270)
    forward(55)
    right(45)
    forward(60)
    right(45)
    forward(42)
    left(135)
    forward(25)
    left(45)
    forward(31)
    left(45)
    forward(28)
    end_fill()
    penup()
    

#---UPSIDE DOWN LETTERS---#

def Letter_HU1():
    # Half H
    begin_fill()
    pendown()
    left(90)
    forward(125)
    right(90)
    forward(35)
    right(90)
    forward(50)
    left(45)
    forward(5)
    left(45)
    forward(60)
    right(90)
    forward(20)
    right(90)
    forward(55)
    left(90)
    forward(51)
    right(90)
    forward(46)
    end_fill()
    penup()

def Letter_HU2():
    # Half H
    begin_fill()
    pendown()
    left(90)
    forward(103)
    left(90)
    forward(35)
    left(90)
    forward(72)
    circle(30.5,100)
    end_fill()
    penup()

def Letter_AU1():
    # Bottom A
    begin_fill()
    pendown()
    forward(35)
    left(45)
    forward(50)
    right(45)
    forward(35)
    right(45)
    forward(50)
    left(45)
    forward(35)
    left(125)
    forward(70)
    left(55)
    forward(100)
    left(58)
    forward(68)
    end_fill()
    penup()

def Letter_AU2():
    # Top A
    begin_fill()
    pendown()
    right(115)
    forward(80)
    left(57)
    forward(15)
    left(60)
    forward(60)
    left(120)
    forward(15)
    left(60)
    forward(5)
    left(254)
    forward(28)
    left(47)
    forward(52)
    end_fill()
    penup()

def Letter_LU1():
    # Letter L
    begin_fill()
    pendown()
    left(90)
    forward(105)
    right(90)
    forward(20)
    right(45)
    forward(40)
    right(45)
    forward(60)
    circle(25,50)
    left(40)
    forward(70)
    right(45)
    forward(15)
    right(45)
    forward(6)
    right(90)
    forward(125)
    right(55)
    forward(23)
    end_fill()
    penup()

def Letter_LU2():
    # Letter O sticking out
    begin_fill()
    pendown()
    left(90)
    forward(60)
    left(90)
    forward(17)
    left(90)
    forward(50)
    left(55)
    forward(18)
    end_fill()
    penup()

def Letter_OU1():
    # Dot
    begin_fill()
    pendown()
    circle(15)
    end_fill()
    penup()

def Letter_OU2():
    # Exterior O
    begin_fill()
    pendown()
    forward(50)
    left(45)
    forward(70)
    right(45)
    forward(20)
    left(90)
    forward(15)
    left(90)
    forward(20)
    right(45)
    forward(85)
    left(45)
    forward(87)
    left(90)
    forward(20)
    left(90)
    forward(80)
    right(45)
    forward(70)
    left(270)
    forward(55)
    right(45)
    forward(60)
    right(45)
    forward(42)
    left(135)
    forward(25)
    left(45)
    forward(31)
    left(45)
    forward(28)
    end_fill()
    penup()
    
#---END---#

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with one that describes the image
# ***** displayed on your billboard when the sheets are pasted
# ***** correctly
title("Halo")

### Call the student's function to display the billboard
### ***** Change the number in the argument to this function
### ***** to test your code with a different data set
paste_up(data_sets[49])

# Exit gracefully
release_drawing_canvas()

#
#--------------------------------------------------------------------#

