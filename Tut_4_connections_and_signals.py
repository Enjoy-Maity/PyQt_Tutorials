from PySide6.QtWidgets import QApplication,QPushButton, QMainWindow, QCheckBox
import sys

def button_clicked():
    print("You clicked the button, didn't you!")

def check_btn_clicked(data):
    print(f"You clicked on the data : {data}")

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("PySide Tutorial")
window.show()

button = QPushButton()
button.setText("Press Me")
button.show()

# connecting the button to a method, after the button is clicked.
# clicked is a signal here, thats emitted when the button is clicked.
button.clicked.connect(button_clicked)

check_button = QCheckBox()
check_button.setText("Click to check")
check_button.show()
check_button.clicked.connect(check_btn_clicked)
window.setCentralWidget(button)



app.exec()