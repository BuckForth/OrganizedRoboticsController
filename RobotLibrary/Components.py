#import Robot
import smbus
import math

#Standard Bot_Node Structural Component
class Component:
    """Node class for the bot structure"""
    def __init__(self, label = "botNode", parent = None, robot = None):
        self.label = label
        self.parent = parent
        self.children = []
        if robot is None and parent is not None:
            self.robot = parent.robot
        else:
            self.robot = robot
    
    def initialize(self, robot):
        robot.log("initialized component %s as:\n\t%s"%(self.label,str(type(self))))
    
    def setData(self, data):
        self.robot.log("Setting component %s(%s) data to %s(%s)" % (self.label,str(type(self)),str(data),str(type(data))))
    
    def updateStep(self, deltaTime):
        self.robot.log("Updating component %s(%s) after %.4f(secs)" % (self.label,str(type(self)),deltaTime))
    
    def addChild(self, child):
        child.parent = self
        child.robot = self.robot
        self.children.append(child);
        return child
    
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
#----------------END OF BOT_NODE---------------------#


#Definition of Servo BotNode Joint
    #Rotates along axis
class Servo_Node(Component):
    """Node class for the bot structure"""
    def __init__(self, label = "botNode",parent = None, kitID = 0, 
    servoID = 0, restPos = 0.0, robot = None, actuation_range = 180, mirror = False):
        super().__init__(label = label, parent = parent)
        self.kitID = kitID
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
        super(deltaTime)
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
#----------------END OF SERVO_NODE---------------------#       
        
        
#Definition of GY_521 Gyroscope sensor
    #Measures angle from flat
class Sensor_GY_521(Component): 
    """Node class for the bot structure"""
    def __init__(self, label = "botNode",parent = None, robot = None):
        self.power_mgmt_1 = 0x6b
        self.power_mgmt_2 = 0x6c
        
        self.bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
        self.address = 0x68       # via i2cdetect
        
        self.label = label
        self.parent = parent
        self.children = []
        if robot is None:
            self.robot = parent.robot
        else:
            self.robot = robot
        self.loud = False
    
    def updateStep(self, deltaTime):
        self.bus.write_byte_data(self.address, self.power_mgmt_1, 0)
        gyroskop_xout = self.read_word_2c(0x43)
        gyroskop_yout = self.read_word_2c(0x45)
        gyroskop_zout = self.read_word_2c(0x47)
        gy_521_xout = self.read_word_2c(0x3b)
        gy_521_yout = self.read_word_2c(0x3d)
        gy_521_zout = self.read_word_2c(0x3f)
        gy_521_xout_skaliert = gy_521_xout / 16384.0
        gy_521_yout_skaliert = gy_521_yout / 16384.0
        gy_521_zout_skaliert = gy_521_zout / 16384.0
        if (self.loud):
            print ("X Rotation:" , self.get_x_rotation(gy_521_xout_skaliert, gy_521_yout_skaliert, gy_521_zout_skaliert))
            print ("Y Rotation:" , self.get_y_rotation(gy_521_xout_skaliert, gy_521_yout_skaliert, gy_521_zout_skaliert))
    
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
            self.bus.write_byte_data(self.address, self.power_mgmt_1, 0)
            gyroskop_xout = self.read_word_2c(0x43)
            gyroskop_yout = self.read_word_2c(0x45)
            gyroskop_zout = self.read_word_2c(0x47)
            gy_521_xout = self.read_word_2c(0x3b)
            gy_521_yout = self.read_word_2c(0x3d)
            gy_521_zout = self.read_word_2c(0x3f)
            gy_521_xout_skaliert = gy_521_xout / 16384.0
            gy_521_yout_skaliert = gy_521_yout / 16384.0
            gy_521_zout_skaliert = gy_521_zout / 16384.0
            if self.parent is None:
                print (" - "*depth + "|-> Parent        : None")
            else:
                print (" - "*depth + "|-> Parent        : " + self.parent.label)
            print (" - "*depth + "|-> X Rotation:" , self.get_x_rotation(gy_521_xout_skaliert, gy_521_yout_skaliert, gy_521_zout_skaliert))
            print (" - "*depth + "|-> Y Rotation:" , self.get_y_rotation(gy_521_xout_skaliert, gy_521_yout_skaliert, gy_521_zout_skaliert))
    
        
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
    
    def read_byte(self, reg):
        return self.bus.read_byte_data(self.address, reg)
 
    def read_word(self, reg):
        h = self.bus.read_byte_data(self.address, reg)
        l = self.bus.read_byte_data(self.address, reg+1)
        value = (h << 8) + l
        return value
 
    def read_word_2c(self, reg):
        val = self.read_word(reg)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val
 
    def dist(self, a,b):
        return math.sqrt((a*a)+(b*b))
 
    def get_y_rotation(self, x,y,z):
        radians = math.atan2(x, self.dist(y,z))
        return -math.degrees(radians)
 
    def get_x_rotation(self, x,y,z):
        radians = math.atan2(y, self.dist(x,z))
        return math.degrees(radians)