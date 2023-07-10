import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton("quit", self)
        self.btn.resize(100, 30)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.btn_clicked)

        self.btn2 = QPushButton("start", self)
        self.btn2.setDisabled(True)
        self.btn.move(20, 50)
        print(f'btn text 값 얻어오기: {self.btn.text()}')

    # btn click 시 호출되는 메소드
    def btn_clicked(self):
        print("btn clicked!")
        self.close()

app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()