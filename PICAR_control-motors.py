# Imports
import RPi.GPIO as GPIO
from time import sleep

# Initialisation
GPIO.setmode(GPIO.BCM)

Motor1E = 23
Motor1A = 24
Motor1B = 25

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

Motor1 = GPIO.PWM(23, 50)
Motor2 = GPIO.PWM(21, 50)
Motor1.start(0)
Motor2.start(0)

# marche avant
def forward(speed):
	print "going forwards"
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	Motor1.ChangeDutyCycle(speed)

# marche arrière
def backward(speed)
	print "going backwards"
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	Motor1.ChangeDutyCycle(speed)

def stop()
	Motor1.ChangeDutyCycle(0)
	Motor2.ChangeDutyCycle(0)
	
forward(50)
sleep(2)
backward(50)
sleep(2)
stop()


# print "And stop before cleaning up"
# GPIO.output(Motor1E,GPIO.LOW)
# GPIO.output(Motor2E,GPIO.LOW)

GPIO.cleanup()