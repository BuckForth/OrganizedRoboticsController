from adafruit_servokit import ServoKit
import smbus
import math
import time
from RobotLibrary.Components.Component import Component as Component

#Definition of Servo BotNode Joint
    #Rotates along axis
class Servo_Node(Component):
    """Node class for the bot structure"""
    def __init__(self, label = "botNode",parent = None, kitAddress = 0x40, 
    servoID = 0, restPos = 0.0, robot = None, actuation_range = 180, mirror = False):
        super(Servo_Node, self).__init__(label = label, parent = parent, robot = robot)
        #init Servokit PMW
        self.robot = robot
        self.servoKit = None
        self.kitAddress = kitAddress
        try:
            self.servoKit = ServoKit(channels = 16, address=kitAddress)
            self.servoKit.frequency = 50
        except Exception as e:
            self.robot.log("An error occurred defining servo kit\n" + str(e),3)
            return
        self.servoID = servoID
        self.restPos = restPos
        self.actuation_range = actuation_range
        self.currentPos = self.restPos
        if (self.currentPos < 0):
            self.currentPos = 0
        if (self.currentPos > self.actuation_range):
            node.currentPos = self.actuation_range
        self.destinationPos = self.currentPos
        self.offset = 0.0
        self.speed = 0.0
        self.mirror = mirror
        return
                  
    def moveAngle(self, angle, speed):
        if angle >= 0 and angle <= self.actuation_range:
            self.speed = speed
            self.destinationPos = angle
            if self.mirror:
                self.destinationPos = self.actuation_range - self.destinationPos
        else:
            print("Cannot move to angle:" + angle);
            print("\tAngle must fall withing range: 0, " + self.acactuation_range);
        return self
    
    def updateStep(self, deltaTime):
        super().updateStep(deltaTime)
        if (self.robot is not None and self.servoKit is not None):
            #self.currentPos = self.robot.servoKits[self.kitID].servo[self.servoID].angle
            if (self.currentPos < 0):
                self.currentPos = 0
            if (self.currentPos > self.actuation_range):
                self.currentPos = self.actuation_range
            diff = self.destinationPos - self.currentPos
            maxStep = self.speed * deltaTime
            step = maxStep
            if diff < 0:
                step *= -1.0
            if abs(diff) < abs(maxStep):
                step = diff
            self.currentPos += step
            self.servoKit.servo[self.servoID].angle = self.currentPos
            #print("Angle update")
        else:
            cause = "\t"
            if self.robot is None:
                cause += "Robot not assigned or properly initialized"
            if self.servoKit is None:
                cause += "servoKit not defined or initialized"
            self.robot.log("Error occured updating node '" + self.label + "'\n" + cause, 3)
    
    def printNode(self, depth = 0, full = False):
        super(Servo_Node, self).printNode(depth, full)
        if full:
            print (" - "*depth + "|-> ServoID       : " + str(self.servoID))
            print (" - "*depth + "|-> I2CAddress    : " + str(self.kitAddress))
            print (" - "*depth + "|-> restPos       : " + str(self.restPos))
            print (" - "*depth + "|-> offset        : " + str(self.offset))
            print (" - "*depth + "|-> actuationRange: " + str(self.actuation_range))
#----------------END OF SERVO_NODE---------------------#