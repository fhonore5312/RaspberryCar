# Imports
import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
from time import sleep
import PICAR_controller

# Initialisation
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.mouse.set_visible(0)

# GPIO cleanup in case last execution did not end correctly
PICAR_controller.cleanup()

pressed_left = False
pressed_right = False
pressed_up = False
pressed_down = False


def move():
    if pressed_left:
        PICAR_controller.Motor1_left()
    if pressed_right:
        PICAR_controller.Motor1_right()
    if pressed_up:
        PICAR_controller.Motor2_forward()
    if pressed_down:
        PICAR_controller.Motor2_backward()
    sleep(0.2)
    PICAR_controller.stop()


while 1:
        for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                        sys.exit()
                        PICAR_controller.cleanup()
                elif event.type == pygame.KEYDOWN:          # check for key presses          
                        if event.key == pygame.K_LEFT:        # left arrow turns left
                                print ("appui K_LEFT")
                                pressed_left = True
                        elif event.key == pygame.K_RIGHT:     # right arrow turns right
                            pressed_right = True
                        elif event.key == pygame.K_UP:        # up arrow goes up
                            pressed_up = True
                        elif event.key == pygame.K_DOWN:     # down arrow goes down
                            pressed_down = True
                elif event.type == pygame.KEYUP:            # check for key releases
                        if event.key == pygame.K_LEFT:        # left arrow turns left
                                print ("relache K_LEFT")
                                pressed_left = False
                        elif event.key == pygame.K_RIGHT:     # right arrow turns right
                           pressed_right = False
                        elif event.key == pygame.K_UP:        # up arrow goes up
                           pressed_up = False
                        elif event.key == pygame.K_DOWN:     # down arrow goes down
                           pressed_down = False

        move()
