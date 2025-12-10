import json
import os
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QCheckBox, QFileDialog, QMessageBox, QGridLayout
)
from PyQt6.QtCore import Qt



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
    
    
  def apply_changes(self):
    # get the states of the checkboxes
    self.checkbox_state_keyboard = self.watch_keyboard.checkState()
    self.checkbox_state_mouse    = self.watch_mouse.checkState()
    self.checkbox_state_screen   = self.watch_screen.checkState()
    
    data = {
      "keyboard_watch": str(self.checkbox_state_keyboard),
      "mouse_watch": str(self.checkbox_state_mouse),
      "screen_watch": str(self.checkbox_state_screen)
    }
    
    with open("settings.json", "w") as f:
      json.dump(data, f, indent = 4)
  
  def clear_settings(self):
    pass
    
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
    
    layout_vertical.addWidget(label_title)
    layout_vertical.addWidget(self.watch_keyboard)
    layout_vertical.addWidget(self.watch_mouse)
    layout_vertical.addWidget(self.watch_screen)
    
    
    layout_horizontal = QHBoxLayout()
    button_confirm =    QPushButton("Apply")
    button_cancel =     QPushButton("Cancel")
    layout_horizontal.addWidget(button_confirm)
    layout_horizontal.addWidget(button_cancel)

    
    self.layout_main.addLayout(layout_vertical)
    self.layout_main.addLayout(layout_horizontal)
  
  
    button_confirm.clicked.connect(self.apply_changes)
    button_cancel.clicked.connect(self.clear_settings)
    

def main():
  os.system("clear")
  app = QApplication([])
  w = MainWindow()
  w.show()
  app.exec()


if __name__ == "__main__":
    main()
