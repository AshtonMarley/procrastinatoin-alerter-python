import pyautogui
import keyboard
import json
import time
import colors


class input_capture:
  def __init__(self):
    self.TIME_delay = 0.01
    self.state_mouse = False


    # colors main color 
    self.color_library = colors.bcolors()
    
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
  
  def test_function(self):
    print(f"{self.color_library.OKGREEN} MAIN PROCESS RUNNNING {self.color_library.ENDC}")
  
  
def main():
  main_function = input_capture()
  main_function.test_function()