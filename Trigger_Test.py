import RobotLibrary as RL
import time
from picamera import PiCamera
from adafruit_servokit import ServoKit

camera = PiCamera()

# trigger_robot = RL.RoBoi()
# trigger_robot.printStructure()
camera.start_preview()
# trigger_robot.initializeServos()
time.sleep(10)
camera.stop_preview()
# trigger_robot.disengage()
print("end")