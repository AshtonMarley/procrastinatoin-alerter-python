import json
import os
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QCheckBox, QFileDialog, QMessageBox, QGridLayout, QSlider
)
from PyQt6.QtCore import Qt
import colors
import multiprocessing
import main_process


SETTINGS_FILE = "settings.json"


class MainWindow(QWidget):
  def __init__(self):
    super().__init__()
    # define the positions for the settings box
    self.title_row =          1
    self.keyboard_watch_row = 2
    self.mouse_watch_row =    3
    self.screen_watch_row =   4
    self.confirm_button_row = 5
    self.cancel_button_row =  6
    
    self.default_col =        0
    self.align_center =       Qt.AlignmentFlag.AlignCenter # position flag
    

    # default setup for window
    self.title =         "Settings Panel"
    self.window_width =  200
    self.window_height = 200
    
    self.setWindowTitle(self.title)
    self.setFixedSize(self.window_width, self.window_height)
    
    self.layout_main = QVBoxLayout()
    self.setLayout(self.layout_main)
    self.settingsBox()


    self.checkbox_not_checked = False

    self.color_library = colors.bcolors()


  def start_separate_process(self):
    main_process.main()



  def preload_settings(self):
    # check if settings file exists
    if os.path.exists(SETTINGS_FILE):
      with open(SETTINGS_FILE, "r") as f:
        self.data_json = json.load(f)
        print()

        self.status_keyboard = self.data_json['keyboard_watch']
        self.status_mouse =    self.data_json['mouse_watch']
        self.status_screen =   self.data_json['screen_watch']

        self.watch_keyboard.setChecked(self.status_keyboard)
        self.watch_mouse.setChecked(self.status_mouse)
        self.watch_screen.setChecked(self.status_screen)
        print(f"[ {self.color_library.OKGREEN}LOADED ]: pre existing settings from file: {SETTINGS_FILE} {self.color_library.ENDC}")
    else:
      print("No Existing Settings file... IGNORE")
    
  def apply_changes(self):
    # get the states of the checkboxes
    self.checkbox_state_keyboard = self.watch_keyboard.isChecked()
    self.checkbox_state_mouse    = self.watch_mouse.isChecked()
    self.checkbox_state_screen   = self.watch_screen.isChecked()
    
    data = {
      "keyboard_watch": self.checkbox_state_keyboard,
      "mouse_watch":    self.checkbox_state_mouse,
      "screen_watch":   self.checkbox_state_screen
    }
    
    try:
      with open("settings.json", "w") as f:
        json.dump(data, f, indent = 4)
    except OSError:
      print(f"{self.color_library.FAIL} COULD NOT OPEN FILE: {SETTINGS_FILE} {self.color_library.ENDC}")
  
  def clear_settings(self):
    self.watch_keyboard.setChecked(self.checkbox_not_checked)
    self.watch_mouse.setChecked(self.checkbox_not_checked)
    self.watch_screen.setChecked(self.checkbox_not_checked)
    
  def settingsBox(self):
    """
    _summary_
    
    this will be the settings window
    
    it will go as follow
    setting:
      check box
      slider (for the sensitivity)
      
    and then all the way at the bottom there will be a time delay for how often the program goes off
    
    """
    
    
    layout_vertical = QVBoxLayout() # setup the layout for vertical
    label_title =     QLabel("Settings Panel")
    self.watch_keyboard =  QCheckBox("Keyboard Listen")
    self.watch_mouse =     QCheckBox("Mouse Listen")
    self.watch_screen =    QCheckBox("Screen Listen")

    # title for the intensitybar
    self.title_intensity_bar = QLabel("Intensity")
    self.intensity_bar =   QSlider(orientation=Qt.Orientation.Horizontal)
    self.intensity_bar.setMinimum(0)
    self.intensity_bar.setMaximum(100)


    
    layout_vertical.addWidget(label_title)
    layout_vertical.addWidget(self.watch_keyboard)
    layout_vertical.addWidget(self.watch_mouse)
    layout_vertical.addWidget(self.watch_screen)
    layout_vertical.addWidget(self.intensity_bar)
    
    
    layout_horizontal = QHBoxLayout()
    button_confirm =    QPushButton("Apply")
    button_cancel =     QPushButton("Cancel")
    layout_horizontal.addWidget(button_confirm)
    layout_horizontal.addWidget(button_cancel)

    
    self.layout_main.addLayout(layout_vertical)
    self.layout_main.addLayout(layout_horizontal)
  
  
    button_confirm.clicked.connect(self.apply_changes)
    button_cancel.clicked.connect(self.clear_settings)
    self.preload_settings()

    

def main():
  #os.system("clear")
  app = QApplication([])
  w = MainWindow()
  w.show()
  app.exec()
 

if __name__ == "__main__":
    main()
