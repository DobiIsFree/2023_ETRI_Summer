import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # label
        self.label = QLabel("msg: ", self)
        self.label.move(10, 10)

        # btn
        self.btn = QPushButton("click", self)
        self.btn.move(10, 40)

        # signal-slot
        self.btn.clicked.connect(self.btn_clicked)

        # img
        self.img_label = QLabel()
        self.img_label.setPixmap(QPixmap("logo.png"))
        self.setCentralWidget(self.img_label)

    def btn_clicked(self):
        self.label.clear()
        self.label.setText("btn click")


app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()