import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # status bar: window 하단에 간단한 메시지 출력
        self.statusbar = QStatusBar(self) # QStatusBar 객체 생성
        self.setStatusBar(self.statusbar) # 위젯 배치
        self.statusbar.showMessage("hello ^^") # 문자열을 상태바에 출력
        # currentMessage() 현재 메시지 얻어오기
        # clearMessage() 상태바에 출력된 메시지 지우기

app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()