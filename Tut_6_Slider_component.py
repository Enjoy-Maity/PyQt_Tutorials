# Creating a Slider component
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

def value_viewer(data):
    print(f"You selected the value of :{data}")

app = QApplication()
slider = QSlider(Qt.Horizontal)
vslider = QSlider(Qt.Vertical)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

vslider.setMinimum(1)
vslider.setMaximum(100)
vslider.setValue(25)

slider.valueChanged.connect(value_viewer)
slider.show()

vslider.valueChanged.connect(value_viewer)
vslider.show()
app.exec()