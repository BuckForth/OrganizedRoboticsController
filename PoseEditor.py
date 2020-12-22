import RobotLibrary
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
         
class NodeEditor:
    def updateNodes(self, event):
        for sliderNode in self.sliderNodes:
            val = sliderNode[0].get()
            sliderNode[1].moveAngle(val, self.robotAdjustSpeed)
            
            
    def __init__(self, root):
        root.title("Configure Bot Nodes")
        self.robotAdjustSpeed = 360
#Generate/Load Bot
        self.robot = RobotLibrary.RoBoi()
        self.nodes = self.robot.getNodeList()
        self.activeBotNode = self.robot.root
        self.sliderNodes = []
#Build UI
        ii = 0
        coloumCount = 3
        for node in self.nodes:
            frame = Frame(root)
            ttk.Label(frame, text = node.label).grid(column = 0, row = 0)
            slider = Scale(frame, from_=0, to=node.actuation_range, orient=HORIZONTAL, command = self.updateNodes, length = 160)
            slider.set(node.restPos)
            slider.grid(column = 1, row = 0)
            frame.grid(column = ii % coloumCount, row = ii // 4)
            self.sliderNodes.append([slider,node])
            ii = ii + 1
        
        self.robot.initializeServos()
    

        

        

root = Tk()
NodeEditor(root)
root.mainloop()

