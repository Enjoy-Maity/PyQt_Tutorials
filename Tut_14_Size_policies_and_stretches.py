import sys
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QSizePolicy, QHBoxLayout, QVBoxLayout, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Size Policy and Stretch")
        self.setMinimumSize(500,300)
        label = QLabel("Some Text: ")
        line_edit = QLineEdit()

        # SizePolicy : how the widgets behaves if container space is expanded or shrunk

        # First Parameter is for horizontal size policy, and the second parameter is for vertical size policy
        line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)    # these are the defaults
        # line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(line_edit)

        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")

        # Stretch : how much of the available space (in Layout) is occupied by each widget.
        # You specify the stretch when you add things to the layout : button_1 takes up 2 units, 
        # button_2 and button_3 take up 1 unit each.

        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(button_1,stretch = 2)
        h_layout_1.addWidget(button_2,stretch = 1)
        h_layout_1.addWidget(button_3,stretch = 1)

        v_layout =  QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addLayout(h_layout_1)
        self.setLayout(v_layout)

app = QApplication(sys.argv)
widget = Widget()
widget.show()
app.exec()