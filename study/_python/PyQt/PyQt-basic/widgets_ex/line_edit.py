import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # line_edit: 사용자로부터 입력 받는데 사용
        self.line_edit = QLineEdit(" ", self)
        self.line_edit.move(10, 10)

        self.line_edit.setEnabled(False)
        self.line_edit.setText("hello")

        # btn
        self.btn = QPushButton("edit", self)
        self.btn.move(10, 40)
        self.btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("start text edit")
        self.line_edit.clear()
        self.line_edit.setEnabled(True)

app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()