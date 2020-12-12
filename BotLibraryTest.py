import RobotLibrary
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
         
class NodeEditor:
    def __init__(self, root):
        root.title("Configure Bot Nodes")
        root.geometry("640x240")
#Generate/Load Bot
        self.robot = RobotLibrary.RoBoi()
        self.nodes = self.robot.getNodeList()
        self.activeBotNode = self.robot.root
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
        self.nodeView.column("#0", width=240, minwidth=240)
        self.nodeView.heading("#0",text="ServoNode", anchor=tk.W)
        self.nodeView.place(x=0, y=0, relheight = 1.0, height = -31, relwidth = 1.0, width = -15)

        for node in self.nodes:
            if node.parent is None:
                self.nodeView.insert('', "end", node.label, text = node.label)
            else:
                self.nodeView.insert(node.parent.label, "end", node.label, text = node.label)
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
        #Form Entries
        self.botNode = tk.StringVar()
        self.kitID = tk.StringVar()
        self.servoID = tk.StringVar()
        self.restPos = tk.StringVar()
        self.offset = tk.StringVar()
        self.actuation = tk.StringVar()
        self.mirror = tk.StringVar()
        
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

        #Bind update functionallity to NodeViewer
        self.nodeView.bind("<Double-1>", self.populateForm)
    
    def populateForm(self, event):
        item =  self.nodeView.identify('item',event.x,event.y)
        self.activeBotNode = self.robot.getNode(self.nodeView.item(item,"text"))
        
        self.botNodeEntry.delete(0,END)
        self.botNodeEntry.insert(0,self.activeBotNode.label)
        
        self.kitIDEntry.delete(0,END)
        self.kitIDEntry.insert(0,str(self.activeBotNode.kitID))
        
        self.servoIDEntry.delete(0,END)
        self.servoIDEntry.insert(0,str(self.activeBotNode.servoID))
        
        self.restPosEntry.delete(0,END)
        self.restPosEntry.insert(0,str(self.activeBotNode.restPos))
        
        self.offsetEntry.delete(0,END)
        self.offsetEntry.insert(0,str(self.activeBotNode.offset))
        
        self.actuationEntry.delete(0,END)
        self.actuationEntry.insert(0,str(self.activeBotNode.actuation_range))
        
        self.mirrorEntry.delete(0,END)
        self.mirrorEntry.insert(0,str(self.activeBotNode.mirror))

        
        
root = Tk()
NodeEditor(root)
root.mainloop()

