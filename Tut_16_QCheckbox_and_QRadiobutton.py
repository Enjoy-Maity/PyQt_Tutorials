import sys
from PySide6.QtWidgets import QWidget, QApplication, QGroupBox, QCheckBox, QRadioButton, QVBoxLayout, QHBoxLayout, QButtonGroup

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCheckBox and QRadioButton")

        os = QGroupBox("Choose operating system")       # Grouping all the checkboxes
        windows = QCheckBox("Windows")
        windows.toggled.connect(self.windows_box_toggled)

        linux = QCheckBox("Linux")
        linux.toggled.connect(self.linux_box_toggled)

        mac = QCheckBox("Mac")
        mac.toggled.connect(self.mac_box_toggled)

        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        os.setLayout(os_layout)

        drinks = QGroupBox("Drinks")
        beer = QCheckBox("Beer")
        juice = QCheckBox("Juice")
        coffee = QCheckBox("Coffee")
        beer.setChecked(True)
        
        # Exclusive checkboxes
        exclusive_button_group = QButtonGroup(self)
        exclusive_button_group.addButton(beer)
        exclusive_button_group.addButton(juice)
        exclusive_button_group.addButton(coffee)
        exclusive_button_group.setExclusive(True)       # Making the group exclusive

        drink_layout = QVBoxLayout()
        drink_layout.addWidget(beer)
        drink_layout.addWidget(juice)
        drink_layout.addWidget(coffee)
        drinks.setLayout(drink_layout)

        answers = QGroupBox("Choose Answer")
        answer_a = QRadioButton("a")
        answer_b = QRadioButton("b")
        answer_c = QRadioButton("c")
        answer_a.setChecked(True)

        answer_layout = QVBoxLayout()
        answer_layout.addWidget(answer_a)
        answer_layout.addWidget(answer_b)
        answer_layout.addWidget(answer_c)
        answers.setLayout(answer_layout)

        h_layout = QHBoxLayout()
        h_layout.addWidget(os)
        h_layout.addWidget(drinks)

        layout = QVBoxLayout()
        layout.addLayout(h_layout)
        layout.addWidget(answers)

        self.setLayout(layout)

    def windows_box_toggled(self,checked):
        if(checked):
            print("Windows Box Checked")
        
        else:
            print("Windows Box Unchecked")

    def linux_box_toggled(self,checked):
        if(checked):
            print("Linux Box Checked")
        
        else:
            print("Linux Box Unchechcked")

    def mac_box_toggled(self,checked):
        if(checked):
            print("Mac Box Checked")
        
        else:
            print("Mac Box Unchecked")

app = QApplication(sys.argv)
widget = Widget()
widget.show()
app.exec()