import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)

        self.cbox = QCheckBox("미수", self)
        self.cbox.move(10, 10)
        self.cbox.stateChanged.connect(self.slot)

        self.spinbox = QSpinBox(self)
        self.spinbox.move(10, 50)
        self.spinbox.valueChanged.connect(self.spinbox_value_chagned)

        self.combo = QComboBox(self)
        self.combo.resize(200, 30)
        self.combo.move(10, 100)

        self.combo.addItem("easy")
        self.combo.addItem("normal")
        self.combo.addItem("hard")
        self.combo.currentTextChanged.connect(self.slot2)

    def slot(self, state):
        if state == Qt.Checked:
            print("미수")
        else:
            print("보통")

    def slot2(self, text):
        print(f'combo box: {text}')

    def spinbox_value_chagned(self):
        value = self.spinbox.value()
        print(f'spinbox value: {value}')

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()
