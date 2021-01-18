import RobotLibrary
import time
import tkinter as tk
import pickle
from PoseEditor import PoseEditor
from pathlib import Path
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class orcEditConfig:
    def __init__(self):
        self.lastRobotConfigPath = "/"
        self.robotConfigCache = None
        self.lastRobotPosePath = "/"
        
    def writeConfig(self, filename):
        with open(fileName, 'rb') as input:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)
        
            
    def loadConfig(self, filename):
        with open(fileName, 'rb') as input:
            loadedData = pickle.load(input).lastRobotConfigPath
            self.lastRobotConfigPath = loadedData.lastRobotConfigPath
            self.robotConfigCache = loadedData.robotConfigCache
            self.lastRobotPosePath = loadedData.lastRobotPosePath
        
        
    
class orcEdit:
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
    
    def nodeEditorForms(self, frame):
        #Build UI
        hierarchyFrame = ttk.Frame(root, width = (root.winfo_width())-16)
        hierarchyFrame.pack(side="left", fill = "both")
        nodeFrame = ttk.Frame(root)
        nodeFrame.pack(side="right")
# Creating Node hierarchy window         
        ttk.Label(hierarchyFrame, text ="Hierarchy").pack()
        self.nodeView = ttk.Treeview(hierarchyFrame)
        vsb = ttk.Scrollbar(hierarchyFrame, orient="vertical", command=self.nodeView.yview)
        vsb.place(relx = 1, x = -15, y=0, relheight = 1.0, height = -15)
        hsb = ttk.Scrollbar(hierarchyFrame, orient="horizontal", command=self.nodeView.xview)
        hsb.place(rely = 1, y = -15, x=0, relwidth = 1.0)
        
        self.nodeView.configure(yscrollcommand=vsb.set)
        self.nodeView.configure(xscrollcommand=hsb.set)
        self.nodeView.column("#0", stretch = True)
        self.nodeView.heading("#0",text="ServoNode", anchor=tk.W)
        self.nodeView.place(x=0, y=0, relheight = 1.0, height = -31, relwidth = 1.0, width = -15)
        self.nodeView.pack(side="left", fill = "y")
   
# Create NodeData
        #Form Labels
        nodenameLabel = ttk.Label(nodeFrame, text = "Node Label").grid(
            column = 0, row = 0, sticky = "e")
        kitIDLabel = ttk.Label(nodeFrame, text = "Kit ID").grid(
            column = 0, row = 1, sticky = "e")
        servoIDLabel = ttk.Label(nodeFrame, text = "Servo ID").grid(
            column = 0, row = 2, sticky = "e")
        restPosLabel = ttk.Label(nodeFrame, text = "Rest Pos").grid(
            column = 0, row = 3, sticky = "e")
        offsetLabel = ttk.Label(nodeFrame, text = "Servo Offset").grid(
            column = 0, row = 4, sticky = "e")
        actuationLabel = ttk.Label(nodeFrame, text = "Actuation Range").grid(
            column = 0, row = 5, sticky = "e")
        mirrorLabel = ttk.Label(nodeFrame, text = "Mirror").grid(
            column = 0, row = 6, sticky = "e")
        #Form Entries Vars
        self.botNode = tk.StringVar()
        self.kitID = tk.StringVar()
        self.servoID = tk.StringVar()
        self.restPos = tk.StringVar()
        self.offset = tk.StringVar()
        self.actuation = tk.StringVar()
        self.mirror = tk.StringVar()
        #Form Objects
        self.botNodeEntry = ttk.Entry(nodeFrame,   textvariable = self.botNode)
        self.botNodeEntry.grid(          column = 1, row = 0)
        self.kitIDEntry = ttk.Entry(nodeFrame,     textvariable = self.kitID)
        self.kitIDEntry.grid(            column = 1, row = 1)
        self.servoIDEntry = ttk.Entry(nodeFrame,   textvariable = self.servoID)
        self.servoIDEntry.grid(          column = 1, row = 2)
        self.restPosEntry = ttk.Entry(nodeFrame,   textvariable = self.restPos)
        self.restPosEntry.grid(          column = 1, row = 3)
        self.offsetEntry = ttk.Entry(nodeFrame,    textvariable = self.offset)
        self.offsetEntry.grid(           column = 1, row = 4)
        self.actuationEntry = ttk.Entry(nodeFrame, textvariable = self.actuation)
        self.actuationEntry.grid(        column = 1, row = 5)
        self.mirrorEntry = ttk.Entry(nodeFrame,    textvariable = self.mirror)
        self.mirrorEntry.grid(           column = 1, row = 6)
        
        nodeSaveButton = ttk.Button(nodeFrame, text ="Save Node", command = self.updateNodeView)
        nodeSaveButton.grid(column = 0, row = 7, sticky = "e")

        
        newNodeButton = ttk.Button(nodeFrame, text ="Add Child")
        newNodeButton.grid(column = 1, row = 7, sticky = "w")
        #Bind functionallity to objects
        self.nodeView.bind("<1>", self.populateForm)
        #Load tree
        self.initForm()
        self.updateNodeView()
    #End of nodeEditorForms()
       
       
    def __init__(self, root, lastOpenedDir):
        root.title("Robot Editor")
        self.robotAdjustSpeed = 360
