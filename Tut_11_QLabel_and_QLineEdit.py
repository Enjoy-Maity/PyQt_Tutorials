import sys
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QApplication, QPushButton

class Widget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("QLabel and QLineEdit")
        self.setFixedSize(540,360)
        label = QLabel("Fullname: ")
        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(self.text_changed)                       # gets triggered whenever thethe text changes
        self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        self.line_edit.editingFinished.connect(self.editing_finished)
        self.line_edit.returnPressed.connect(self.return_pressed)
        self.line_edit.selectionChanged.connect(self.selection_changed)
        self.line_edit.textEdited.connect(self.text_edited)

        button = QPushButton("Grab Data")
        self.text_holder_Label = QLabel("I AM BATMAN!")

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_Label)

        self.setLayout(v_layout)

    
    def button_clicked(self):
        print("Fullname :",self.line_edit.text())
        self.text_holder_Label.setText(self.line_edit.text())
    
    def text_changed(self):
        # print("Text changed to ",self.line_edit.text())
        self.text_holder_Label.setText(self.line_edit.text())

    def cursor_position_changed(self,old,new):
        print("Cursor old position : ",old,"-New Position : ",new)

    def editing_finished(self):
        print("Editing Finished")

    def return_pressed(self):
        print("Return Pressed")
    
    def selection_changed(self):
        print("Selection Changed : ",self.line_edit.selectedText())

    def text_edited(self,new_text):
        print("Text Edited. New Text : ",new_text)
        
app = QApplication(sys.argv)

widget = Widget()
widget.show()

app.exec()