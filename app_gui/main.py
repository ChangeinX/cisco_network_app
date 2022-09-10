# Use pyqt5 to create a GUI for the app
# the GUI should have three buttons that open new windows
# the first button should open a new window from another class
# the second button should open a new window from another class
# the third button should open a new window from another class

import sys

import setuptools.package_index
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSizePolicy, QLineEdit

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

        self.btn_view_devices = QPushButton('View Devices', self)
        self.btn_view_devices.clicked.connect(self.view_device_click)
        self.btn_view_devices.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.btn_configure_devices = QPushButton('Configure Device', self)
        self.btn_configure_devices.clicked.connect(self.config_device_click)
        self.btn_configure_devices.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.btn_config_orion = QPushButton('Configure Orion', self)
        self.btn_config_orion.clicked.connect(self.config_orion_click)
        self.btn_config_orion.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.btn_view_devices.move(10, 0)
        self.btn_configure_devices.move(10, 160)
        self.btn_config_orion.move(10, 320)

        self.btn_view_devices.resize(430, 80)
        self.btn_configure_devices.resize(430, 80)
        self.btn_config_orion.resize(430, 80)
        # style the window
        self.setStyleSheet("background-color: #2d2d2d; color: #f0f0f0")
        self.btn_view_devices.setStyleSheet("background-color: #3d3d3d; color: #f0f0f0")
        self.btn_configure_devices.setStyleSheet("background-color: #3d3d3d; color: #f0f0f0")
        self.btn_config_orion.setStyleSheet("background-color: #3d3d3d; color: #f0f0f0")
        # make button text large and bold
        self.btn_view_devices.setStyleSheet("font: 30pt")
        self.btn_configure_devices.setStyleSheet("font: 30pt")
        self.btn_config_orion.setStyleSheet("font: 30pt")

        # input fields for username and password on the right of the buttons with space in between
        self.username = QLineEdit(self)
        # make space between the buttons and the input fields
        self.username.move(480, 60)
        self.username.resize(300, 50)
        self.username.setStyleSheet("background-color: #3d3d3d; color: #f0f0f0")
        self.username.setFont(QFont('Arial', 30))
        self.username.setPlaceholderText("Username")

        # make password appear as dots
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.move(480, 150)
        self.password.resize(300, 50)
        self.password.setStyleSheet("background-color: #3d3d3d; color: #f0f0f0")
        self.password.setFont(QFont('Arial', 30))
        self.password.setPlaceholderText("Password")

        # login button
        self.btn_login = QPushButton('Login', self)
        self.btn_login.clicked.connect(self.login_click)
        self.btn_login.move(480, 240)
        self.btn_login.resize(300, 50)
        self.btn_login.setFont(QFont('Arial', 30))
        # make the login button appear 3D
        self.btn_login.setStyleSheet(
            "border-style: outset; border-width: 2px; border-radius: 10px; border-color: beige; font: bold 14px; "
            "min-width: 10em; padding: 6px;"
        )
        # disable the buttons until the user logs in
        self.btn_view_devices.setEnabled(False)
        self.btn_configure_devices.setEnabled(False)
        self.btn_config_orion.setEnabled(False)

        # allow user to tab between input fields
        self.username.setTabOrder(self.username, self.password)
        self.password.setTabOrder(self.password, self.btn_login)
        self.btn_login.setTabOrder(self.btn_login, self.username)

        # set focus to username input field
        self.username.setFocus()

        # allow user to press enter to log in
        self.username.returnPressed.connect(self.btn_login.click)
        self.password.returnPressed.connect(self.btn_login.click)

        self.show()

    def view_device_click(self):
        self.w = device_list.DeviceList()
        self.w.show()

    def config_device_click(self):
        self.w = window2.Window2()
        self.w.show()

    def config_orion_click(self):
        self.w = window3.Window3()
        self.w.show()

    def login_click(self):
        # check if username and password are correct
        # if they are correct, open the main window
        # if they are incorrect, show an error message
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())




