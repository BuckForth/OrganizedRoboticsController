import RobotLibrary as RL
import time
from adafruit_servokit import ServoKit


kit1 = ServoKit(channels = 16, address=0x40)
kit1.frequency = 50
kit2 = ServoKit(channels = 16, address=0x41)
kit2.frequency = 50
    
trigger_robot = RL.RoBoi()


trigger_robot.initializeServos()
time.sleep(1)
trigger_robot.getNode("Shoulder_Z_Right").moveAngle(0,60)
time.sleep(4)
trigger_robot.getNode("Shoulder_Z_Right").moveAngle(140,240)
time.sleep(4)
trigger_robot.getNode("Shoulder_Z_Right").moveAngle(60,360)
time.sleep(4)
trigger_robot.disengage()
print("end")