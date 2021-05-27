import RobotLibrary as RL
from RobotLibrary.BotConfiguration import *
import time
from picamera import PiCamera
from adafruit_servokit import ServoKit

camera = PiCamera()

trigger_robot = RL.RoBoi()
trigger_robot.printStructure(full = True)
    

pullStructure(trigger_robot)
    

print("end")