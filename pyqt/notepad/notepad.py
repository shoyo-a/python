import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QHBoxLayout,
    QFileDialog
)

class Notepad(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton("Clear", self)
        self.save_btn = QPushButton("Save", self)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.clr_btn)
        btn_layout.addWidget(self.save_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addLayout(btn_layout)
        self.setLayout(layout)

        self.clr_btn.clicked.connect(self.clear_text)
        self.save_btn.clicked.connect(self.save_text)

        self.setWindowTitle("Notepad")
        self.show()

    def clear_text(self):
        self.text.clear()
    
    def save_text(self):
        filename = self.get_save_file_name()
        print(filename)

        if filename:
            self.save_to_text(filename)
    
    def get_save_file_name(self) -> str:
        return QFileDialog().getSaveFileName(self, caption = self.text.toPlainText())[0]
    
    def save_to_text(self, filename:str):
        with open(filename, "w") as fp:
            fp.write(self.text.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec_())