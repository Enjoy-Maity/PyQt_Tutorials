from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

class Widget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setMinimumSize(1000,500)
        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.button_clicked_hard_way)

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critical)

        button_question = QPushButton("Question")
        button_question.clicked.connect(self.button_clicked_question)

        button_information = QPushButton("Information")
        button_information.clicked.connect(self.button_clicked_information)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_clicked_about)

        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout)
    
    # Hard Way
    def button_clicked_hard_way(self):
        message = QMessageBox()
        message.setMinimumSize(700,200)
        message.setWindowTitle("Message Title")
        message.setText("Something Happened")
        message.setInformativeText("Do you want to do something about it?")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User Chose ok")
        
        else:
            print("User chose Cancel")
    
    # Critical
    def button_clicked_critical(self):
        ret = QMessageBox.critical(self,"Message Title","Critical Message!",QMessageBox.Ok|QMessageBox.Cancel)

        if ret == QMessageBox.Ok:
            print("User Chose Ok")
        
        else:
            print("User Chose Cancel")
    
    # Question
    def button_clicked_question(self):
        ret = QMessageBox.question(self,"Message Title","Question",QMessageBox.Ok|QMessageBox.Cancel)

        if ret == QMessageBox.Ok:
            print("User Chose Ok")

        else:
            print("User Chose Cancel")
        
    # Information
    def button_clicked_information(self):
        ret = QMessageBox.information(self,"Message Title!","Some Information", QMessageBox.Ok|QMessageBox.Cancel)

        if ret == QMessageBox.Ok:
            print("User Chose Ok")
        
        else:
            print("User Chose Cancel")
    
    # Warning
    def button_clicked_warning(self):
        ret = QMessageBox.warning(self,"Message Title!","Some Warning",QMessageBox.Ok|QMessageBox.Cancel)

        if ret == QMessageBox.Ok:
            print("User Chose Ok")
        
        else:
            print("User Chose Cancel")

    # About
    def button_clicked_about(self):
        ret = QMessageBox.about(self,"Message Title!","About")

        if ret == QMessageBox.Ok:
            print("User Chose Ok")

        else:
            print("User Chose Cancel")


app = QApplication()

widget = Widget()
widget.show()

app.exec()