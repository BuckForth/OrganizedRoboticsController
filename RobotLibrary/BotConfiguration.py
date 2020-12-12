import tkinter as tk
from tkinter import *     
     
def create_widget(bot_node):
    spinbox = Spinbox(from_=-180, to=180, increment=0.5)
    spinbox.pack()


robot = Robot(self, servoKits = None, refreshRate = 60)
create_widget(None)
app.mainloop()