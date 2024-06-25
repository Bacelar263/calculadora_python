from ast import Try
import sys
from unicodedata import name
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QSizePolicy

class calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora do Bazela')
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: white; color: #000; font-size: 30px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.addBtn(QPushButton('7'), 1, 0, 1, 1)
        self.addBtn(QPushButton('8'), 1, 1, 1, 1)
        self.addBtn(QPushButton('9'), 1, 2, 1, 1)
        self.addBtn(QPushButton('+'), 1, 3, 1, 1)
        self.addBtn(
            QPushButton('C'), 1, 4, 1, 1, 
            lambda: self.display.setText(''),
            'background: #d5580d; color: #fff; font-weight: 700;'
        )

        self.addBtn(QPushButton('4'), 2, 0, 1, 1)
        self.addBtn(QPushButton('5'), 2, 1, 1, 1)
        self.addBtn(QPushButton('6'), 2, 2, 1, 1)
        self.addBtn(QPushButton('-'), 2, 3, 1, 1)
        self.addBtn(
            QPushButton('<-'), 2, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1],
            ), 
            'background: #13823a; color: #fff; font-weight: 700;'
        )

        self.addBtn(QPushButton('1'), 3, 0, 1, 1)
        self.addBtn(QPushButton('2'), 3, 1, 1, 1)
        self.addBtn(QPushButton('3'), 3, 2, 1, 1)
        self.addBtn(QPushButton('/'), 3, 3, 1, 1)
        self.addBtn(QPushButton(''), 3, 4, 1, 1)

        self.addBtn(QPushButton('.'), 4, 0, 1, 1)
        self.addBtn(QPushButton('0'), 4, 1, 1, 1)
        self.addBtn(QPushButton(''), 4, 2, 1, 1)
        self.addBtn(QPushButton('*'), 4, 3, 1, 1)
        self.addBtn(
            QPushButton('='), 4, 4, 1, 1,
            self.eval_igual,
            'background: #095177; color: #fff; font-weight: 700;'
            )

        self.setCentralWidget(self.cw)

    def addBtn(self, btn, row, col, rowspan, colspan, func=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not func:
            btn.clicked.connect(
                lambda: self.display.setText(self.display.text() + btn.text())
            )
        else:
            btn.clicked.connect(func) 

        if style: 
            btn.setStyleSheet(style)
                  
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)


    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Conta inválida.')



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = calculadora()
    calc.show()
    qt.exec_()