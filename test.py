# from PySide6.QtGui import QTextCursor, QTextCharFormat, QColor
# from PySide6.QtWidgets import QTextEdit, QApplication
# import sys

# class FileTextReader(QTextEdit):
#     def __init__(self, parent=None):
#         super().__init__(parent)
        
#     def search_and_highlight(self, search_str):
#         cursor = self.document().find(search_str, QTextCursor.Start)
#         if not cursor.isNull():
#             format = QTextCharFormat()
#             format.setBackground(QColor("yellow"))
#             while not cursor.isNull():
#                 cursor.mergeCharFormat(format)
#                 cursor = self.document().find(search_str, cursor)

#                 # Get the line containing the search string
#                 block = cursor.block()
#                 line_number = block.blockNumber() + 1
#                 line_text = block.text().strip()
#                 print(f"Found '{search_str}' in line {line_number}: {line_text}")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     reader = FileTextReader()
#     reader.setPlainText("This is a test file.\nHere is a line with the word 'test'.\nAnother line here.")
#     reader.show()
#     reader.search_and_highlight("test")
#     sys.exit(app.exec_())

# from PySide6.QtCore import Qt, QRegularExpression
# from PySide6.QtGui import QTextCursor, QTextCharFormat, QColor, QSyntaxHighlighter

# class SearchHighlighter(QSyntaxHighlighter):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.search_text = ""
#         self.search_format = QTextCharFormat()
#         self.search_format.setBackground(Qt.yellow)
        
#     def highlightBlock(self, text):
#         if self.search_text:
#             index = text.indexOf(self.search_text, 0, Qt.CaseInsensitive)
#             while index >= 0:
#                 length = len(self.search_text)
#                 self.setFormat(index, length, self.search_format)
#                 index = text.indexOf(self.search_text, index + length, Qt.CaseInsensitive)
    
#     def setSearchText(self, search_text):
#         self.search_text = QRegularExpression(search_text)

# from PySide6.QtWidgets import QMainWindow, QTextEdit, QFileDialog, QInputDialog
# from PySide6.QtGui import QAction
# class FileTextReader(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.highlighter = SearchHighlighter(self.text_edit.document())
        
#     def initUI(self):
#         self.text_edit = QTextEdit(self)
#         self.setCentralWidget(self.text_edit)
        
#         self.search_action = QAction("Search", self)
#         self.search_action.triggered.connect(self.search)
#         self.addAction(self.search_action)
        
#         self.show()
        
#     def search(self):
#         search_text, ok = QInputDialog.getText(self, "Search", "Enter search text")
#         if ok:
#             self.highlighter.setSearchText(search_text)
#             self.highlighter.rehighlight()
# from PySide6.QtCore import Qt, QRegularExpression
# from PySide6.QtGui import QTextCursor, QTextCharFormat, QColor, QSyntaxHighlighter, QAction
# from PySide6.QtWidgets import QMainWindow, QTextEdit, QFileDialog, QMessageBox, QInputDialog, QApplication
# import sys

# class SearchHighlighter(QSyntaxHighlighter):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.search_text = ""
#         self.search_format = QTextCharFormat()
#         self.search_format.setBackground(Qt.yellow)
        
#     def highlightBlock(self, text):
#         if self.search_text:
#             index = text.indexOf(self.search_text, 0, Qt.CaseInsensitive)
#             while index >= 0:
#                 length = len(self.search_text)
#                 self.setFormat(index, length, self.search_format)
#                 index = text.indexOf(self.search_text, index + length, Qt.CaseInsensitive)
    
#     def setSearchText(self, search_text):
#         self.search_text = QRegularExpression(search_text)
        

# class FileTextReader(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.highlighter = SearchHighlighter(self.text_edit.document())
        
#     def initUI(self):
#         self.text_edit = QTextEdit(self)
#         self.setCentralWidget(self.text_edit)
        
#         self.search_action = QAction("Search", self)
#         self.search_action.triggered.connect(self.search)
#         self.addAction(self.search_action)
        
#         self.show()
        
