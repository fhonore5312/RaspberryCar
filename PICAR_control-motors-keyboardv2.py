# Contrôle de la Raspberry Car à l'aide de la librairie pygame
# Pygame est capable de savoir si une touche reste appuyée et quand elle est relâchée.
# Mais ces événements Pygame sont prévus pour être interceptés dans un écran
# Il est donc nécessaire de se connecter par VNCviewer et de lancer le programme.

# Imports
import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import RPi.GPIO as GPIO
from time import sleep

# Initialisation
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.mouse.set_visible(0)

GPIO.setmode(GPIO.BCM)
# GPIO.cleanup()

# Keyboard Variables
pressed_left = False
pressed_right = False
pressed_up = False
pressed_down = False

# These two blocks of code configure the PWM settings for the two DC motors on the Raspberry car.
# It defines the two GPIO pins used for the input, starts the PWM and sets the motors' speed to 0

# Configuration of Motor1, motor for direction: going left / going right
# On declare les ports qui permettent de piloter le Moteur1 depuis la puce electronique 293
# Motor1 => moteur de direction
Motor1E = 23
Motor1A = 24
Motor1B = 25
# On indique que ces ports sont pilotés depuis le raspberry et sont des ports de sortie
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
# Instruction qui permet d'indiquer que l'on va utiliser 100% de la puissance moteur
Motor1 = GPIO.PWM(Motor1E, 100)
# On force la vitesse à 0
Motor1.start(0)

# Motor2 => moteur de marche avant / marche arrière
Motor2E = 21
Motor2A = 16
Motor2B = 20
# On indique que ces ports sont pilotés depuis le raspberry et sont des ports de sortie
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)
# Instruction qui permet d'indiquer que l'on va utiliser 100% de la puissance moteur
Motor2 = GPIO.PWM(21, 100)
# On force la vitesse à 0
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
        # print ("LEFT")
        Motor1_left()
        Motor1.ChangeDutyCycle(99)
        Motor2.ChangeDutyCycle(99)
    if pressed_right:
        # print ("RIGHT")
        Motor1_right()
        Motor1.ChangeDutyCycle(99)
        Motor2.ChangeDutyCycle(99)
    if pressed_up:
        Motor2_forward()
        Motor2.ChangeDutyCycle(99)
    if pressed_down:
        Motor2_backward()
        Motor2.ChangeDutyCycle(99)
    sleep(0.2)
    stop()

def Motor1_left():
    GPIO.output(Motor1A, True)
    GPIO.output(Motor1B, False)

def Motor1_right():
    GPIO.output(Motor1A, False)
    GPIO.output(Motor1B, True)

def Motor2_forward():
    GPIO.output(Motor2A, False)
    GPIO.output(Motor2B, True)

def Motor2_backward():
    GPIO.output(Motor2A, True)
    GPIO.output(Motor2B, False)

while 1:
        for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                        sys.exit()        
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

#  cleaning up

GPIO.cleanup()
