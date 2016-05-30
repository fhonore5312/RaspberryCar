# Imports
import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import RPi.GPIO as GPIO
from time import sleep

# Initialisation
pygame.init()
GPIO.setmode(GPIO.BCM)
# GPIO.cleanup()

# Keyboard Variables
pressed_left = False

# Motor1 => moteur de direction
Motor1E = 23
Motor1A = 24
Motor1B = 25

# Motor2 => moteur de marche avant / marche arrière
Motor2E = 21
Motor2A = 16
Motor2B = 20

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

# GPIO.output(Motor1E,GPIO.HIGH)
# GPIO.output(Motor1E,GPIO.HIGH)

Motor1 = GPIO.PWM(23, 100)
Motor2 = GPIO.PWM(21, 100)
Motor1.start(0)
Motor2.start(0)

# marche avant
def forward(speed):
	# print "going forwards"
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	Motor2.ChangeDutyCycle(speed)

# marche arrière
def backward(speed):
	# print "going backwards"
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	Motor2.ChangeDutyCycle(speed)

def stop():
	Motor1.ChangeDutyCycle(0)
	Motor2.ChangeDutyCycle(0)

def move():
	if pressed_left:
		forward(50)
		sleep(2)


# forward(50)
# sleep(2)
# backward(50)
# sleep(2)
# stop()

# event loop

while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()        
            elif event.type == pygame.KEYDOWN:          # check for key presses          
                if event.key == pygame.K_LEFT:        # left arrow turns left
                        print ("appui")
                       # forward(50)
                       # sleep(1)
                        pressed_left = True
                #elif event.key == pygame.K_RIGHT:     # right arrow turns right
                #    pressed_right = True
                #elif event.key == pygame.K_UP:        # up arrow goes up
                #    pressed_up = True
                #elif event.key == pygame.K_DOWN:     # down arrow goes down
                #    pressed_down = True
            elif event.type == pygame.KEYUP:            # check for key releases
                if event.key == pygame.K_LEFT:        # left arrow turns left
                        print ("relache")
                       #  forward(50)
                       #  sleep(1)
                        pressed_left = False
                #elif event.key == pygame.K_RIGHT:     # right arrow turns right
                #    pressed_right = False
                #elif event.key == pygame.K_UP:        # up arrow goes up
                #    pressed_up = False
                #elif event.key == pygame.K_DOWN:     # down arrow goes down
                #    pressed_down = False

        move()

# In your game loop, check for key states:
# if pressed_left:
#     forward(50)
#    sleep(1)
# if pressed_right:
#    forward(50)
#    sleep(1)
# if pressed_up:
#    forward(50)
#    sleep(1)
#if pressed_down:
#    forward(50)
#    sleep(1)


# print "And stop before cleaning up"
# GPIO.output(Motor1E,GPIO.LOW)
# GPIO.output(Motor2E,GPIO.LOW)

GPIO.cleanup()
