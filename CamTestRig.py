import RobotLibrary

import time
import cv2

res = (320, 240)
fr = 30
testTime = 5


#Initializes test robot (Cam -> HeadPitch -> Neck_Pan)
testComponent = RobotLibrary.Components.piCamComponent(label = "testCam", resolution = res, framerate = fr)
testRobot = RobotLibrary.Robot(10, testComponent)
testRobot.root.addChild(RobotLibrary.Servo_Node(label = "Head_Pitch", kitAddress = 0x41, servoID = 15, restPos = 90))
testRobot.getNode("Head_Pitch").addChild(RobotLibrary.Servo_Node(label = "Neck_Pan", restPos = 90))
testRobot.printStructure(full = True)
testRobot.engage()
time.sleep(0.1)
startTime = time.time()

# capture frames from the camera
while (time.time() < startTime + testTime):
    image = testRobot.root.getData()
    image = cv2.rotate(image, cv2.cv2.ROTATE_180)
    cv2.imshow("Frame", image)

testRobot.disengage()
print ("Done")