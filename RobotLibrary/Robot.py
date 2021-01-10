import threading
import time

class Robot:
    #Robot class for robot control
    def __init__(self, refreshRate = 50, root = None):
        self.root = root
        self.frequency = refreshRate
        self.lastUpdate = None
        
    def orcDriver(self):
        self.active = True
        while self.active:
            if (lastUpdate == None):
                lastUpdate = time.time()
            nodes = self.root.getList()
            for node in nodes:
                nodeDeltaTime = time.time() - lastUpdate
                node.updateStep(deltaTime = nodeDeltaTime)
            NextUpdateFrame = lastUpdate + (1.0/frequency)
            sleepDelay = NextUpdateFrame - time.time()
            if (sleepDelay < 0):
                self.log("Bot state update unable to keep up.\n")
                nSkip = 0
                while (sleepDelay < 0):
                    sleepDelay + (1.0/frequency)
                    nSkip = nSkip + 1
                self.log("\tSkipping %d frame(s)")
            time.sleep(sleepDelay)
    
    def initialize(self):
        nodes = self.root.getList()
        for node in nodes:
            node.initialize(self)
        
    def disengage(self):
        self.active = False
        
    def getNode(self, nodeName):
        return self.root.getNode(nodeName)
    
    def getNodeList(self):
        return self.root.getList()
    
    def log(self, string):
        print(string)
        
    def printStructure(self, full = False):
        self.root.printStructure(0,full)