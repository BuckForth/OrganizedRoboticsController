import RobotLibrary as RL
from RobotLibrary.BotConfiguration import *
import time
from picamera import PiCamera
from adafruit_servokit import ServoKit

camera = PiCamera()

trigger_robot = RL.RoBoi()
trigger_robot.printStructure(full = True)
    
trigger_robot.engage()

trigger_robot.getNode("Neck_Pan").moveAngle(90, 1000)

time.sleep(1)

trigger_robot.getNode("Neck_Pan").moveAngle(10, 1000)

time.sleep(1)

trigger_robot.getNode("Neck_Pan").moveAngle(170, 1000)

time.sleep(1)

trigger_robot.disengage()

print("end")