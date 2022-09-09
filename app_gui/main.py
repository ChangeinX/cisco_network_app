# Use pyqt5 to create a GUI for the app
# the GUI should have three buttons that open new windows
# the first button should open a new window from another class
# the second button should open a new window from another class
# the third button should open a new window from another class

# import the necessary modules
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


# create a class for the GUI
class App(QWidget):

    # create a method to initialize the GUI
    def __init__(self):
        # call the init method from the parent class
        super().__init__()
        # call the init method from the GUI class
        self.initUI()

    # create a method to initialize the GUI
    def initUI(self):
        # set the size of the window
        self.resize(300, 200)
        # set the position of the window
        self.move(300, 300)
        # set the title of the window
        self.setWindowTitle('App')
        # set the icon of the window
        self.setWindowIcon(QIcon('web.png'))

        # create a button to open a new window
        btn = QPushButton('Open Window', self)
        # set the position of the button
        btn.move(20, 20)
        # set the size of the button
        btn.resize(btn.sizeHint())
        # connect the button to the open_window method
        btn.clicked.connect(self.device_information)

        # create a button to open a new window
        btn = QPushButton('Open Window', self)
        # set the position of the button
        btn.move(20, 60)
        # set the size of the button
        btn.resize(btn.sizeHint())
        # connect the button to the open_window method
        btn.clicked.connect(self.device_information)

        # create a button to open a new window
        btn = QPushButton('Open Window', self)
        # set the position of the button
        btn.move(20, 100)
        # set the size of the button
        btn.resize(btn.sizeHint())
        # connect the button to the open_window method
        btn.clicked.connect(self.device_information)

        # create a button to exit the app
        btn = QPushButton('Exit', self)
        # set the position of the button
        btn.move(20, 140)
        # set the size of the button
        btn.resize(btn.sizeHint())
        # connect the button to the exit method
        btn.clicked.connect(QCoreApplication.instance().quit)

        # show the window
        self.show()

    # create a method to open the window for device information
    def device_information(self):
        # create a new window
        device_info = DeviceInfo()
        # show the new window
        device_info.show()

    # create a method to open the window for configuring devices
    def configure_devices(self):
        # create a new window
        configure_devices = ConfigureDevices()
        # show the new window
        configure_devices.show()

    # create a method to open the window for downloading configs
    def download_configs(self):
        # create a new window
        download_configs = DownloadConfigs()
        # show the new window
        download_configs.show()

    # create a method to configure Orion NPM
    def configure_orion_npm(self):
        # create a new window
        oriong_view = OrionView()
        # show the new window
        oriong_view.show()


# create a class for the new window
class DeviceInfo(QWidget):

    # create a method to initialize the new window
    def __init__(self):
        # call the init method from the parent class
        super().__init__()
        # call the init method from the new window class
        self.initUI()

    # create a method to initialize the new window
    def initUI(self):
        # set the size of the window
        self.resize(300, 200)
        # set the position of the window
        self.move(600, 300)
        # set the title of the window
        self.setWindowTitle('Window')
        # set the icon of the window
        self.setWindowIcon(QIcon('web.png'))

        # create a button to close the window
        btn = QPushButton('Close', self)
        # set the position of the button
        btn.move(20, 20)
        # set the size of the button
        btn.resize(btn.sizeHint())
        # connect the button to the close method
        btn.clicked.connect(self.close)

        # show the window
        self.show()


# create a class for the new window
class ConfigureDevices(QWidget):

    # create a method to initialize the new window
    def __init__(self):
        # call the init method from the parent class
        super().__init__()
        # call the init method from the new window class
        self.initUI()

    # create a method to initialize the new window
    def initUI(self):
        # set the size of the window
        self.resize(300, 200)
        # set the position of the window
        self.move(600, 300)
        # set the title of the window
        self.setWindowTitle('Window')
        # set the icon of the window
        self.setWindowIcon(QIcon('web.png'))

        # create a button to close the window
        btn = QPushButton('Close', self)
        # set the position of the button
        btn.move(20, 20)
        # set the size of the button
        btn.resize(btn.sizeHint())
        # connect the button to the close method
        btn.clicked.connect(self.close)

        # show the window
        self.show()


# create a class for the new window
class DownloadConfigs(QWidget):

    # create a method to initialize the new window
    def __init__(self):
        # call the init method from the parent class
        super().__init__()
        # call the init method from the new window class
        self.initUI()

    # create a method to initialize the new window
    def initUI(self):
        # set the size of the window
        self.resize(300, 200)
        # set the position of the window
        self.move(600, 300)
        # set the title of the window
        self.setWindowTitle('Window')
        # set the icon of the window
        self.setWindowIcon(QIcon('web.png'))

        # create a button to close the window
        btn = QPushButton('Close', self)
        # set the position of the button
        btn.move(20, 20)
        # set the size of the button
        btn.resize(btn.sizeHint())
        # connect the button to the close method
        btn.clicked.connect(self.close)

        # show the window
        self.show()


# create a class for the new window
class OrionView(QWidget):
    # create a method to initialize the new window
    def __init__(self):
        # call the init method from the parent class
        super().__init__()
        # call the init method from the new window class
        self.initUI()

    # create a method to initialize the new window
    def initUI(self):
        # set the size of the window
        self.resize(300, 200)
        # set the position of the window
        self.move(600, 300)
        # set the title of the window
        self.setWindowTitle('Window')
        # set the icon of the window
        self.setWindowIcon(QIcon('web.png'))

        # create a button to close the window
        btn = QPushButton('Close', self)
        # set the position of the button
        btn.move(20, 20)
        # set the size of the button
        btn.resize(btn.sizeHint())
        # connect the button to the close method
        btn.clicked.connect(self.close)

        # show the window
        self.show()


# create a method to run the app
def main():
    # create an instance of QApplication
    app = QApplication(sys.argv)
    # create an instance of the GUI class
    ex = App()
    # run the app
    sys.exit(app.exec_())


# run the app
if __name__ == '__main__':
    main()

