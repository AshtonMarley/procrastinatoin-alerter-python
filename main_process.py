import pyautogui
import keyboard
import json
import time
import os
import sys
import ctypes
import console_logs
import multiprocessing


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

  
  def capture_keyboard(self):
    pass

  def capture_screen(self):
    pass
  
class read_settings:
  def __init__(self):
    self.SETTINGS_FILE = "settings.json"

  def open_file(self):
    if os.path.exists(self.SETTINGS_FILE):
      console_logs.Logs.success(f"{self.SETTINGS_FILE} located")
      with open(self.SETTINGS_FILE, "r")as file:
        data = json.load(file)
    
    return data


def main():
  loop_bool = True
  threads_active = []
  main_function =          input_capture()
  function_load_settings = read_settings()

  json_file_data = function_load_settings.open_file()
  func_keyboard = json_file_data['keyboard_watch']
  func_mouse = json_file_data['mouse_watch']
  func_screen = json_file_data['screen_watch']


  proc_keyboard = multiprocessing.Process(target=main_function.capture_keyboard)
  proc_mouse =    multiprocessing.Process(target=main_function.capture_mouse_velocity)
  proc_screen =    multiprocessing.Process(target=main_function.capture_screen)
  

  if func_keyboard:
    proc_keyboard.start()
  if func_mouse:
    proc_mouse.start()
  if func_screen:
    proc_screen.start()
