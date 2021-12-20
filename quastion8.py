from Rules import Ui_Rules
from qus import read_single_row
import re
from PyQt5 import QtCore
from PyQt5 import QtWidgets, QtGui
from quastion9 import Ui_quastion9
import user


class Ui_quastion8(QtWidgets.QWidget):
    def __init__(self, parent=None, current_user = None):

        super().__init__(parent)
        if (current_user != None) and type(current_user) == user.User:
            self.current_user = current_user
        self.massiv = []
        self.maassiv_otvet = []

        self.setupUi()

    def par(self):

        text = self.lineEdit_answer.text()
        if not re.search("[A-D]",
                         text):
            flag = 0
        else:
            flag = -1

        if flag == 0:
            r = "Введите только A, B, C или D!"

        self.lable__ = QtWidgets.QLabel(self)
        self.lable__.setGeometry(QtCore.QRect(510, 610, 201, 16))
        self.lable__.setStyleSheet("color: rgb(255, 0, 0);")
        self.lable__.setObjectName("l")
        self.lable__.setText(r)
        self.lable__.show()

    def mas(self, numberColumn, numberRow, massiv):
        r = massiv[numberRow][numberColumn]
        return r

    def s(self):

        self.close()
        self.ui = Ui_quastion9(None, self.current_user)
        self.ui.show()

    def rules(self):
        self.window_rules = QtWidgets.QMainWindow()
        self.ui = Ui_Rules()
        self.ui.setupUi(self.window_rules)
        self.window_rules.show()

    def qas(self):

        text = self.lineEdit_answer.text()
        if not re.search("[A-D]",
                         text):
            flag = 0
        else:
            flag = -1

        # if flag == -1:
        #   r = ""

        if flag == 0:
            r = "Введите только A, B, C или D!"
            self.lable__ = QtWidgets.QLabel(self)
            self.lable__.setGeometry(QtCore.QRect(510, 610, 201, 16))
            self.lable__.setStyleSheet("color: rgb(255, 0, 0);")
            self.lable__.setObjectName("l")
            self.lable__.setText(r)
            self.lable__.show()
        if flag == -1:
            if self.label_A_answer.text() == self.mas(6, 1, self.massiv):
                self.maassiv_otvet.append(self.label_A_answer.objectName())
            if self.label_B_answer.text() == self.mas(6, 1, self.massiv):
                self.maassiv_otvet.append(self.label_B_answer.objectName())
            if self.label_C_answer.text() == self.mas(6, 1, self.massiv):
                self.maassiv_otvet.append(self.label_C_answer.objectName())
            if self.label_D_answer.text() == self.mas(6, 1, self.massiv):
                self.maassiv_otvet.append(self.label_D_answer.objectName())
            if self.lineEdit_answer.text() == self.maassiv_otvet[0]:
                self.current_user.answered_correct()

            print(self.current_user.login + F" correct_answers: {self.current_user.correct_answers}")

            self.s()


    def setupUi(self):

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
        # self.label_quastion.objectName()


        self.massiv = read_single_row()  # массив для бд

        self.maassiv_otvet = []  # массив для objecktName

        self.label_quastion.setText(self.mas(1, 1, self.massiv))
        self.label_quastion.show()

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 470, 191, 21))
        self.label_2.setObjectName("label_2")

        self.label_A = QtWidgets.QLabel(self)
        self.label_A.setGeometry(QtCore.QRect(30, 510, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_A.setFont(font)
        self.label_A.setText("A")
        self.label_A.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_A.setObjectName("label_A")

        self.label_B = QtWidgets.QLabel(self)
        self.label_B.setGeometry(QtCore.QRect(30, 570, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_B.setFont(font)
        self.label_B.setText("B")
        self.label_B.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_B.setObjectName("label_B")
        self.label_C = QtWidgets.QLabel(self)
        self.label_C.setGeometry(QtCore.QRect(420, 510, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_C.setFont(font)
        self.label_C.setText("C")
        self.label_C.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_C.setObjectName("label_C")

        self.label_D = QtWidgets.QLabel(self)
        self.label_D.setGeometry(QtCore.QRect(420, 570, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_D.setFont(font)
        self.label_D.setText("D")
        self.label_D.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_D.setObjectName("label_D")

        self.label_A_answer = QtWidgets.QLabel(self)
        self.label_A_answer.setGeometry(QtCore.QRect(60, 510, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_A_answer.setFont(font)
        self.label_A_answer.setObjectName("A")
        self.label_A_answer.setText(self.mas(2, 1, self.massiv))
        if self.label_A_answer.text() == self.mas(6, 1, self.massiv):
            self.massiv.append(self.label_A_answer.objectName())
        self.label_B_answer = QtWidgets.QLabel(self)
        self.label_B_answer.setGeometry(QtCore.QRect(60, 570, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_B_answer.setFont(font)
        self.label_B_answer.setObjectName("B")
        self.label_B_answer.setText(self.mas(3, 1, self.massiv))
        if self.label_B_answer.text() == self.mas(6, 1, self.massiv):
            self.massiv.append(self.label_B_answer.objectName())

        self.label_C_answer = QtWidgets.QLabel(self)
        self.label_C_answer.setGeometry(QtCore.QRect(450, 510, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_C_answer.setFont(font)
        self.label_C_answer.setObjectName("C")
        self.label_C_answer.setText(self.mas(4, 1, self.massiv))
        if self.label_C_answer.text() == self.mas(6, 1, self.massiv):
            self.massiv.append(self.label_C_answer.objectName())

        self.label_D_answer = QtWidgets.QLabel(self)
        self.label_D_answer.setGeometry(QtCore.QRect(450, 570, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_D_answer.setFont(font)
        self.label_D_answer.setObjectName("D")
        self.label_D_answer.setText(self.mas(5, 1, self.massiv))
        if self.label_D_answer.text() == self.mas(6, 1, self.massiv):
            self.massiv.append(self.label_D_answer.objectName())
        self.label_aswer = QtWidgets.QLabel(self)
        self.label_aswer.setGeometry(QtCore.QRect(240, 640, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_aswer.setFont(font)
        self.label_aswer.setText("Введите букву ответа(A, B, C, D):")
        self.label_aswer.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_aswer.setObjectName("label_aswer")

        self.lineEdit_answer = QtWidgets.QLineEdit(self)
        self.lineEdit_answer.setGeometry(QtCore.QRect(530, 640, 91, 31))
        self.lineEdit_answer.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_answer.setObjectName("lineEdit_2")
        self.lineEdit_answer.setMaxLength(1)

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
            "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#ffffff;\">Вопрос: 8/10</span></p></body></html>")

        self.label_2.setText(
            "<html><head/><body><p><span style=\" font-size:11pt;\">Варианты ответов:</span></p></body></html>")

        self.pushButton.setText("следующий вопрос")
        self.label_3.setText(
            "<html><head/><body><p><span style=\" font-size:9pt;\">примечание: вернуться на предыдущий вопрос невозможно!</span></p></body></html>")
        self.pushButton_3.setText("правила")





