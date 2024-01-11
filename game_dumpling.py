"""
Name(s): Sirisha Thapa 
CSC 201
Project 3
 
This game is used to shoot the dumplings.The user shall shoot the dumplings that is falling from top.If the dumplings touches the human,
you loose the game. 
 
Document Assistance: (who and what  OR  declare that you gave or received no assistance):
I took help from zelle graphics pdf to be familer with concepts like getAnchor(), getY(), displaying text on screen
and changing its font type and size.
I took help from powerpoint slide of moving the circle to be familer with animation timing and features.
I took witch_game.py as my reference for writing this code.
I took help from following websites for following things:
1) For importing sound : https://www.geeksforgeeks.org/play-sound-in-python/
2) For making while loop work: https://www.coursera.org/tutorials/python-break


Bonus Additions:
1) When the code is run, user is given an option to enter their gaming name and the gaming name is displayed with a welcome message.
2) I have added sound for 3 different parts:
   (Please install pygame package to make sound run in the game)
   i) When the game runs there is the start mp3 which will only sound wooosh.
   ii) When the user looses, oh noo!! sound is played.
   iii) When user wins, congratulations sound is played.
3) After the user wins/looses (game end), user will be given a entry box where they can enter yes if they want to  play the game again.
 
"""

from graphics2 import *
import math 
import random
import time

import sys
#import subprocess # sound for mac
from pygame import mixer  

    

# This values are fixed and doesnot change.

WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
X_MIDPOINT = WINDOW_WIDTH / 2
Y_MIDPOINT = WINDOW_HEIGHT / 2
DUMPLING_SPEED = 15 # BY DEFAULT SPEED
HUMAN_SPEED = 100
WINNING_POINTS = 20
BOX_SPEED = 40
THRESHOLD = 50
DUMPLINGS_HUMAN_THRESHOLD = 90
    

def bamboo_box(window,human):
    
    """
    This displays bamboo box picture right in middle using midpoints of the window as its  points
    and box.gif as its image.
    Params:
    Takes window as its parameter to draw/display  image on screen.
    Returns:
    returns bamboo image 
 
    """
    x = human.getAnchor().getX()
    y_coordinate = human.getAnchor().getY()
    y_coordinate = y_coordinate - 100

    bamboo = Image(Point(x, y_coordinate), "box.gif")
    bamboo.draw(window)

    return bamboo
    
    
    
# displays human image

def human_image(window):
    """
    Displays human picture on window based upon randomly x cooridnate of mid point 
    and picture file human.gif
    
    Params:
    Takes window as its parameter to draw/display image on screen.
    
    Returns:
    human which stores human picture in it 
    """
    
    default_x = X_MIDPOINT
    default_y = 685

    human = Image(Point(default_x,default_y),"human.gif")
    human.draw(window)

    return human
    
def dumpling_image(window):
    
    """
    Displays dumpling picture on window based upon randomly generated x coordinate
    and picture file dumpling.gif
    
    Params:
    Takes window as its parameter to draw/display image on screen.
    
    Returns:
        dumpling which stores dumpling picture.
    """
    x_coordinate = random.randrange(50,700)

    dumpling = Image(Point(x_coordinate,0),"dumpling.gif")
    dumpling.draw(window)

    return dumpling


    



def moveDumpling(dumpling_list):
    
    """
    This takes dumpling_list as its parameter and
    hence move the dumpling  vertically down
    based upon the dumpling speed.
    
    Params:
    Dumpling_list
    Type: list
    dumpling_list is the list that contains the image of dumplings. 
    """
    for dumplings in dumpling_list:
        dumplings.move(0,DUMPLING_SPEED)
        

    
        

def human_move(human, click_point , min_height_limit,min_width_limit,max_width):
    """
    This takes human, click_point and min_height_limit as its parameter and
    hence move the human image horizontally left and right based upon the
    human speed and give conditions.
    
    Params:
    
    human : it is a image of human.
    
    click_point :
    datatype = tuple
    It gets the points from the user based upon the mouse clicks.
    
    min_height_limit :
    type = float
    It is the minimum height  of image and its value is used to compare with y coordinate to see if y coordinate is greater than it or not.
    
    min_width_limit:
    type = float
    It  is the minimum width  of image and it's value is used to compare  with x coordinate to see if x coordinate is lesser than it or not.
    
    
    max_width:
    type = float
    It is the maximum width of the image and it is used to see if x coordinate is greather than max width or not.

    
    
    """
    
    if click_point is not None:

        
        x_coordinate = click_point.getX()
        
        y_coordinate = click_point.getY()
            
            
        if y_coordinate > min_height_limit and x_coordinate < min_width_limit :
              
             human.move(-HUMAN_SPEED,0) # for left
                  
        elif y_coordinate > min_height_limit and x_coordinate > max_width :
            
             human.move(HUMAN_SPEED,0) # for right
             

