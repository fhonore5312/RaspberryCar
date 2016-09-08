import PICAR_controller
from time import sleep

# turn left
PICAR_controller.Motor1_left()
sleep (1)
PICAR_controller.stop()

# turn right
PICAR_controller.Motor1_right()
sleep (1)
PICAR_controller.stop()

# go forward
PICAR_controller.Motor2_forward()
sleep (1)
PICAR_controller.stop()

# go backward
PICAR_controller.Motor2_backward()
sleep (1)
PICAR_controller.stop()

PICAR_controller.cleanup()


