# Device window has two tables, one for routers and one for switches, and a dynamic search bar above the tables.


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QWidget, QTableWidget, QVBoxLayout, QAbstractItemView, \
    QHeaderView, QLineEdit, QHBoxLayout, QLabel, QPushButton


class DeviceList(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Device List'
        self.left = 10
        self.top = 10
        self.width = 860
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = QTableWidget()
        # row count is 0 because we will add rows dynamically
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(['Device Name', 'Location', 'IP Address'])
        # make header tables text black
        for i in range(self.table_widget.columnCount()):
            self.table_widget.horizontalHeaderItem(i).setForeground(QBrush(QColor(0, 0, 0)))
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_widget.itemClicked.connect(self.on_click)

        # add dynamic search bar above the table
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('Search')
        self.search_bar.textChanged.connect(self.search)

        # add label above the search bar
        self.search_label = QLabel('Search:')

        # add label above the table
        self.table_label = QLabel('Routers:')
        self.table_label.setStyleSheet('font-weight: bold;')
        # make the font larger
        font = self.table_label.font()
        font.setPointSize(14)
        self.table_label.setFont(font)
        # center the label
        self.table_label.setAlignment(Qt.AlignCenter)

        # add table for switches on the right side of the window
        self.table_widget2 = QTableWidget()
        # row count is 0 because we will add rows dynamically
        self.table_widget2.setRowCount(0)
        self.table_widget2.setColumnCount(3)
        self.table_widget2.setHorizontalHeaderLabels(['Device Name', 'Location', 'IP Address'])
        # make the horizontal header labels text black instead of white
        for i in range(self.table_widget2.columnCount()):
            self.table_widget2.horizontalHeaderItem(i).setForeground(QBrush(QColor(0, 0, 0)))

        self.table_widget2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget2.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_widget2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_widget2.itemClicked.connect(self.on_click)

        # add label above the table
        self.table_label2 = QLabel('Switches:')
        self.table_label2.setStyleSheet('font-weight: bold;')
        # make the font larger
        font = self.table_label2.font()
        font.setPointSize(14)
        self.table_label2.setFont(font)
        # center the label
        self.table_label2.setAlignment(Qt.AlignCenter)

        # four buttons for table 1
        self.button1 = QPushButton('Add')
        self.button2 = QPushButton('Edit')
        self.button3 = QPushButton('Delete')
        self.button4 = QPushButton('Download Config')

        # place buttons below table 1
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.button1)
        self.button_layout.addWidget(self.button2)
        self.button_layout.addWidget(self.button3)
        self.button_layout.addWidget(self.button4)

        # four buttons for table 2
        self.add_button2 = QPushButton('Add')
        self.edit_button2 = QPushButton('Edit')
        self.delete_button2 = QPushButton('Delete')
        self.download_button2 = QPushButton('Download Config')

        # place buttons below table 2
        self.button_layout2 = QHBoxLayout()
        self.button_layout2.addWidget(self.add_button2)
        self.button_layout2.addWidget(self.edit_button2)
        self.button_layout2.addWidget(self.delete_button2)
        self.button_layout2.addWidget(self.download_button2)

        # place table 1 and table 2 side by side
        self.table_layout = QHBoxLayout()
        self.table_layout.addWidget(self.table_widget)
        self.table_layout.addWidget(self.table_widget2)

        # place search bar above table 1
        self.search_layout = QHBoxLayout()
        self.search_layout.addWidget(self.search_label)
        self.search_layout.addWidget(self.search_bar)

        # add the search bar and table to the layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.search_label)
        self.layout.addWidget(self.search_bar)
        self.layout.addWidget(self.table_label)
        self.layout.addWidget(self.table_widget)
        self.layout.addLayout(self.button_layout)
        self.layout.addWidget(self.table_label2)
        self.layout.addWidget(self.table_widget2)
        self.layout.addLayout(self.button_layout2)
        self.setLayout(self.layout)

        # style the window for a nice blue look
        self.setStyleSheet("background-color: #2c3e50; color: #ecf0f1;")
        self.table_widget.setStyleSheet("background-color: #34495e; color: #ecf0f1;")
        self.table_widget2.setStyleSheet("background-color: #34495e; color: #ecf0f1;")
        self.search_bar.setStyleSheet("background-color: #34495e; color: #ecf0f1;")
        self.search_label.setStyleSheet("color: #ecf0f1;")
        self.table_label.setStyleSheet("color: #ecf0f1;")
        self.button1.setStyleSheet("background-color: #34495e; color: #ecf0f1;")
        self.button2.setStyleSheet("background-color: #34495e; color: #ecf0f1;")
        self.button3.setStyleSheet("background-color: #34495e; color: #ecf0f1;")
        self.button4.setStyleSheet("background-color: #34495e; color: #ecf0f1;")
        self.add_button2.setStyleSheet("background-color: #34495e; color: #ecf0f1;")
        self.edit_button2.setStyleSheet("background-color: #34495e; color: #ecf0f1;")
        self.delete_button2.setStyleSheet("background-color: #34495e; color: #ecf0f1;")
        self.download_button2.setStyleSheet("background-color: #34495e; color: #ecf0f1;")
        self.table_label2.setStyleSheet("color: #ecf0f1;")
        self.table_widget2.setStyleSheet("background-color: #34495e; color: #ecf0f1;")
        self.table_widget2.horizontalHeader().setStyleSheet("background-color: #34495e; color: #ecf0f1;")
        self.table_widget2.verticalHeader().setStyleSheet("background-color: #34495e; color: #ecf0f1;")
        self.table_widget.horizontalHeader().setStyleSheet("background-color: #34495e; color: #ecf0f1;")
        self.table_widget.verticalHeader().setStyleSheet("background-color: #34495e; color: #ecf0f1;")
        self.table_widget.setStyleSheet("background-color: #34495e; color: #ecf0f1;")

        # self.button1.clicked.connect(self.add_row)
        # self.button2.clicked.connect(self.edit_row)
        # self.button3.clicked.connect(self.delete_row)
        # self.button4.clicked.connect(self.download_config)
        # self.add_button2.clicked.connect(self.add_row2)
        # self.edit_button2.clicked.connect(self.edit_row2)
        # self.delete_button2.clicked.connect(self.delete_row2)
        # self.download_button2.clicked.connect(self.download_config2)

        self.show()

    def search(self):
        # search the table for the text in the search bar
        # if the text is found, highlight the row
        # if the text is not found, remove the highlight
        search_text = self.search_bar.text()
        for row in range(self.table_widget.rowCount()):
            for column in range(self.table_widget.columnCount()):
                item = self.table_widget.item(row, column)
                if item is not None:
                    if search_text.lower() in item.text().lower():
                        self.table_widget.selectRow(row)
                        return
        self.table_widget.clearSelection()

    def on_click(self):
        # when a row is clicked, print the text in the first column
        for currentQTableWidgetItem in self.table_widget.selectedItems():
            print(currentQTableWidgetItem.text())
