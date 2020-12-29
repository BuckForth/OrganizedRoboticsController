import RobotLibrary as RL
import time
from adafruit_servokit import ServoKit



trigger_robot = RL.RoBoi()
trigger_robot.printStructure()
trigger_robot.root.loud = True

trigger_robot.initializeServos()
time.sleep(4)
trigger_robot.disengage()
print("end")