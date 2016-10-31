# Imports
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
Motor1A = 22
Motor1B = 27

# Configuration of Motor2, motor : going forwards / going backwards
# We set the ports used to action Motor2 - GPIO pins are cabled to the electronic component L293
Motor2E = 17
Motor2A = 18
Motor2B = 24

# Configuration of servo motors
# Pan for horizontal moves
# Tilt for horizontal moves
PanPin = 13
TiltPin = 12

# On precise que les ports GPIO utilises pour commander les moteurs sont des ports de sortie du GPIO
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

GPIO.setup(PanPin,GPIO.OUT)
GPIO.setup(TiltPin,GPIO.OUT)

# We define Motor1 and Motor2
Motor1 = GPIO.PWM(Motor1E, 100)
Motor2 = GPIO.PWM(Motor2E, 100)

# We set the speed PWM to 0. To be sure the car is not going to go move !
Motor1.start(0)
Motor2.start(0)

# Creation of PWM object to control PanTilt
# Servo for Tilt
TiltServo = GPIO.PWM(TiltPin, 50) #50 pulses per second
TiltServo.start(9) #Centers the servo
sleep(0.5) #Allowing the servo to move to the center
TiltServo.ChangeDutyCycle(0) #The black magic. I'll explain later
# Servo for Pan
PanServo = GPIO.PWM(PanPin, 50) #50 pulses per second
PanServo.start(5.9) #Centers the servo
sleep(0.5) #Allowing the servo to move to the center
PanServo.ChangeDutyCycle(0) #The black magic. I'll explain later

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
    print "AVANT"
    GPIO.output(Motor2A, False)
    GPIO.output(Motor2B, True)
    Motor2.ChangeDutyCycle(100)

def Motor2_backward():
    print "ARRIERE"
    GPIO.output(Motor2A, True)
    GPIO.output(Motor2B, False)
    Motor2.ChangeDutyCycle(100)

def stop():
    Motor1.ChangeDutyCycle(0)
    Motor2.ChangeDutyCycle(0)

def move_Tilt (Y):
    degreeY = Y*90
    print "angle Y", degreeY

    if degreeY < -90: #This
        degreeY = -90
    elif degreeY > 90: #and this ensures that we're not overshooting
        degreeY = 90

    dutyY = (0.05555555*degreeY) + 9 #This converts angle to dutycycle
    TiltServo.ChangeDutyCycle(dutyY)
    #TiltServo.ChangeDutyCycle(0) #Again, black magic

def move_Pan (X):
    degreeX = X*90
    print "angle X", degreeX

    if degreeX < -90: #This
        degreeX = -90
    elif degreeX > 90: #and this ensures that we're not overshooting
        degreeX = 90

    dutyX = (0.05555555*degreeX) + 5.9 #This converts angle to dutycycle
    PanServo.ChangeDutyCycle(dutyX)
    #PanServo.ChangeDutyCycle(0) #Again, black magic

def PanTilt_stop():
    PanServo.ChangeDutyCycle(5.9)
    TiltServo.ChangeDutyCycle(9)
    sleep(0.1)
    PanServo.ChangeDutyCycle(0)
    TiltServo.ChangeDutyCycle(0)

def cleanup():
    GPIO.cleanup()
