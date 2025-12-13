import pyautogui
import keyboard
import json
import time
import os
import sys
import ctypes
import console_logs


class input_capture:
  def __init__(self):
    self.TIME_delay = 0.2
    self.state_mouse = False

    
  def capture_mouse_velocity(self):
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
    console_logs.Logs.success("main process running")

  
  
def main():
  main_function = input_capture()

  while True:
    print(main_function.capture_mouse_velocity())