#     def search(self):
#         search_text, ok = QInputDialog.getText(self, "Search", "Enter search text")
#         if ok:
#             self.highlighter.setSearchText(search_text)
#             self.highlighter.rehighlight()
#             cursor = self.text_edit.document().find(self.highlighter.search_text)
#             if cursor.isNull():
#                 QMessageBox.information(self, "Search", "No match found.")
#             else:
#                 line = cursor.blockNumber() + 1
#                 QMessageBox.information(self, "Search", f"Line containing the search string: {line}")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     reader = FileTextReader()
#     reader.setPlainText("This is a test file.\nHere is a line with the word 'test'.\nAnother line here.")
#     reader.show()
#     reader.search_and_highlight("test")
#     sys.exit(app.exec_())

# from PySide6.QtCore import Qt, QRegularExpression as QRegExp
# from PySide6.QtGui import QTextCursor, QTextCharFormat, QColor, QSyntaxHighlighter,QAction
# from PySide6.QtWidgets import QMainWindow, QTextEdit, QFileDialog, QMessageBox, QInputDialog

# class SearchHighlighter(QSyntaxHighlighter):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.search_text = ""
#         self.search_format = QTextCharFormat()
#         self.search_format.setBackground(Qt.yellow)
        
#     def highlightBlock(self, text):
#         if self.search_text:
#             index = text.indexOf(self.search_text, 0, Qt.CaseInsensitive)
#             while index >= 0:
#                 length = len(self.search_text)
#                 self.setFormat(index, length, self.search_format)
#                 index = text.indexOf(self.search_text, index + length, Qt.CaseInsensitive)
    
#     def setSearchText(self, search_text):
#         self.search_text = QRegExp(search_text)
        

# class FileTextReader(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.highlighter = SearchHighlighter(self.text_edit.document())
        
#     def initUI(self):
#         self.text_edit = QTextEdit(self)
#         self.setCentralWidget(self.text_edit)
        
#         self.search_action = QAction("Search", self)
#         self.search_action.triggered.connect(self.search)
#         self.addAction(self.search_action)
        
#         self.show()
        
#     def search(self):
#         search_text, ok = QInputDialog.getText(self, "Search", "Enter search text")
#         if ok:
#             self.highlighter.setSearchText(search_text)
#             self.highlighter.rehighlight()
#             cursor = self.text_edit.document().find(self.highlighter.search_text)
#             if cursor.isNull():
#                 QMessageBox.information(self, "Search", "No match found.")
#             else:
#                 line = cursor.blockNumber() + 1
#                 QMessageBox.information(self, "Search", f"Line containing the search string: {line}")

# if __name__ == "__main__":
#     import sys
#     from PySide6.QtWidgets import QApplication

#     app = QApplication(sys.argv)
#     window = FileTextReader()
#     sys.exit(app.exec())
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class FileReader(QMainWindow):
    def __init__(self, parent=None):
        super(FileReader, self).__init__(parent)
        
        # Set up the main window
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("File Reader")
        
        # Set up the text editor
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        
        # Set up the search bar and button
        search_layout = QHBoxLayout()
        search_label = QLabel("Search:")
        self.search_box = QLineEdit()
        self.search_button = QPushButton("Search")
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_box)
        search_layout.addWidget(self.search_button)
        search_layout.addStretch()
        
        # Set up the status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        # Connect the search button to the search function
        self.search_button.clicked.connect(self.search_text)
        
    def search_text(self):
        # Get the search string from the search box
        search_string = self.search_box.text()
        
        # If the search string is empty, do nothing
        if not search_string:
            return
        
        # Clear the previous selections
        self.text_edit.moveCursor(QTextCursor.Start)
        self.text_edit.selectAll()
        self.text_edit.setTextBackgroundColor(QColor("white"))
        self.text_edit.moveCursor(QTextCursor.Start)
        
        # Search for the string in the text
        found = False
        line_number = 1
        while True:
            cursor = self.text_edit.find(search_string, QTextDocument.FindCaseSensitively)
            if cursor.isNull():
                break
            
            # Highlight the text
            self.text_edit.setTextBackgroundColor(QColor("yellow"))
            
            # Scroll to the highlighted text
            self.text_edit.ensureCursorVisible()
            
            # Show the line containing the string in the status bar
            current_block = cursor.block()
            line_text = current_block.text()
            self.status_bar.showMessage(f"Found '{search_string}' on line {line_number}: {line_text}")
            
            found = True
            line_number += 1
        
        # If the string wasn't found, display a message
        if not found:
            self.status_bar.showMessage(f"'{search_string}' not found.")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    file_reader = FileReader()
    file_reader.show()
    sys.exit(app.exec())
