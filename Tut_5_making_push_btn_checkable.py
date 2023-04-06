# Checkable push buttons are really helpful for stating the condition of the button being
# pushed or not.

from PySide6.QtWidgets import QApplication, QPushButton
import sys

def btn_clicked(data):
    print(f"You clicked on the button : {data}")

app = QApplication(sys.argv)
btn = QPushButton()
btn.setText("Checkable Push Button")
btn.setCheckable(True)
btn.clicked.connect(btn_clicked)
btn.show()
app.exec()