def play_sound(file_path):
    '''
    This function helps to play sound track in different parts of the game.
    
    Params:
    file_path:
    type = string
    it helps to play sound based upon the path or name of the sound file.
    '''
    mixer.init()
    sound = mixer.Sound(file_path)
    sound.play()           
    
def bamboo_box_move(bamboo_box):
    '''
    This is used to move the bamboo box based upon the box speed.
    params:
    bamboo_box
    type : list
    it stores the images of bamboo boxes in a list and hence helps each of the bambo box images to move.
    '''
    bamboo_box.move(0,-BOX_SPEED)
    
    
    

def distance_between_points(point1, point2):
    '''
    This helps to find distance between two images based upon their points.
    Params:
    Point1:
    type : tuple
    it stores the center point of the images 
    
    
    Point2:
    type:tuple
    it stores the center point of the images
    
    returns:
    returns the formula to calculate distance between two points.
    '''
    p1x = point1.getX()
    p1y = point1.getY()

    p2x = point2.getX()
    p2y = point2.getY()

    return math.sqrt((p1x - p2x) * (p1x - p2x) + (p1y - p2y) * (p1y - p2y))

def is_close_enough(human, dumpling_image):
    '''
    This helps to find anchor or center point of the images.
    Params:
    human:
    type : image
    it passes the human image 
    
    
    dumpling_image:
    type:image
    it is the dumpling picture
    
    returns:
    returns the calculation of distance between two points by passing the center/anchor point of the images.
    '''
    
    point1 = dumpling_image.getAnchor()
    point2 = human.getAnchor()

    return distance_between_points(point1, point2 )



def game_won(window,points):
    '''
    It creates a rectangle when user wins and displays some text and plays sound on that window.
    params:
    window - this is the screen where all the work of this function takes place.
    '''
            
    
    rectangle = Rectangle(Point(0,0),Point(WINDOW_WIDTH, WINDOW_HEIGHT))
    rectangle.setFill("Black")
    rectangle.draw(window)

    winer =  Text(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 20),"You Wonnnnnnn!!!!!")
    marks = Text(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 20 + 30),f"You managed to collect {points} dumplingssss!!!!")
    
    winer.setTextColor("red")
    winer.setSize(18)
    marks.setSize(18)
    
    marks.setTextColor("red")
    marks2 = Text(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 20 + 70),"Click anywhere on screen")
    
    marks2.setTextColor("red")
    marks2.setStyle("italic")
    marks2.setSize(16)
            
    winer.draw(window)
    marks.draw(window)
    marks2.draw(window)

    play_sound("congrats.mp3")
    play_sound("congo.mp3")
            
    star = Image(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2),"star.gif")
    star.draw(window)
    time.sleep(0.2)

    star2 = Image(Point(WINDOW_WIDTH / 2 - 120, WINDOW_HEIGHT / 2),"star.gif")
    star2.draw(window)
    time.sleep(0.2)

    star3 = Image(Point(WINDOW_WIDTH / 2 + 120, WINDOW_HEIGHT / 2),"star.gif")
    star3.draw(window)
    time.sleep(0.2)
            
    window.getMouse()
    play_again(window)

