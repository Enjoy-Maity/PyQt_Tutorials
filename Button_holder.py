from PySide6.QtWidgets import QMainWindow, QPushButton
class Button_Holder(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Button Holder App")
		button = QPushButton("Press Me!")
		
		#Set up the Button as the central widget for application
		self.setCentralWidget(button)
