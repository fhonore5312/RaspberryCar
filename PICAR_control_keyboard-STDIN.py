# Imports
import sys, tty, termios, time
import PICAR_controller
from time import sleep

# The getch method can determine which key has been pressed by the user on the keyboard by accessing the system files
# It will then return the pressed key as a variable

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


# Infinite loop that will not end until the user presses the exit key

while True:
    # Keyboard character retrieval method is called and saved into variable
    char = getch()

    # The car will go left when the "k" key is pressed
    if(char == "k"):
        PICAR_controller.Motor1_left()
        sleep(0.2)

    # The car will go right when the "m" key is pressed
    if(char == "m"):
        PICAR_controller.Motor1_right()
        sleep(0.2)

    # The car will go forward when the "r" key is pressed
    if(char == "r"):
        PICAR_controller.Motor2_forward()
        sleep(0.2)

    # The car will go forward when the "r" key is pressed
    if(char == "f"):
        PICAR_controller.Motor2_backward()
        sleep(0.2)

    PICAR_controller.stop()
    # The "x" key will break the loop and exit the program
    if(char == "x"):
        print("Program Ended")
        PICAR_controller.cleanup()
        break

    # At the end of each loop the acceleration motor will stop
    # and wait for its next command
    # Motor1.ChangeDutyCycle(0)
    # Motor2.ChangeDutyCycle(0)

    # The keyboard character variable will be set to blank, ready
    # to save the next key that is pressed
    char = ""