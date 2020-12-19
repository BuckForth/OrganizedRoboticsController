import RobotLibrary as RL
import time
from adafruit_servokit import ServoKit

trigger_robot = RL.RoBoi()
trigger_robot.printStructure()
trigger_robot.initializeServos()
trigger_robot.getNode("Hip_Y_Left").moveAngle(180, 10)

time.sleep(5)

trigger_robot.disengage()