def game_lost(window,points):
    
    '''
    It creates a rectangle when user looses and displays some text and plays sound on that window.
    params:
    window - this is the screen where all the work of this function takes place.
    points :
    type = integer
    this is the total score the user earned in the game.
    '''

    rectangle = Rectangle(Point(0,0),Point(800,800))
    rectangle.setFill("red")
    rectangle.draw(window)

    marks = Text(Point(WINDOW_WIDTH /2 ,WINDOW_HEIGHT / 20 + 30),"YOU LOOSEEEEEEEE !!!")
    marks.setStyle("bold")
    marks.setSize(18)
    marks.setTextColor("Black")
    marks.draw(window)

    marks3 = Text(Point(WINDOW_WIDTH /2 ,WINDOW_HEIGHT / 20 + 60),f"Your Score is {points}")
    marks3.setStyle("bold")
    marks3.setSize(18)
    marks3.setTextColor("Black")
    marks3.draw(window)
    
    marks2 = Text(Point(WINDOW_WIDTH /2 ,WINDOW_HEIGHT / 20 + 90),"Click anywhere on screen")
    marks2.setTextColor("Black")
    marks2.setStyle("italic")
    marks2.setSize(16)
    marks2.draw(window)

    ohno = Image(Point(X_MIDPOINT,650),"ohno.gif")
    ohno.draw(window)
    play_sound("ohno.mp3")

    window.getMouse()

    play_again(window)
    

def play_again(window):
    '''
    This asks users if they want to play the game again or not.If they want to play the game they should enter yes in the box.
    Params:
    window -  this is the screen where all the work of this function takes place.
    '''
    user_response = Text(Point(WINDOW_WIDTH / 2,WINDOW_HEIGHT / 20 + 140),"Enter yes if you want to play again and click on screen \n or Click anywhere on screen to exit")
    user_response.setSize(20)
    user_response.setStyle("bold")
    user_response.setTextColor("white")
    user_response.draw(window)
    
    userInput = Entry(Point(WINDOW_WIDTH / 2,WINDOW_HEIGHT / 10 + 180), 10)
    userInput.draw(window)
    
    window.getMouse()
    
    inputStr = userInput.getText()
    inputStr = inputStr.lower() 
    if inputStr == "yes":
        window.close()
        main() 
    else: 
        #window.close()
        sys.exit(1)
        


def game_loop(window):
    
    """
    Displays points on the corner of the window which decreases each time the dumpling leaves the bottom and increases each time user shoots the dumplings.
    This function also calls human_image function and bamboo_box function.It creates a dumpling list and bamboo box list and based upon
    the looping condition it shows them in screen....
    Whenever user press the space key, it launches the bamboo box and both dumpling and box that hit eachother removes  and undraw.
    It uses while loop until game is over or points is equals to winning score. 
    
    
    params:
    window - this is the screen where all the work of this function takes place.
    
    """
    # for displaying bamboo box and human image 
    human = human_image(window)
    
    # for displaying points on window 
    points = 0
    score = Text(Point(600,50), f"Points : {points}")
    score.setFace("arial")
    score.setSize(18)
    score.draw(window)

    dumpling_list = []
    #newDumplings = dumpling_list.copy()
    bamboo_list = []

    
    #bamboo_box_move(bamboo_list,window)

    #bamboo_list.append(bamboo)
    game_over = False 
    
    
    while not game_over and points != WINNING_POINTS:
        play_sound("start.mp3")

        #time.sleep(0.5)
        randomNum = random.randrange(1,700)
        moveDumpling(dumpling_list)
       
        #print(randomNum)
        
        if randomNum < 70:
            dumplings_pic = dumpling_image(window)
            dumpling_list.append(dumplings_pic)  

        for dumplings in dumpling_list:
            
            if dumplings.getAnchor().getY() >= WINDOW_HEIGHT:
                dumplings.undraw()
                dumpling_list.remove(dumplings)
                points -= 1 
                #print(points) 
                score.setText(f"Points : {points}")
    
            elif (is_close_enough(human,dumplings) < DUMPLINGS_HUMAN_THRESHOLD) :
                game_over = True
    
                #time.sleep(3)
                #sys.exit(1)        
    
        # findinf the center point and upper port or half height of the image 
        center_point = human.getAnchor().getY()
        center_point_x = human.getAnchor().getX()

        human_height_upper = human.getHeight() / 2
        human_width_half = human.getWidth() / 2

        min_height_limit = center_point - human_height_upper
        min_width_limit = center_point_x - human_width_half
        max_width = center_point_x + human_width_half
        
        

       # for moving the human image 
        click_point = window.checkMouse()
        human_move(human, click_point, min_height_limit, min_width_limit, max_width)
        
        
        keys = window.checkKey()
        
        if keys == "space":
            
            bamboo_box_pic = bamboo_box(window,human)
            bamboo_list.append(bamboo_box_pic) # adding to bamboo list 
            
            
        for bamboos in bamboo_list:
            bamboo_box_move(bamboos)
            
            for dumplings in dumpling_list:
                
                if (is_close_enough(bamboos,dumplings) < THRESHOLD) :
                    dumplings.undraw()
                    dumpling_list.remove(dumplings)

                    bamboos.undraw()
                    bamboo_list.remove(bamboos)
                    
                    points += 1
                    score.setText(f"Points : {points}")
                    
    
                    #print("exact",is_close_enough(human,dumplings))
                    
    if points == WINNING_POINTS:
        game_won(window,points)
            
    else:
        game_lost(window,points)


