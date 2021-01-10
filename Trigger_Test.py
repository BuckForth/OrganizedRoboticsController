import RobotLibrary as RL
import time
from picamera import PiCamera
from adafruit_servokit import ServoKit

camera = PiCamera()

trigger_robot = RL.RoBoi()
trigger_robot.printStructure()
trigger_robot.initialize()
time.sleep(5)
trigger_robot.disengage()
print("end")