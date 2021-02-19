import smbus
import math
import time
from RobotLibrary.Components.Component import Component as Component

#Definition of GY_521 Gyroscope sensor
    #Measures angle from top of unit
class Sensor_GY_521(Component): 
    """Node class for the bot structure"""
    def __init__(self, label = "botNode",parent = None, robot = None):
        super(Sensor_GY_521, self).__init__(label = label, parent = parent, robot = robot)
        self.power_mgmt_1 = 0x6b
        self.power_mgmt_2 = 0x6c
        
        self.bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
        self.address = 0x68       # via i2cdetect
        
        self.label = label
        self.parent = parent
        self.children = []
        if robot is None and parent is not None:
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
    
    def printNode(self, depth = 0, full = False):
        super(Sensor_GY_521, self).printNode(depth, full)
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
            print (" - "*depth + "|-> X Rotation:" , self.get_x_rotation(gy_521_xout_skaliert, gy_521_yout_skaliert, gy_521_zout_skaliert))
            print (" - "*depth + "|-> Y Rotation:" , self.get_y_rotation(gy_521_xout_skaliert, gy_521_yout_skaliert, gy_521_zout_skaliert))
    
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