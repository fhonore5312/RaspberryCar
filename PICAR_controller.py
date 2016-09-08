# Imports
import pygame
import RPi.GPIO as GPIO
from time import sleep

# Initialisation
GPIO.setmode(GPIO.BCM)
# GPIO.cleanup()

# Configuration the PWM settings for the two DC motors on the Raspberry car.
# It defines the two GPIO pins used for the input, starts the PWM and sets the motors' speed to 0

# Configuration of Motor1, motor for direction: going left / going right
# We set the ports used to action Motor1 - GPIO pins are cabled to the electronic component L293
Motor1E = 23
Motor1A = 24
Motor1B = 25

# Configuration of Motor2, motor : going forwards / going backwards
# We set the ports used to action Motor2 - GPIO pins are cabled to the electronic component L293
Motor2E = 21
Motor2A = 16
Motor2B = 20

# On precise que les ports GPIO utilises pour commander les moteurs sont des ports de sortie du GPIO
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

# We define Motor1 and Motor2
Motor1 = GPIO.PWM(Motor1E, 100)
Motor2 = GPIO.PWM(Motor2E, 100)

# We set the speed PWM to 0. To be sure the car is not going to go move !
Motor1.start(0)
Motor2.start(0)

def Motor1_left():
    GPIO.output(Motor1A, True)
    GPIO.output(Motor1B, False)
    Motor1.ChangeDutyCycle(100)
    Motor2.ChangeDutyCycle(100)

def Motor1_right():
    GPIO.output(Motor1A, False)
    GPIO.output(Motor1B, True)
    Motor1.ChangeDutyCycle(100)
    Motor2.ChangeDutyCycle(100)

def Motor2_forward():
    GPIO.output(Motor2A, False)
    GPIO.output(Motor2B, True)
    Motor2.ChangeDutyCycle(100)

def Motor2_backward():
    GPIO.output(Motor2A, True)
    GPIO.output(Motor2B, False)
    Motor2.ChangeDutyCycle(100)

def stop():
    Motor1.ChangeDutyCycle(0)
    Motor2.ChangeDutyCycle(0)

def cleanup():
    GPIO.cleanup()
