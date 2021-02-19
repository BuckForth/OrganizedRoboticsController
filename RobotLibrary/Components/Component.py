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
    
    def engage(self, robot):
        self.robot.log("initialized component %s as:\n\t%s"%(self.label,str(type(self))),0)
    
    def disengage(self, robot):
        self.robot.log("initialized component %s as:\n\t%s"%(self.label,str(type(self))),0)
    
    def setData(self, data):
        self.robot.log("Setting component %s(%s) data" % (self.label,str(type(self))),0)
    
    def getData(self):
        self.robot.log("Reading component %s(%s) data" % (self.label,str(type(self))),0)
    
    def updateStep(self, deltaTime):
        self.robot.log("Updating component %s(%s) after %.4f(secs)" % (self.label,str(type(self)),deltaTime),0)
    
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
        print (" - "*depth + "|-> Class         : " + str(type(self)))
        if full:
            if self.parent is None:
                print (" - "*depth + "|-> Parent        : None")
            else:
                print (" - "*depth + "|-> Parent        : " + self.parent.label)
        
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