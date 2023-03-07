#File created by Alec Carrera

# import libraries from outside of Python
from time import sleep
from random import randint 
import pygame as pg
import os
import time

#accesses the game's folder, prints file path in terminal
game_folder = os.path.dirname(__file__)
print(game_folder)

# game window settings
WIDTH = 768
HEIGHT = 570
FPS = 30

# define colors
# tuples are immutable - cannot change once created
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#list that sets choices, string for later use
choices = ["rock", "paper", "scissors"]

# function that allows cpu to choose randomly from given list - randint number aligns with order
def cpu_randchoice():
    choice = choices[randint(0,2)]
    print("computer randomly decides..." + choice)
    return choice

# - not working - fucntion that resets photos and fucntions to start screen to allow player to play another round 
def reset():
    chose_screen_image_rect.y = 0
    paper_image_rect.y = 50
    paper_image_rect.x = 50
    rock_image_rect.y = 170
    rock_image_rect.x = 50
    scissors_image_rect.y = 315
    scissors_image_rect.x = 50

#initiates pygame and pygame audio abilities 
pg.init()
pg.mixer.init()

#variable that defines audio file
RWSE = pg.mixer.Sound('rock.win.wav')

#sets volume for sound effect
pg.mixer_music.set_volume(0.3)

# trial and error for sound effects
def scissorbreak():
    RWSE.play()
    pg.time.wait(int(RWSE.get_length() * 1000))
    RWSE.stop()
    
    
#sets game window settings, including title 
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors...")
clock = pg.time.Clock()

#links images found in game folder to varaibles to ease and simplify code
#_rect allows to grab position of photos to control/understand their location and/or job
rock_image = pg.image.load(os.path.join(game_folder, 'new.rock.png')).convert()
rock_image_rect = rock_image.get_rect()
cpu_rock_image_rect = rock_image.get_rect()

paper_image = pg.image.load(os.path.join(game_folder, 'newest.paper.png')).convert()
paper_image_rect = paper_image.get_rect()
cpu_paper_image_rect = paper_image.get_rect()

scissors_image = pg.image.load(os.path.join(game_folder, 'new.scissors.png')).convert()
scissors_image_rect = scissors_image.get_rect()
cpu_scissors_image_rect = scissors_image.get_rect()

startscreen_image = pg.image.load(os.path.join(game_folder, 'startscreen.png')).convert()
startscreen_image_rect = startscreen_image.get_rect()

cpu_rock_win_image = pg.image.load(os.path.join(game_folder, 'cpu.rock.win.png')).convert()
cpu_rock_win_image_rect = cpu_rock_win_image.get_rect()

cpu_rock_lose_image = pg.image.load(os.path.join(game_folder, 'cpu.rock.lose.png')).convert()
cpu_rock_lose_image_rect = cpu_rock_lose_image.get_rect()

cpu_rock_tie_image = pg.image.load(os.path.join(game_folder, 'cpu.rock.tie.png')).convert()
cpu_rock_tie_image_rect = cpu_rock_tie_image.get_rect()

CPW_image = pg.image.load(os.path.join(game_folder, 'cpu.paperwin.png')).convert()
CPW_image_rect = CPW_image.get_rect()

CPL_image = pg.image.load(os.path.join(game_folder, 'cpu.paperlose.png')).convert()
CPL_image_rect = CPL_image.get_rect()

CPT_image = pg.image.load(os.path.join(game_folder, 'cpu.paper.tie.png')).convert()
CPT_image_rect = CPT_image.get_rect()

CSW_image = pg.image.load(os.path.join(game_folder, 'cpu.scissors.win.png')).convert()
CSW_image_rect = CSW_image.get_rect()

CSL_image = pg.image.load(os.path.join(game_folder, 'cpu.scissors.lose.png')).convert()
CSL_image_rect = CSL_image.get_rect()

CST_image = pg.image.load(os.path.join(game_folder, 'cpu.paper.tie.png')).convert()
CST_image_rect = CST_image.get_rect()

chose_screen_image = pg.image.load(os.path.join(game_folder, 'chose.screen.png')).convert()
chose_screen_image_rect = chose_screen_image.get_rect()

replay_image = pg.image.load(os.path.join(game_folder, 'replay.button.pn.png')).convert()
replay_image_rect = replay_image.get_rect()


#
start_screen = True

player_choice = ""
cpu_choice = ""
running = True
replay = False

