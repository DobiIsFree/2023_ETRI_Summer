import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My HTS v1.0")
        self.setGeometry(300, 300, 400, 400)
        # self.setWindowIcon(QIcon("pie-chart.png"))

        btn = QPushButton(text="매수", parent=self)
        btn.move(10, 10) # btn 위치
        btn.clicked.connect(self.buy) # 이벤트 루프에 의해 호출 당하는 함수, callback

        btn = QPushButton(text="Quit", parent=self)
        btn.move(10, 40)
        btn.clicked.connect(self.btn_quit_clicked)

    def buy(self):
        # 시그널: 사용자가 버튼을 클링하는 행위
        # 슬롯: 버튼을 클릭했을 때 수행할 함수
        print("buy all")
    def btn_quit_clicked(self):
        QApplication.instance().quit()

# icon 넣기: https://www.iconfinder.com/
# 16x16 크기의 png foramt 아이콘 다운로드

print(sys.argv)
app = QApplication(sys.argv)
window = MyWindow()
window.show()

app.exec_() #start event loop