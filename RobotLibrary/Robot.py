import threading
import time
import sys

class Robot:
    #Robot class for robot control
    def __init__(self, refreshRate = 50, root = None):
        self.root = root
        if (root is not None):
            self.root.robot = self
        self.frequency = refreshRate
        self.lastUpdate = None
        self.ctrlThread = None
        self.logMode = 3
        
    def orcDriver(self):
        self.active = True
        while self.active:
            if (self.lastUpdate is None):
                self.lastUpdate = time.time()
            nodes = self.root.getList()
            for node in nodes:
                nodeDeltaTime = time.time() - self.lastUpdate
                node.updateStep(deltaTime = nodeDeltaTime)
            sleepDelay = ((1.0/self.frequency) - (time.time() - self.lastUpdate)) #Total time slice - used time
            if (sleepDelay < 0):
                nSkip = int(sleepDelay / (-1.0/self.frequency) + 1)
                sleepDelay = sleepDelay + (nSkip * (1.0/self.frequency))
                self.log("Bot state update unable to keep up.({:f}s/{:f}s)\n\tSkipping {:d} frame(s)\n".format(time.time() - self.lastUpdate,(1.0/self.frequency),nSkip),2)
                sys.stdout.flush()
            self.lastUpdate = time.time()
            time.sleep(sleepDelay)
    
    def initialize(self):
        nodes = self.root.getList()
        for node in nodes:
            node.initialize(self)
        self.ctrlThread  = threading.Thread(target=self.orcDriver, daemon=True)
        self.ctrlThread.start()
        
    def disengage(self):
        self.active = False
        self.ctrlThread.join()
        
    def getNode(self, nodeName):
        return self.root.getNode(nodeName)
    
    def getNodeList(self):
        return self.root.getList()
    
    def log(self, string, priority = 0):
        # 0 : Debug (hidden by default)
        # 1 : Message
        # 2 : Warning
        # 3 : Error
        if (priority >= self.logMode):
            print(string)
        
    def printStructure(self, full = False):
        self.root.printStructure(0,full)