from Rules import Ui_Rules
import re
import user
from PyQt5 import QtCore
from PyQt5 import QtWidgets, QtGui
from quastion10 import Ui_quastion10
from difficult_questions import adding

class Ui_quastion9(QtWidgets.QWidget):
    def __init__(self, parent=None, current_user = None):

        super().__init__(parent)
        if (current_user != None) and type(current_user) == user.User:
            self.current_user = current_user
        self.massiv = []
        self.maassiv_otvet = []
        self.setupUi()


    def mas(self, numberColumn, numberRow, massiv):
        r = massiv[numberRow][numberColumn]
        return r

    # def chek(self):
    def s(self):

        self.close()
        self.ui = Ui_quastion10(None, self.current_user)
        self.ui.show()


    def rules(self):

        self.window_rules = QtWidgets.QMainWindow()
        self.ui = Ui_Rules()
        self.ui.setupUi(self.window_rules)
        self.window_rules.show()

    def qas(self):

        text = self.lineEdit_answer.text()
        if text == self.mas(2, 1, self.massiv):
            self.current_user.answered_correct()
        print(self.current_user.login + F" correct_answers: {self.current_user.correct_answers}")
        self.s()


    def setupUi(self):
        self.massiv = adding()
        self.setObjectName("quastion")
        self.resize(911, 712)
        self.setStyleSheet("background-color: rgb(234, 239, 255);")
        self.setWindowTitle("Викторина")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 30, 391, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                 "")
        self.label.setObjectName("label")
        # ВОПРОССССС
        self.label_quastion = QtWidgets.QLabel(self)
        self.label_quastion.setGeometry(QtCore.QRect(30, 130, 861, 331))
        font = QtGui.QFont()
        font.setFamily(" Segoe UI Black")
        font.setPointSize(12)
        self.label_quastion.setFont(font)
        self.label_quastion.setStyleSheet("background-color: rgb(246, 249, 255);")
        self.label_quastion.setObjectName("label_quastion")


        self.label_quastion.setText(self.mas(1, 1, self.massiv))
        self.label_quastion.show()

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 470, 191, 21))
        self.label_2.setObjectName("label_2")

        self.label_aswer = QtWidgets.QLabel(self)
        self.label_aswer.setGeometry(QtCore.QRect(30, 580, 831, 16))

        self.label_aswer.setText("ввод ответа только с маленькой буквы, без использования пробелов. Допускается ввод "
                                 "только кириллицей или цифрами.")
        self.label_aswer.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_aswer.setObjectName("label_aswer")

        self.lineEdit_answer = QtWidgets.QLineEdit(self)
        self.lineEdit_answer.setGeometry(QtCore.QRect(30, 490, 851, 91))
        self.lineEdit_answer.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_answer.setObjectName("lineEdit_2")
        self.lineEdit_answer.setMaxLength(50)


        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(670, 640, 211, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(193, 185, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.qas)

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(220, 680, 441, 20))
        self.label_3.setObjectName("label_3")
        # кнопка правила
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 640, 93, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(248, 193, 255);\n"
                                        "color: rgb(0, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.rules)

        self.label.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#ffffff;\">Вопрос: 9/10</span></p></body></html>")

        self.pushButton.setText("следующий вопрос ->")

        self.label_3.setText(
            "<html><head/><body><p><span style=\" font-size:9pt;\">примечание: вернуться на предыдущий вопрос невозможно!</span></p></body></html>")
        self.pushButton_3.setText("правила")




