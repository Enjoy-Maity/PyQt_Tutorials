from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Our First Main Window App!")
window.show()

button = QPushButton()
button.setText("Press Me")

window.setCentralWidget(button)

app.exec()