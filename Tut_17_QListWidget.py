import sys
from PySide6.QtWidgets import QApplication, QWidget, QListWidget, QAbstractItemView, QPushButton, QVBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QListWidget demo")
        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)     # Giving the ability to select multople items
        self.list_widget.addItem("One")
        self.list_widget.addItems(["Two","Three"])
        self.list_widget.currentItemChanged.connect(self.current_item_changed)
        self.list_widget.currentTextChanged.connect(self.current_text_changed)

        button_add_item = QPushButton("Add Item")
        button_add_item.clicked.connect(self.add_item)

        button_delete_item = QPushButton("Delete Item")
        button_delete_item.clicked.connect(self.delete_item)

        button_item_count = QPushButton("Item Count")
        button_item_count.clicked.connect(self.item_count)

        button_selected_items = QPushButton("Selected Items")
        button_selected_items.clicked.connect(self.selected_items)

        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)
        layout.addWidget(button_add_item)
        layout.addWidget(button_delete_item)
        layout.addWidget(button_item_count)
        layout.addWidget(button_selected_items)

        self.setLayout(layout)

    def current_item_changed(self,item):
        if(item):
            print("Current Item : ", item.text())

    def current_text_changed(self,text):
        print("Current Text Changed : ",text)

    def add_item(self):
        self.list_widget.addItem("New Item")

    def delete_item(self):
        self.list_widget.takeItem(self.list_widget.currentRow())

    def item_count(self):
        print("Item Count : ",self.list_widget.count())
    
    def selected_items(self):
        list = self.list_widget.selectedItems()
        for i in list:
            print(i.text())

app = QApplication(sys.argv)
widget = Widget()
widget.show()
app.exec()