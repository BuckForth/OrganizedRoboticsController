import RobotLibrary
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
         
class PoseEditor:
    def updateNodes(self, event):
        for sliderNode in self.sliderNodes:
            val = sliderNode[0].get()
            sliderNode[1].moveAngle(val, self.robotAdjustSpeed)
            
    def nodeName(self, node):
        return node.label
    
    def poseNodeName(self, node):
        rVal = ""
        if (node.parent is not None):
            rVal += self.poseNodeName(node.parent) + ':'
        rVal += node.label
        return rVal
            
    def writePose(self):
        filename = filedialog.asksaveasfilename(initialdir = self.workingDir,
                                                filetypes=[("Pose Files","*.rps")])
        pose = RobotLibrary.Pose()
        for node in self.nodes:
            poseNodeLabel = self.poseNodeName(node)
            pose.poseData.append([poseNodeLabel, node.destinationPos])
            pose.writeToFile(filename)
            
    def loadPose(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="open File",
                                              filetypes=[("Pose Files","*.rps")])
        pose = RobotLibrary.Pose()
        pose.loadFromFile(fileName = filename)
        for nodeAngle in pose.poseData:
            nodePath = nodeAngle[0]
            angle = nodeAngle[1]
            for sliderNode in self.sliderNodes:
                sliderNodePath = self.poseNodeName(sliderNode[1])
                if (sliderNodePath == nodePath):
                    slider = sliderNode[0]
                    Node = sliderNode[1]
                    slider.set(angle)
                    Node.moveAngle(angle,self.robotAdjustSpeed)
            
        
    def __init__(self, root, lastOpenedDir):
        root.title("Configure Bot Nodes")
        self.robotAdjustSpeed = 360
#Generate/Load Bot
        self.robot = RobotLibrary.RoBoi()
        self.nodes = self.robot.getNodeList()
        #self.nodes.sort(key = self.nodeName)
        self.activeBotNode = self.robot.root
        self.sliderNodes = []
        self.workingDir = lastOpenedDir
#Build UI
        ii = 0
        coloumCount = 3
        for node in self.nodes:
            frame = Frame(root)
            ttk.Label(frame, text = node.label).grid(column = 0, row = 0)
            slider = Scale(frame, from_=0, to=node.actuation_range, orient=HORIZONTAL, command = self.updateNodes, length = 160)
            slider.set(node.restPos)
            slider.grid(column = 1, row = 0)
            frame.grid(column = ii % coloumCount, row = 1 + (ii // coloumCount))
            self.sliderNodes.append([slider,node])
            ii = ii + 1
        
        writePosButton = Button(root, text = "Save Pose", command = self.writePose)
        writePosButton.grid(column = 0, row = 0)
        loadPosButton = Button(root, text = "Load Pose", command = self.loadPose)
        loadPosButton.grid(column = coloumCount - 1, row = 0)
        self.robot.initializeServos()
    

        

        

root = Tk()
PoseEditor(root, "/")
root.mainloop()

