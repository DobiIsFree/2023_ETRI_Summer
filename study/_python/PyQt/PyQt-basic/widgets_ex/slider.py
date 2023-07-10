import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(0, 100)
        self.slider.move(10, 10)
        self.slider.valueChanged.connect(self.slider_value_changed)

    def slider_value_changed(self):
        value = self.slider.value()
        print(value)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()