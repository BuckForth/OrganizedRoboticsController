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
    
    def initializeServos(self):
        kitCheck = True
        if len(self.servoKits) > 0:
            kitCheck += 0x01
        for kit in self.servoKits:
                if kit == None:
                    kitCheck = False
        if kitCheck:
            #Initialize Positions
            nodes = self.getNodeList()
              
            #Start servo update thread
            self.thread = threading.Thread(target=self.servoDriver_thread, daemon=True)
            self.thread.start()
        else:
            print("An error occurred initializing servo kits") 
        
    def disengage(self):
        self.active = False
        
    def getNode(self, nodeName):
        return self.root.getNode(nodeName)
    
    def getNodeList(self):
        return self.root.getList()
    
    def printStructure(self, full = False):
        self.root.printStructure(0,full)