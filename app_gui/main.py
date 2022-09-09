# Use pyqt5 to create a GUI for the app
# the GUI should have three buttons that open new windows
# the first button should open a new window from another class
# the second button should open a new window from another class
# the third button should open a new window from another class

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

from app_gui import device_list, configure_device_window, window3

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 App'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.button1 = QPushButton('Open Window 1', self)
        self.button1.move(20, 20)
        self.button1.clicked.connect(self.on_click1)

        self.button2 = QPushButton('Open Window 2', self)
        self.button2.move(20, 60)
        self.button2.clicked.connect(self.on_click2)

        self.button3 = QPushButton('Open Window 3', self)
        self.button3.move(20, 100)
        self.button3.clicked.connect(self.on_click3)

        self.show()

    def on_click1(self):
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




