import sys
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QTabWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget Demo")

        tab_widget = QTabWidget(self)

        # Information
        widget_form = QWidget()
        label_full_name = QLabel("Full Name: ")
        line_edit_full_name = QLineEdit()
        form_layout = QHBoxLayout()
        form_layout.addWidget(label_full_name)
        form_layout.addWidget(line_edit_full_name)
        widget_form.setLayout(form_layout)

        # Buttons
        widget_buttons = QWidget()
        button_1 = QPushButton("One")
        button_1.clicked.connect(self.button_1_clicked)
        
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(button_1)
        buttons_layout.addWidget(button_2)
        buttons_layout.addWidget(button_3)
        widget_buttons.setLayout(buttons_layout)

        # add tabs
        tab_widget.addTab(widget_form,"Information")
        tab_widget.addTab(widget_buttons, "Buttons")

        v_layout = QVBoxLayout()
        v_layout.addWidget(tab_widget)

        self.setLayout(v_layout)

    def button_1_clicked(self):
        print("Button 1 Clicked")

app = QApplication(sys.argv)
widget = Widget()
widget.show()
app.exec()