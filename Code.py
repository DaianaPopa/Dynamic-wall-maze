#region VEXcode Generated Robot Configuration
import math
import random
from vexcode_vr import *

# Brain should be defined by default
brain=Brain()

drivetrain = Drivetrain("drivetrain", 0)
pen = Pen("pen", 8)
pen.set_pen_width(THIN)
left_bumper = Bumper("leftBumper", 2)
right_bumper = Bumper("rightBumper", 3)
front_eye = EyeSensor("frontEye", 4)
down_eye = EyeSensor("downEye", 5)
front_distance = Distance("frontdistance", 6)
distance = front_distance
magnet = Electromagnet("magnet", 7)
location = Location("location", 9)

#endregion VEXcode Generated Robot Configuration
# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       Daiana A. P. Popa
#	Created:
#	Description:  VEXcode VR Python Project
# 
# ------------------------------------------

# Add project code in "main"
def main():
   pen.set_pen_color_rgb(12, 148, 16, 100)
   pen.move(DOWN)
   drivetrain.set_drive_velocity(100, PERCENT)
   drivetrain.set_turn_velocity(100, PERCENT)
   
   while not down_eye.detect(RED):
       #and front_distance.get_distance(MM) < 3000
       if front_distance.get_distance(MM) > 250:
           drivetrain.drive_for(FORWARD, 250, MM)
           drivetrain.turn_for(LEFT, 90, DEGREES)
       else:
           drivetrain.turn_for(RIGHT, 90, DEGREES)
   wait(3, SECONDS)

   drivetrain.turn_for(RIGHT, 90, DEGREES)
   pen.set_pen_color_rgb(255, 0, 0, 100)
   

   while not (location.position(X, MM)>=115 and location.position(X, MM)<=145 and location.position(Y,MM)>=-915 and location.position(Y,MM)<=-885):
       if front_distance.get_distance(MM) > 250:
           drivetrain.drive_for(FORWARD, 250, MM)
           drivetrain.turn_for(RIGHT, 90, DEGREES)
       else:
           drivetrain.turn_for(LEFT, 90, DEGREES)
   wait(3, SECONDS)
  


# VR threads — Do not delete
vr_thread(main)
