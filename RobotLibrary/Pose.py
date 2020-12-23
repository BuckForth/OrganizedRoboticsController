import pickle

class Pose:
    def __init__ (self, poseData = []):
        self.poseData = poseData
    
    def loadFromFile(self, fileName = "/pose.rps"):
        with open(fileName, 'rb') as input:
            self.poseData = pickle.load(input).poseData
    
    def writeToFile(self, fileName = "/pose.rps"):
        with open(fileName, 'wb') as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)
        