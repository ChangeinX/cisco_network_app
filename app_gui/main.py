# Use pyqt5 to create a GUI for the app
# the GUI should have three buttons that open new windows
# the first button should open a new window from another class
# the second button should open a new window from another class
# the third button should open a new window from another class

import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSizePolicy

from app_gui import device_list, configure_device_window, window3

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'App'
        # window size is 860x480
        self.left = 10
        self.top = 10
        self.width = 860
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.button1 = QPushButton('View Devices', self)
        self.button1.clicked.connect(self.view_device_click)
        self.button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.button2 = QPushButton('Configure Device', self)
        self.button2.clicked.connect(self.on_click2)
        self.button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.button3 = QPushButton('Configure Orion', self)
        self.button3.clicked.connect(self.on_click3)
        self.button3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.button1.move(0, 0)
        self.button2.move(0, 160)
        self.button3.move(0, 320)

        self.button1.resize(860, 160)
        self.button2.resize(860, 160)
        self.button3.resize(860, 160)
        # style the window
        self.setStyleSheet("background-color: #2d2d2d; color: #f0f0f0")
        self.button1.setStyleSheet("background-color: #3d3d3d; color: #f0f0f0")
        self.button2.setStyleSheet("background-color: #3d3d3d; color: #f0f0f0")
        self.button3.setStyleSheet("background-color: #3d3d3d; color: #f0f0f0")
        # make button text large and bold
        self.button1.setStyleSheet("font: 30pt")
        self.button2.setStyleSheet("font: 30pt")
        self.button3.setStyleSheet("font: 30pt")


        self.show()

    def view_device_click(self):
        self.w = device_list.DeviceList()
        self.w.show()

    def on_click2(self):
        self.w = window2.Window2()
        self.w.show()

    def on_click3(self):
        self.w = window3.Window3()
        self.w.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())




