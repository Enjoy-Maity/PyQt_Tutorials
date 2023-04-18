import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel with Image")

        image_label = QLabel()
        image_label.setPixmap(QPixmap("./images/minions.png"))

        v_layout = QVBoxLayout()
        v_layout.addWidget(image_label)
        # v_layout.addanchor(image_label,Qt.A)

        self.setLayout(v_layout)


app = QApplication(sys.argv)
widget = Widget()
widget.show()
app.exec()