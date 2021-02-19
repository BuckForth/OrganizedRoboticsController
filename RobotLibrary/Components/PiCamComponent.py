from picamera.array import PiRGBArray
from picamera import PiCamera
from RobotLibrary.Components.Component import Component as Component
#Definition of PiCam controller
    #Measures angle from flat
class piCamComponent(Component):
    def __init__(self, label = "botNode",parent = None, robot = None, resolution = (320, 240), framerate = 30):
        super(piCamComponent, self).__init__(label = label, parent = parent, robot = robot)
        self.camera = None
        self.rawCapture = None
        self.resolution = resolution
        self.framerate = framerate
    
    def engage(self, robot):
        super(piCamComponent, self).engage(robot)
        self.camera = PiCamera()
        self.camera.resolution = self.resolution
        self.camera.framerate = self.framerate
        self.rawCapture = PiRGBArray(self.camera, size=(640,480))
        self.stream = self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True)
        self.frame = None
        time.sleep(0.1)

        
    def disengage(self, robot):
        super(piCamComponent, self).disengage(robot)
        self.camera.close()        

    def getData(self):
        super(piCamComponent, self).getData()
        time.sleep(0.1)
        #use_video_port=True)
        self.camera.capture(self.rawCapture, format="bgr")
        image = self.rawCapture.array
        self.rawCapture.truncate(0)
        
        return 