import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom MainWindow")

        button = QPushButton("Click")
        button.clicked.connect(self.button_clicked)
        button.pressed.connect(self.button_pressed)
        button.released.connect(self.button_released)

        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)

    def button_clicked(self):
        print("Button Clicked")
    
    def button_released(self):
        print("Button Released")

    def button_pressed(self):
        print("Button Pressed")

app = QApplication(sys.argv)

widget = Widget()
widget.show()

app.exec()