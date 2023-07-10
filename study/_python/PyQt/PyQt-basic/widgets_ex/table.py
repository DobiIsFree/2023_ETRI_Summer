import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 300, 300, 300)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(290, 290)
        # vertical header 숨기기
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(2)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("(0,0"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("(0,1"))

        self.tableWidget.setItem(1, 0, QTableWidgetItem("(1,0"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("(1,1"))

        self.tableWidget2 = QTableWidget(self)
        self.tableWidget2.move(0, 100)
        self.tableWidget2.resize(290, 290)
        self.tableWidget2.setColumnCount(2)
        self.tableWidget2.setRowCount(3)

        labels = ['종목명', '종목코드']
        self.tableWidget2.setHorizontalHeaderLabels(labels)

        self.tableWidget2.setItem(0, 0, QTableWidgetItem("삼성전자"))
        self.tableWidget2.setItem(0, 1, QTableWidgetItem("005930"))
        self.tableWidget2.setItem(1, 0, QTableWidgetItem("SK하이닉스"))
        self.tableWidget2.setItem(1, 1, QTableWidgetItem("000660"))
        self.tableWidget2.setItem(2, 0, QTableWidgetItem("NAVER"))
        self.tableWidget2.setItem(2, 1, QTableWidgetItem("035420"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()