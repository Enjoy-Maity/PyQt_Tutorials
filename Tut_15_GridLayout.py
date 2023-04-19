import sys
from PySide6.QtWidgets import QWidget, QApplication, QSizePolicy, QPushButton, QGridLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GridLayout")
        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")
        button_3.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding) # Adding this to make the button expand in all direction when the rowspan is used
        button_4 = QPushButton("Four")
        button_5 = QPushButton("Five")
        button_6 = QPushButton("Six")
        button_7 = QPushButton("Seven")

        grid_layout = QGridLayout()
        grid_layout.addWidget(button_1,0,0)
        grid_layout.addWidget(button_2,0,1,1,2) # (row,column,rowspan, colspan)
        grid_layout.addWidget(button_3,1,0,2,1) # This alone will not show the button expanded in all directions
        grid_layout.addWidget(button_4,1,1)
        grid_layout.addWidget(button_5,1,2)
        grid_layout.addWidget(button_6,2,1)
        grid_layout.addWidget(button_7,2,2)

        self.setLayout(grid_layout)

app = QApplication(sys.argv)
widget = Widget()
widget.show()
app.exec()