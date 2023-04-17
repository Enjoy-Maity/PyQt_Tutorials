import sys
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction,QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QStatusBar

# QMainWindow is a class that allows us to work with events like 
# Menu, Toolbars, StatusBars, Actions

class MainWindow(QMainWindow):
    def __init__(self,app) -> None:
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom MainWindow")

        # MenuBar and Menus
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        # addAction gives us the way to manipulate Qt Application 
        # For example the user wants to quit either through the toolbar or go into the file menu and select quit 
        # the way Qt does this, it adds in an intermediary step through which you can go to trigger this action
        
        # An Action is an object that you can either add to the toolbar or the menubar and when the user tries to 
        # quit either through the menu or the toolbar, all these things are going to go through the same action and 
        # you can connect this action to a method that is going to do things in our Qt Application and we don't have to write
        # duplicate our code either in the menubar or the toolbar.

        quit_action = file_menu.addAction("Quit") # naming this action and we are connecting to it & making a slot repobnd whenever 
                                                  # this action here is triggered
        
        quit_action.triggered.connect(self.quit)

        edit_menu = menubar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menubar.addMenu("Window")
        menubar.addMenu("Setting")
        menubar.addMenu("Help")

        # Working with toolbars
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        toolbar.addAction(quit_action)

        action1 = QAction("Some Action",self)
        action1.setStatusTip("Status message for some action") # This popups when you hover over the button
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("start.png"),"Some other Action",self)
        action2.setStatusTip("Status message for some other action")
        action2.triggered.connect(self.toolbar_button_click)
        # action2.setCheckable(True)
        toolbar.addAction(action2)

        # Adding a separator 
        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click Here"))

        # Working with Statusbar
        self.setStatusBar(QStatusBar(self))

        button = QPushButton("Button")
        button.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button)


    def button1_clicked(self):
        print("Clicked on button1")
    
    def toolbar_button_click(self):
        self.statusBar().showMessage(" Action 1 triggered",3000)
    
    def quit(self): 
        self.app.quit()


app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()