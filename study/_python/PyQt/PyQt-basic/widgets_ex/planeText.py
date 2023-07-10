import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 200)

        self.text = QPlainTextEdit(self)
        self.text.move(10, 10)
        self.text.resize(280, 180)

        # print text
        self.text.appendPlainText("hello\n")
        self.text.appendPlainText("python\n")
        self.text.appendPlainText("plan text!\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