while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # ########## input ###########
        # HCI - human computer interaction...
        # keyboard, mouse, controller, vr headset
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                print("game on!!!!")
                


        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                print("replay!!!!")
                replay = True
        
        if event.type == pg.MOUSEBUTTONUP:
            print(pg.mouse.get_pos()[0])
            print(pg.mouse.get_pos()[1])
            mouse_coords = pg.mouse.get_pos()
           
            print(rock_image_rect.collidepoint(mouse_coords))
            if rock_image_rect.collidepoint(mouse_coords):
                print("you clicked on rock..")
                player_choice = "rock"
                cpu_choice = cpu_randchoice()
                # call a function that gets the cpu choice...
            elif paper_image_rect.collidepoint(mouse_coords):
                print("you clicked on paper...")
                player_choice = "paper"
                cpu_choice = cpu_randchoice()
       
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("you clicked on scissors...")
                player_choice = "scissors"
                cpu_choice = cpu_randchoice()                 
            else:
                print("you didn't click on anything...")
                
            if replay_image_rect.collidepoint(mouse_coords):
             print("restarting the game")
             reset()


    ############ draw ###################
    #fills window with color black, defined earlier
    # screen.blit calls in image from variables defined through pygame image load
    screen.fill(BLACK)
    screen.blit(chose_screen_image, chose_screen_image_rect)
    screen.blit(cpu_rock_lose_image, cpu_rock_lose_image_rect)
    screen.blit(cpu_rock_win_image, cpu_rock_win_image_rect)
    screen.blit(cpu_rock_tie_image, cpu_rock_tie_image_rect)
    screen.blit(CPL_image, CPL_image_rect)
    screen.blit(CPW_image, CPW_image_rect)
    screen.blit(CPT_image, CPT_image_rect)
    screen.blit(CSW_image, CSW_image_rect)
    screen.blit(CSL_image, CSL_image_rect)
    screen.blit(CST_image, CST_image_rect)
    screen.blit(rock_image, rock_image_rect)
    screen.blit(paper_image, paper_image_rect)
    screen.blit(scissors_image, scissors_image_rect)
    screen.blit(startscreen_image, startscreen_image_rect)
    screen.blit(replay_image, replay_image_rect)
    
    
    # intro screen to game, instructs player to click space to continue playing
    # printing in terminal can help make sure what is happeneing on screen is being recognized by the computer
    # all images called in are pushed off the screem to be called in later 
    if start_screen:
        print("this is working...")
        rock_image_rect.y = 2000
        paper_image_rect.y = 2000
        scissors_image_rect.y = 2000
        chose_screen_image_rect.y = 2000
        cpu_rock_lose_image_rect.y = 1500
        cpu_rock_tie_image_rect.y  = 1501
        cpu_rock_win_image_rect.y = 1504
        CPL_image_rect.y = 1508
        CPT_image_rect.y = 1629
        CPW_image_rect.y = 1738
        CSW_image_rect.y = 1500
        CSL_image_rect.y = 2000
        CST_image_rect.y = 2000
        replay_image_rect.y = 1629


    # sets up game and image positions, allowing player to select rock paper or scissors
    if not start_screen and player_choice == "":
        startscreen_image_rect.y = 2000
        chose_screen_image_rect.y = 0
        paper_image_rect.y = 50
        paper_image_rect.x = 50
        rock_image_rect.y = 170
        rock_image_rect.x = 50
        scissors_image_rect.y = 315
        scissors_image_rect.x = 50
      

    # following if statements both determine what the outcome of the game will be and properly display the results
    # manipulating _rect allows to move photos both in and outside the screen dimensions
    # screen.blit calls in the images needed
    
# list instrctuion for different outcomes to user chosing rock
    if player_choice == "rock":
        rock_image_rect.y = 250
        paper_image_rect.y = 2000
        scissors_image_rect.y = 2000
        if cpu_choice == "rock":
            cpu_rock_image_rect.x = 470
            cpu_rock_image_rect.y = 80
            cpu_rock_tie_image_rect.y = 0
            screen.blit(rock_image, cpu_rock_image_rect)
            replay_image_rect.x = 600
            replay_image_rect.y = 360
            
        if cpu_choice == "paper":
            cpu_paper_image_rect.x = 470
            cpu_paper_image_rect.y = 80
            CPL_image_rect.y = 0
            screen.blit(paper_image, cpu_paper_image_rect)
            replay_image_rect.x = 600
            replay_image_rect.y = 360
            
        if cpu_choice == "scissors":
            cpu_scissors_image_rect.x = 470
            cpu_scissors_image_rect.y = 120
            CSW_image_rect.y = 0 
            screen.blit(rock_image, rock_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            replay_image_rect.x = 600
            replay_image_rect.y = 360
            scissorbreak()
            sleep(1)
            while scissorbreak():
                running = False
           
        
    # list instrctuion for different outcomes to user chosing paper
    if player_choice == "paper":
        paper_image_rect.y = 250
        scissors_image_rect.y = 2000
        rock_image_rect.y = 2000
        if cpu_choice == "rock":
            cpu_rock_image_rect.x = 470
            cpu_rock_image_rect.y = 80
            cpu_rock_win_image_rect.y = 0
            screen.blit(rock_image, cpu_rock_image_rect)
            replay_image_rect.x = 600
            replay_image_rect.y = 360
            
        if cpu_choice == "paper":
            cpu_paper_image_rect.x = 470
            cpu_paper_image_rect.y = 80
            CPT_image_rect.y = 0
            screen.blit(rock_image, rock_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            replay_image_rect.x = 600
            replay_image_rect.y = 360
            
        if cpu_choice == "scissors":
            cpu_scissors_image_rect.x = 470
            cpu_scissors_image_rect.y = 120
            CSL_image_rect.y = 0 
            screen.blit(rock_image, rock_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            replay_image_rect.x = 600
            replay_image_rect.y = 360

# list instrctuion for different outcomes to user chosing scissors
    if player_choice == "scissors":
        rock_image_rect.y = 2000
        paper_image_rect.y = 2000
        scissors_image_rect.y = 250
        if cpu_choice == "rock":
            cpu_rock_image_rect.x = 470
            cpu_rock_image_rect.y = 80
            cpu_rock_lose_image_rect.y = 0
            screen.blit(rock_image, cpu_rock_image_rect)
            replay_image_rect.x = 600
            replay_image_rect.y = 360
            
        if cpu_choice == "paper":
            cpu_paper_image_rect.x = 470
            cpu_paper_image_rect.y = 80
            CPW_image_rect.y = 0
            screen.blit(rock_image, rock_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            replay_image_rect.x = 600
            replay_image_rect.y = 360
            
        if cpu_choice == "scissors":
            cpu_scissors_image_rect.x = 470
            cpu_scissors_image_rect.y = 120
            CST_image_rect.y = 0 
            screen.blit(rock_image, rock_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            replay_image_rect.x = 600
            replay_image_rect.y = 360
 

    pg.display.flip()

#pygame stops running
pg.quit()