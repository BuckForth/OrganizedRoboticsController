#import Robot

class Bot_Node:
    """Node class for the bot structure"""
    def __init__(self, label = "botNode",parent = None, kitID = 0, 
    servoID = 0, restPos = 0.0, robot = None, actuation_range = 180, mirror = False):
        self.label = label
        self.parent = parent
        self.children = []
        self.kitID = kitID
        self.servoID = servoID
        self.restPos = restPos
        self.currentPos = restPos
        self.destinationPos = restPos
        self.offset = 0.0
        self.speed = 0.0
        self.mirror = mirror
        self.actuation_range = actuation_range
        if robot is None:
            self.robot = parent.robot
        else:
            self.robot = robot
                  
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
        if (self.robot is not None and self.robot.servoKits is not None and
        len(self.robot.servoKits) > self.kitID and self.robot.servoKits[self.kitID] is not None):
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
            self.robot.servoKits[self.kitID].servo[self.servoID].angle = self.currentPos
            #print("Angle update")
        else:
            cause = "\t"
            if self.robot is not None:
                cause += "Robot servoKit not defined or initialized"
            if self.robot.servoKits is not None:
                cause += "Robot servoKit not defined or initialized"
            if len(self.robot.servoKits) < self.kitID:
                cause += "kitID outside bounds"
            if self.robot.servoKits[self.kitID] is None:
                cause += "kitID(" + str(self.kitID) + ") not available or initialized"
            print("Error occured updating node '" + self.label + "'\n" + cause)
    
    def addChild(self, label = "childNode", kitID = 0, servoID = 0, restPos = 0.0):
        newNode = Bot_Node(robot = self.robot, label = label, kitID = kitID,
                           servoID = servoID, parent = self, restPos = restPos)
        self.children.append(newNode);
        return newNode
    
    def printStructure(self, depth, full = False):
        self.printNode(depth = depth, full = full)
        if len(self.children) > 0:
            for child in self.children:
                child.printStructure(depth + 1, full)
                    
    def getList(self):
        rlist = [self]
        if len(self.children) > 0:
            for child in self.children:
                rlist.extend(child.getList())
        return rlist
    
    def printNode(self, depth = 0, full = False):
        print (" - "*depth + self.label)
        if full:
            if self.parent is None:
                print (" - "*depth + "|-> Parent        : None")
            else:
                print (" - "*depth + "|-> Parent        : " + self.parent.label)
            print (" - "*depth + "|-> ServoID       : " + str(self.servoID))
            print (" - "*depth + "|-> KitID         : " + str(self.kitID))
            print (" - "*depth + "|-> restPos       : " + str(self.restPos))
            print (" - "*depth + "|-> offset        : " + str(self.offset))
            print (" - "*depth + "|-> actuationRange: " + str(self.actuation_range))
        
    def getNode(self, nodeName):
        if self.label == nodeName:
            return self
        elif len(self.children) > 0:
            rVal = None
            found = False
            for child in self.children:
                if rVal == None:
                    rVal = child.getNode(nodeName)
                if rVal != None:
                    found = True
            return rVal
        else:
            return None