from PySide6.QtWidgets import QApplication
import sys
from Button_holder import Button_Holder

app = QApplication(sys.argv)
window = Button_Holder()
window.show()
app.exec()