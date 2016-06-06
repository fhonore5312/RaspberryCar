# Imports
import RPi.GPIO as GPIO
import sys, tty, termios, time

# Initialisation
GPIO.setmode(GPIO.BCM)

# These two blocks of code configure the PWM settings for the two DC motors on the Raspberry car.
# It defines the two GPIO pins used for the input, starts the PWM and sets the motors' speed to 0

# Configuration of Motor1, motor for direction: going left / going right
# On declare les ports qui permettent de piloter le Moteur1 depuis la puce electronique 293
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

# Configuration of Motor2, motor : going forwards / going backwards
# on declare les ports qui permettent de piloter le Moteur1 depuis la puce electronique 293
Motor2E = 21
Motor2A = 16
Motor2B = 20
# On indique que ces ports sont pilotés depuis le raspberry et sont des ports de sortie
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)
# Instruction qui permet d'indiquer que l'on va utiliser 100% de la puissance moteur
Motor2 = GPIO.PWM(Motor2E, 100)
# On force la vitesse à 0
Motor2.start(0)

# The getch method can determine which key has been pressed by the user on the keyboard by accessing the system files
# It will then return the pressed key as a variable

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
        sys.stdin.
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


# This section of code defines the methods used to determine whether a motor needs to spin forward or backwards. The
# different directions are acheived by setting one of the  GPIO pins to true and the other to false.

def Motor1_left():
    GPIO.output(Motor1A, True)
    GPIO.output(Motor1B, False)

def Motor1_right():
    GPIO.output(Motor1A, False)
    GPIO.output(Motor1B, True)

def Motor2_forward():
    GPIO.output(Motor2A, True)
    GPIO.output(Motor2B, False)

def Motor2_backward():
    GPIO.output(Motor2A, False)
    GPIO.output(Motor2B, True)

# Infinite loop that will not end until the user presses the exit key

while True:
    # Keyboard character retrieval method is called and saved into variable
    char = getch()

    # The car will go left when the "k" key is pressed
    if(char == "k"):
        Motor1_left()
        Motor1.ChangeDutyCycle(99)

    # The car will go right when the "m" key is pressed
    if(char == "m"):
        Motor1_right()
        Motor1.ChangeDutyCycle(99)

    # The car will go forward when the "r" key is pressed
    if(char == "r"):
        Motor2_forward()
        Motor2.ChangeDutyCycle(99)

    # The car will go forward when the "r" key is pressed
    if(char == "f"):
        Motor2_backward()
        Motor2.ChangeDutyCycle(99)

    # The "a" key will toggle the steering left
    #if(char == "a"):
    #    toggleSteering("left")

    # The "d" key will toggle the steering right
    #if(char == "d"):
    #     toggleSteering("right")


    # The "x" key will break the loop and exit the program
    if(char == "x"):
        print("Program Ended")
        break

    # At the end of each loop the acceleration motor will stop
    # and wait for its next command
    # Motor1.ChangeDutyCycle(0)
    # Motor2.ChangeDutyCycle(0)

    # The keyboard character variable will be set to blank, ready
    # to save the next key that is pressed
    char = ""

# Program will cease all GPIO activity before terminating
GPIO.cleanup()
