# Importing the components we need.
from PySide6.QtWidgets import QApplication, QWidget
# Importing sys which is responsible for processing command line arguments.
import sys

# QApplication is the wrapper class that is going to englobing everything that you do in your application
app = QApplication(sys.argv)

window = QWidget()
# By default the widgets or windows are hidden in the application, so you have show them
window.show()               # Displays the application

# Calling the exec method to start the event loop
app.exec()