def set_background(window,photo):
    '''
    It sets the background of the main window to the desired image.
    params:
    window - this is the screen whose background needs to be set
    photo - image or path of the desired background picture.
    '''
    background = Image(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), photo)
    background.draw(window)

            
def display_window(win):
    '''
    This displays the first window of the screen.It asks users their gaming name and hence shows the welcome message with their gaming name.
    In that window, it shows the rules and instructions based upon how to play the game.
    
    Params:
    win - this is the first window which is created in the screen. 

   '''
    message = Text(Point(WINDOW_WIDTH / 2,WINDOW_HEIGHT / 20),"Enter your gaming name here:")
    message.setSize(20)
    message.setStyle("bold")
    message.draw(win)

    userInput = Entry(Point(WINDOW_WIDTH / 2,WINDOW_HEIGHT / 10), 10)
    userInput.draw(win)

    win.getMouse()
    inputStr = userInput.getText()
    
    
    userInput.undraw()
    message.undraw()
    
    welcome = Text(Point(WINDOW_WIDTH / 2,WINDOW_HEIGHT / 20),f"Welcome {inputStr}")
    welcome.setSize(20)
    welcome.setStyle("bold")

    welcome.draw(win)
    time.sleep(1) 
    
    welcome.undraw()
    rules = Text(Point(WINDOW_WIDTH /2 ,WINDOW_HEIGHT / 20),"Game instructions")
    rules.setStyle("bold")
    rules.setSize(30)


    rules.draw(win)
    
    rules1 = Text(Point(171, (WINDOW_HEIGHT / 10))," * Human can only move through mouse clicks.")
    rules2 = Text(Point(343, (WINDOW_HEIGHT / 10) + 30)," * Be sure to not click on the human or above the head of the human because human will not move.")
    rules3 = Text(Point(161, (WINDOW_HEIGHT / 10) + 60)," * Use space key to launch the bamboo box.")
    rules4 = Text(Point(155, (WINDOW_HEIGHT / 10) + 90)," * To win you must score total points of 20.")
    rules5 = Text(Point(162, (WINDOW_HEIGHT / 10) + 120)," * If dumpling touches the human, you loose.")
    rules6 = Text(Point(203, (WINDOW_HEIGHT / 10) + 150)," * If you miss the dumpling, it will reduce your points by 1.")
    rules7 = Text(Point(263, (WINDOW_HEIGHT / 10) + 180)," * For each dumpling touched by bamboo box, points will be increase by 1.")
    
    
    rules1.setSize(16)
    rules2.setSize(16)
    rules3.setSize(16)
    rules4.setSize(16)
    rules5.setSize(16)
    rules6.setSize(16)
    rules7.setSize(16)
   
    
   
    rules1.draw(win)
    rules2.draw(win)
    rules3.draw(win)
    rules4.draw(win)
    rules5.draw(win)
    rules6.draw(win)
    rules7.draw(win)
    
    
    display = Text(Point(WINDOW_WIDTH /2 ,WINDOW_HEIGHT/2),"Press anywhere on the screen to play the game.")
    display.setSize(16)
    display.setStyle("bold")
    display.draw(win)
    win.getMouse()
    win.close() 


def main():
    
    win = GraphWin("Welcome",WINDOW_WIDTH,WINDOW_HEIGHT)
    win.setBackground("pink")
    display_window(win)

    window = GraphWin("Catch The Dumplings",WINDOW_WIDTH,WINDOW_HEIGHT)
    set_background(window,"china.gif")
    game_loop(window)
  
    


    #window.close() 
main()



