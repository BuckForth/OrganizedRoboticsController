import RobotLibrary.Robot2
import RobotLibrary.Pose
from adafruit_servokit import ServoKit
from RobotLibrary.Robot2 import Robot as Robot
from RobotLibrary.Pose import Pose as Pose
from RobotLibrary.Components2 import Component as Bot_Node
from RobotLibrary.Components2 import Servo_Node as Servo_Node
from RobotLibrary.Components2 import Sensor_GY_521 as GY_521

def RoBoi() -> Robot:
    print("Primitive: RoBOI (0.3a) -> control structure")
    kit1 = None
    try:
        kit1 = ServoKit(channels = 16, address=0x40)
        kit1.frequency = 50
    except Exception as e:
        print("An error occurred defining left servo kit\n" + str(e))
    kit2 = None
    try:
        kit2 = ServoKit(channels = 16, address=0x41)
        kit2.frequency = 50
    except Exception as e:
        print("An error occurred defining right servo kit\n" + str(e))
    servoKits = [kit1,kit2]
    robot = Robot(50)
    #Head and Neck roots
    
    robot.root = GY_521(label = "Root_Gyro", robot = robot)
    robot.root.addChild(Servo_Node(label = "Neck_Pan", kitID = 1, servoID = 15, restPos = 90))
    robot.getNode("Neck_Pan").addChild(Servo_Node(label = "Head_Pitch"))
    #Left leg
    robot.getNode("Root_Gyro").addChild(Servo_Node(label = "Hip_Y_Left",  servoID = 1, restPos = 45))
    robot.getNode("Hip_Y_Left").addChild(Servo_Node(label = "Hip_Z_Left",  servoID = 2, restPos = 15))
    robot.getNode("Hip_Z_Left").addChild(Servo_Node(label = "Hip_X_Left",  servoID = 3, restPos = 130))
    robot.getNode("Hip_X_Left").addChild(Servo_Node(label = "Knee_X_Left", servoID = 4, restPos = 160))
    robot.getNode("Knee_X_Left").addChild(Servo_Node(label = "Foot_Z_Left", servoID = 5, restPos = 75))
    robot.getNode("Foot_Z_Left").addChild(Servo_Node(label = "Foot_X_Left", servoID = 6, restPos = 20))
    #Right leg
    robot.getNode("Root_Gyro").addChild(Servo_Node(   label = "Hip_Y_Right",   kitID = 1, servoID = 14, restPos = 125))
    robot.getNode("Hip_Y_Right").addChild(Servo_Node(label = "Hip_Z_Right",   kitID = 1, servoID = 13, restPos = 115))
    robot.getNode("Hip_Z_Right").addChild(Servo_Node(label = "Hip_X_Right",   kitID = 1, servoID = 12, restPos = 110))
    robot.getNode("Hip_X_Right").addChild(Servo_Node(label = "Knee_X_Right",  kitID = 1, servoID = 11, restPos = 30))
    robot.getNode("Knee_X_Right").addChild(Servo_Node(label = "Foot_Z_Right",  kitID = 1, servoID = 10, restPos = 105))
    robot.getNode("Foot_Z_Right").addChild(Servo_Node(label = "Foot_X_Right",  kitID = 1, servoID = 9 , restPos = 90))
    #Left arm
    robot.getNode("Root_Gyro").addChild(Servo_Node(       label = "Shoulder_X_Left",  servoID = 7,  restPos = 180))
    robot.getNode("Shoulder_X_Left").addChild(Servo_Node( label = "Shoulder_Z_Left",  servoID = 8,  restPos = 130))
    robot.getNode("Shoulder_Z_Left").addChild(Servo_Node( label = "Shoulder_Y_Left",  servoID = 9,  restPos = 90))
    robot.getNode("Shoulder_Y_Left").addChild(Servo_Node( label = "Elbow_X_Left",     servoID = 10, restPos = 60))
    #robot.getNode("Elbow_X_Left").addChild(Servo_Node(    label = "Wrist_Y_Left",     servoID = 11))
    #robot.getNode("Wrist_Y_Left").addChild(Servo_Node(    label = "Finger_1_Left",    servoID = 12))
    #robot.getNode("Wrist_Y_Left").addChild(Servo_Node(    label = "Finger_2_Left",    servoID = 13))
    #robot.getNode("Wrist_Y_Left").addChild(Servo_Node(    label = "Thumb_Rotate_Left",servoID = 14))
    #robot.getNode("Thumb_Rotate_Left").addChild(label = "Thumb_1_Left",     servoID = 15))
    #Right arm
    robot.getNode("Root_Gyro").addChild(Servo_Node(         label = "Shoulder_X_Right",  kitID = 1, servoID = 8, restPos = 0))
    robot.getNode("Shoulder_X_Right").addChild(Servo_Node( label = "Shoulder_Z_Right",  kitID = 1, servoID = 7, restPos = 135))
    robot.getNode("Shoulder_Z_Right").addChild(Servo_Node( label = "Shoulder_Y_Right",  kitID = 1, servoID = 6, restPos = 60))
    robot.getNode("Shoulder_Y_Right").addChild(Servo_Node( label = "Elbow_X_Right",     kitID = 1, servoID = 5, restPos = 100))
    #robot.getNode("Elbow_X_Right").addChild(Servo_Node(    label = "Wrist_Y_Right",     kitID = 1, servoID = 11))
    #robot.getNode("Wrist_Y_Right").addChild(Servo_Node(    label = "Finger_1_Right",    kitID = 1, servoID = 12))
    #robot.getNode("Wrist_Y_Right").addChild(Servo_Node(    label = "Finger_2_Right",    kitID = 1, servoID = 13))
    #robot.getNode("Wrist_Y_Right").addChild(Servo_Node(    label = "Thumb_Rotate_Right",kitID = 1, servoID = 14))
    #robot.getNode("Thumb_Rotate_Right").addChild(Servo_Node(label = "Thumb_1_Right",     kitID = 1, servoID = 15))
    return robot