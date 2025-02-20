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

# Add project code in "main"
def main():
   pen.set_pen_color_rgb(12, 148, 16, 100)
   pen.move(DOWN)
   drivetrain.set_drive_velocity(100, PERCENT)
   drivetrain.set_turn_velocity(100, PERCENT)
   onStart = True
   onFinish = False

   
   while not onFinish:
      #check the whole, to not get out from maze
       if onStart == True and front_distance.get_distance(MM) >= 3000:
           drivetrain.turn_for(RIGHT, 90, DEGREES)
       elif front_distance.get_distance(MM) > 250:
           drivetrain.drive_for(FORWARD, 250, MM)
           drivetrain.turn_for(LEFT, 90, DEGREES)
       else:
           drivetrain.turn_for(RIGHT, 90, DEGREES)

      #check if he is on start or finish
       if location.position(X, MM)>=115 and location.position(X, MM)<=145 and location.position(Y,MM)>=-915 and location.position(Y,MM)<=-885:
           onStart = True
       else:
           onStart = False

       if location.position(X, MM)>=-135 and location.position(X, MM)<=-115 and location.position(Y,MM)>=845 and location.position(Y,MM)<=875:
           onFinish = True
       else:
           onFinish = False

       wait(10,MSEC)
   
   wait(3, SECONDS)
   onFinish = True

   drivetrain.turn_for(LEFT, 90, DEGREES)
   pen.set_pen_color_rgb(255, 0, 0, 100)
   

   while not onStart:
       if front_distance.get_distance(MM) >= 3000 and onFinish == False:
           drivetrain.drive_for(FORWARD, 250, MM)
           drivetrain.turn_for(LEFT, 90, DEGREES)
       elif front_distance.get_distance(MM) > 250:
           drivetrain.drive_for(FORWARD, 250, MM)
           drivetrain.turn_for(LEFT, 90, DEGREES)
       else:
            drivetrain.turn_for(RIGHT, 90, DEGREES)
           
    #again check location
       if location.position(X, MM)>=115 and location.position(X, MM)<=145 and location.position(Y,MM)>=-915 and location.position(Y,MM)<=-885:
           onStart = True
       else:
           onStart = False

       if location.position(X, MM)>=-135 and location.position(X, MM)<=-115 and location.position(Y,MM)>=845 and location.position(Y,MM)<=875:
           onFinish = True
       else:
           onFinish = False
       wait(10,MSEC)   

   wait(3, SECONDS)
  


# VR threads — Do not delete
vr_thread(main)
