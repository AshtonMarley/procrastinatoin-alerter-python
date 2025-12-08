import json
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QCheckBox, QFileDialog, QMessageBox
)
from PyQt6.QtCore import Qt


SETTINGS_FILE = "settings.json"



class MainWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.title = "Settings Panel"
    self.setWindowTitle(self.title)
    self.setGeometry(100, 100, 800, 800)
    
    self.layout = QHBoxLayout()
    self.setLayout(self.layout)
    
    
    self.settingsBox()
    
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
    # make the label
    title = QLabel("Mouse Tracker", self)
    
    self.layout.addWidget(title)
    
    

def main():
    app = QApplication([])
    w = MainWindow()
    w.show()
    app.exec()


if __name__ == "__main__":
    main()
