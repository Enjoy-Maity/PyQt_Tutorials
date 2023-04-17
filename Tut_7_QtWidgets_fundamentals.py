import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()

        button1 = QPushButton("Button 1")
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("Button2")
        button2.clicked.connect(self.button2_clicked)

        # we need to use layout as even though we have created the buttons, 
        # but the widget doesn't know where to put the button

        # widget_layout = QHBoxLayout() # Horizontal
        widget_layout = QVBoxLayout()   # Vertical
        widget_layout.addWidget(button1)
        widget_layout.addWidget(button2)
        self.setWindowTitle("RockWidget")
        self.setLayout(widget_layout)
    
    def button1_clicked(self):
        print("Button 1 Clicked")
    
    def button2_clicked(self):
        print("Button 2 Clicked")


app = QApplication(sys.argv)
widget = RockWidget()
widget.show()

app.exec()