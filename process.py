import pyautogui
import keyboard
import json
import time


class compInputCapture:
  def __init__(self):
    self.TIME_delay = 0.01
    self.state_mouse = False
    
  def capMouseVel(self):
    x1,y1 = pyautogui.position()
    time.sleep(self.TIME_delay)
    x2,y2 = pyautogui.position()
    xvel = abs(x2 - x1) / self.TIME_delay
    yvel = abs(y2 - y1) / self.TIME_delay
    
    if abs(xvel + yvel) == 0:
      self.state_mouse = True
      return self.state_mouse
    
    self.state_mouse = False

  
  def keyboardCapture(self):
    pass
  
  
  
def _runProc(permissions): # permissions should be a dictionary
  print("Hello world!")