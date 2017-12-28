import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

# 두개가 생성된다...
print(sys.argv)

label = QLabel("Hello PyQt")
label.show()


label2 = QPushButton("Quit")
label2.show()
app.exec_()