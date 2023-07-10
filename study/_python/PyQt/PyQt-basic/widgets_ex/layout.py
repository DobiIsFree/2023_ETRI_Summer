import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn1 = QPushButton("Button1")
        btn2 = QPushButton("Button2")

        # QMainWindow 상속 받은 window를 사용하면서
        # QWidget을 QMainWindow 안쪽으로 하나 만들고
        # 그 안으로 QVBoxLayout 을 놓고 그 안에 원하는 위젯 배치하기

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setCentralWidget(widget)

        # QWidgte->QVBoxLayout->QPushButton

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()
