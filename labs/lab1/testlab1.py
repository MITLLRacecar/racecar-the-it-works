"""
Copyright MIT and Harvey Mudd College
MIT License
Summer 2020

Lab 1 - Driving in Shapes
"""

########################################################################################
# Imports
########################################################################################

import sys

sys.path.insert(1, "../../library")
import racecar_core
import racecar_utils as rc_utils

########################################################################################
# Global variables
########################################################################################

rc = racecar_core.create_racecar()


# Put any global variables here

counter = 0
isDrivingB = False
isDrivingX = False
isDrivingY = False

########################################################################################
# Functions
########################################################################################


def start():
    """
    This function is run once every time the start button is pressed
    """
    global counter
    global isDrivingB
    global isDrivingX
    global isDrivingY

    counter = 0
    isDrivingB = False

    # Begin at a full stop
    rc.drive.stop()

    # Print start message
    # TODO (main challenge): add a line explaining what the Y button does
    print(
        ">> Lab 1 - Driving in Shapes\n"
        "\n"
        "Controls:\n"
        "    Right trigger = accelerate forward\n"
        "    Left trigger = accelerate backward\n"
        "    Left joystick = turn front wheels\n"
        "    A button = drive in a circle\n"
        "    B button = drive in a square\n"
        "    X button = drive in a figure eight\n"
    )


def update():
    """
    After start() is run, this function is run every frame until the back button
    is pressed
    """
    global counter
    global isDrivingB
    global isDrivingX
    global isDrivingY

    # TODO (warmup): Implement acceleration and steering
    #rc.drive.set_speed_angle(0, 0)

    # TODO (main challenge): Drive in a circle

    if rc.controller.was_pressed(rc.controller.Button.A):
        
        rc.drive.set_speed_angle(1,1)
        
        

    # TODO (main challenge): Drive in a square when the B button is pressed

    if rc.controller.was_pressed(rc.controller.Button.B):

        print("Driving in a square...")
        counter = 0
        isDrivingX = False
        isDrivingY = False
        isDrivingB = True

    if isDrivingB:
        
        counter += rc.get_delta_time()

        if counter < 1:
            
            rc.drive.set_speed_angle(1, 0)

        elif counter < 2:
            
            rc.drive.set_speed_angle(1, -1)

        elif counter < 3:
            
            rc.drive.set_speed_angle(1, 0)

        elif counter < 4:
            
            rc.drive.set_speed_angle(1, -1)

        elif counter < 5:
            
            rc.drive.set_speed_angle(1, 0)

        elif counter < 6:
            
            rc.drive.set_speed_angle(1, -1)

        elif counter < 7:
            
            rc.drive.set_speed_angle(1, 0)

        else:
            
            rc.drive.stop()
            isDrivingB = False

    # TODO (main challenge): Drive in a figure eight when the X button is pressed

    if rc.controller.was_pressed(rc.controller.Button.X):

        counter = 0
        isDrivingB = False
        isDrivingY = False
        isDrivingX = True

    if isDrivingX:

        counter += rc.get_delta_time()


        if counter < 4:
           
            rc.drive.set_speed_angle(1, 1)

        elif counter < 7:
           
            rc.drive.set_speed_angle(1, -1)
     
        else:

            rc.drive.stop();
            isDrivingX = False
        


    # TODO (main challenge): Drives in a U-turn when the Y button
    # is pressed. However, the task allows for you to have the car 
    # drive in any shape of your choice.

    if rc.controller.was_pressed(rc.controller.Button.Y):
        counter = 0
        isDrivingB = False
        isDrivingX = False
        isDrivingY = True

    if isDrivingY:
        
        counter += rc.get_delta_time()

        if counter < 1:
           
            rc.drive.set_speed_angle(1, 0)

        elif counter < 3:
            
            rc.drive.set_speed_angle(1, -1)

        elif counter < 4:

            rc.drive.set_speed_angle(1, -1)

        elif counter < 5:

            rc.drive.set_speed_angle(1, 0)

        else:
            
            rc.drive.stop()
            isDrivingY = False
        


########################################################################################
# DO NOT MODIFY: Register start and update and begin execution
########################################################################################

if __name__ == "__main__":
    rc.set_start_update(start, update)
    rc.go()
