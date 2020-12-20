import RobotLibrary as RL
import time
from adafruit_servokit import ServoKit


kit1 = ServoKit(channels = 16, address=0x40)
kit1.frequency = 50
kit2 = ServoKit(channels = 16, address=0x41)
kit2.frequency = 50
    
#trigger_robot = RL.Robot(name = "RoBOI (0.2)",servoKits = [kit1,kit2], frequency = 50)
trigger_robot = RL.RoBoi()
#trigger_robot.root = RL.Bot_Node(label = "hip1", robot = trigger_robot, servoID = 1, restPos = 45)
#trigger_robot.getNode("hip1").addChild(   label = "hip2",  servoID = 2, restPos = 15)
#trigger_robot.getNode("hip2").addChild(   label = "hip3",  servoID = 3, restPos = 110)
trigger_robot.printStructure()
#robot.getNode("Hip_Y_Left").addChild( label = "Hip_Z_Left",  servoID = 2, restPos = 30)
#robot.getNode("Hip_Z_Left").addChild( label = "Hip_X_Left",  servoID = 3)
#robot.getNode("Hip_X_Left").addChild( label = "Knee_X_Left", servoID = 4)
#robot.getNode("Knee_X_Left").addChild(label = "Foot_Z_Left", servoID = 5)
#robot.getNode("Foot_Z_Left").addChild(label = "Foot_X_Left", servoID = 6)

trigger_robot.initializeServos()
time.sleep(5)
trigger_robot.disengage()
print("end")