#Generate/Load Bot
        self.robot = RobotLibrary.RoBoi()
        self.nodes = self.robot.getNodeList()
        #self.nodes.sort(key = self.nodeName)
        self.activeBotNode = self.robot.root
        self.sliderNodes = []
        self.workingDir = lastOpenedDir
        self.robot.root.loud = True
#Build UI
        #SetRootNotebook
        self.topleveltabs = ttk.Notebook(root)

        nodeEditorTab = ttk.Frame(self.topleveltabs)
        self.nodeEditorForms(nodeEditorTab)
        poseEditorTab = ttk.Frame(self.topleveltabs)
        PoseEditor.PoseEditor(poseEditorTab)
        self.topleveltabs.add(nodeEditorTab, text = "Configuration")
        self.topleveltabs.add(poseEditorTab, text = "Poses")
        
        self.topleveltabs.pack(expand = 1, fill = 'both')
        
    def populateNodeForm(self, event):
        item =  self.nodeView.identify('item',event.x,event.y)
        if self.activeBotNode is not None and self.robot.getNode(self.nodeView.item(item,"text")) is not None:
            self.activeBotNode = self.robot.getNode(self.nodeView.item(item,"text"))
            self.botNode.set(self.activeBotNode.label)
            self.kitID.set(str(self.activeBotNode.kitID))
            self.servoID.set(str(self.activeBotNode.servoID))
            self.restPos.set(str(self.activeBotNode.restPos))
            self.offset.set(str(self.activeBotNode.offset))
            self.actuation.set(str(self.activeBotNode.actuation_range))
            self.mirror.set(str(self.activeBotNode.mirror))
        
    def initForm(self):
        self.activeBotNode = self.robot.root
        self.botNode.set(self.activeBotNode.label)
        self.kitID.set(str(self.activeBotNode.kitID))
        self.servoID.set(str(self.activeBotNode.servoID))
        self.restPos.set(str(self.activeBotNode.restPos))
        self.offset.set(str(self.activeBotNode.offset))
        self.actuation.set(str(self.activeBotNode.actuation_range))
        self.mirror.set(str(self.activeBotNode.mirror))

    def updateNodeView(self):
        if self.activeBotNode is not None:
            self.activeBotNode.label = self.botNode.get()       
            self.activeBotNode.kitID = int(self.kitID.get())
            self.activeBotNode.servoID = int(self.servoID.get())
            self.activeBotNode.restPos = float(self.restPos.get())
            self.activeBotNode.offset = float(self.offset.get())
            self.activeBotNode.actuation_range = float(self.actuation.get())
            self.activeBotNode.mirror = bool(self.mirror.get())
            self.nodeView.delete(*self.nodeView.get_children())
            for node in self.nodes:
                if node.parent is None:
                    self.nodeView.insert('', "end", node.label, text = node.label)
                else:
                    self.nodeView.insert(node.parent.label, "end", node.label, text = node.label)
            
        
        
        
root = Tk()
editor = orcEdit(root, "/")
root.mainloop()
editor.robot.disengage()
print("Program Ended")
