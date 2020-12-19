import RobotLibrary.Bot_Node
import RobotLibrary.Robot
from adafruit_servokit import ServoKit
from RobotLibrary.Robot import Robot as Robot
from RobotLibrary.Bot_Node import Bot_Node as Bot_Node

def RoBoi() -> Robot:
    print("Generating RoBOI (0.1) control structure")
    kit1 = None
    try:
        kit1 = ServoKit(channels = 16, address=0x40)
    except:
        print("An error occurred defining left servo kit")
    kit2 = None
    try:
        kit2 = ServoKit(channels = 16, address=0x41)
    except:
        print("An error occurred defining right servo kit")
        
    servoKits = [kit1,kit2]
    robot = Robot(name = "RoBOI (0.1)",servoKits = servoKits)
    #Head and Neck roots
    robot.root = Bot_Node(label = "Head_Pitch", robot = robot)
    robot.root.addChild(label = "Neck_Pan", kitID = 1, servoID = 0)
    #Left leg
    robot.getNode("Neck_Pan").addChild(   label = "Hip_Y_Left",  servoID = 1)
    robot.getNode("Hip_Y_Left").addChild( label = "Hip_Z_Left",  servoID = 2)
    robot.getNode("Hip_Z_Left").addChild( label = "Hip_X_Left",  servoID = 3)
    robot.getNode("Hip_X_Left").addChild( label = "Knee_X_Left", servoID = 4)
    robot.getNode("Knee_X_Left").addChild(label = "Foot_Z_Left", servoID = 5)
    robot.getNode("Foot_Z_Left").addChild(label = "Foot_X_Left", servoID = 6)
    #Right leg
    robot.getNode("Neck_Pan").addChild(    label = "Hip_Y_Right",   kitID = 1, servoID = 1)
    robot.getNode("Hip_Y_Right").addChild( label = "Hip_Z_Right",   kitID = 1, servoID = 2)
    robot.getNode("Hip_Z_Right").addChild( label = "Hip_X_Right",   kitID = 1, servoID = 3)
    robot.getNode("Hip_X_Right").addChild( label = "Knee_X_Right",  kitID = 1, servoID = 4)
    robot.getNode("Knee_X_Right").addChild(label = "Foot_Z_Right",  kitID = 1, servoID = 5)
    robot.getNode("Foot_Z_Right").addChild(label = "Foot_X_Right",  kitID = 1, servoID = 6)
    #Left arm
    robot.getNode("Neck_Pan").addChild(         label = "Shoulder_X_Left",  servoID = 7)
    robot.getNode("Shoulder_X_Left").addChild(  label = "Shoulder_Z_Left",  servoID = 8)
    robot.getNode("Shoulder_Z_Left").addChild(  label = "Shoulder_Y_Left",  servoID = 9)
    robot.getNode("Shoulder_Y_Left").addChild(  label = "Elbow_X_Left",     servoID = 10)
    robot.getNode("Elbow_X_Left").addChild(     label = "Wrist_Y_Left",     servoID = 11)
    robot.getNode("Wrist_Y_Left").addChild(     label = "Finger_1_Left",    servoID = 12)
    robot.getNode("Wrist_Y_Left").addChild(     label = "Finger_2_Left",    servoID = 13)
    robot.getNode("Wrist_Y_Left").addChild(     label = "Thumb_Rotate_Left",servoID = 14)
    robot.getNode("Thumb_Rotate_Left").addChild(label = "Thumb_1_Left",     servoID = 15)
    #Right arm
    robot.getNode("Neck_Pan").addChild(          label = "Shoulder_X_Right",  kitID = 1, servoID = 7)
    robot.getNode("Shoulder_X_Right").addChild(  label = "Shoulder_Z_Right",  kitID = 1, servoID = 8)
    robot.getNode("Shoulder_Z_Right").addChild(  label = "Shoulder_Y_Right",  kitID = 1, servoID = 9)
    robot.getNode("Shoulder_Y_Right").addChild(  label = "Elbow_X_Right",     kitID = 1, servoID = 10)
    robot.getNode("Elbow_X_Right").addChild(     label = "Wrist_Y_Right",     kitID = 1, servoID = 11)
    robot.getNode("Wrist_Y_Right").addChild(     label = "Finger_1_Right",    kitID = 1, servoID = 12)
    robot.getNode("Wrist_Y_Right").addChild(     label = "Finger_2_Right",    kitID = 1, servoID = 13)
    robot.getNode("Wrist_Y_Right").addChild(     label = "Thumb_Rotate_Right",kitID = 1, servoID = 14)
    robot.getNode("Thumb_Rotate_Right").addChild(label = "Thumb_1_Right",     kitID = 1, servoID = 15)
    return robot