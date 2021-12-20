import re
from PyQt5 import QtCore, QtGui, QtWidgets
from bd_users import add

class Ui_MainWindow1(object):
        def par(self):

            text = self.lineEdit_login.text()
            text_parol = self.lineEdit_parol.text()
            if re.search("[/)(*?>.<,{}8&^%# !_@$=+]", text) or  text == '':
                flag_log = 0
            else:
                flag_log = -1

            if flag_log == -1:
                r = "Данные введены верно"

            if flag_log == 0:
                r = "Данные введены неверно! "

            self.lable__ = QtWidgets.QLabel(self.centralwidget)
            self.lable__.setGeometry(QtCore.QRect(272, 171, 221, 31))
            self.lable__.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.lable__.setObjectName("l")
            self.lable__.setText(r)
            self.lable__.show()

            if re.search("[/)(*?>.<,{} 8&^%#!_@$]",
                         text_parol) or text_parol == '' :
                flag_par = 0
            else:
                flag_par = -1

            if flag_par == -1:
                p = "Данные введены верно"

            if flag_par == 0:
                p = "Данные введены неверно! "

            self.lable__p = QtWidgets.QLabel(self.centralwidget)
            self.lable__p.setGeometry(QtCore.QRect(270, 260, 221, 31))
            self.lable__p.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.lable__p.setObjectName("l")
            self.lable__p.setText(p)
            self.lable__p.show()
            # окончание проверки на входные данные
            if flag_par == -1:
                function_of_cheking = add(1, text, text_parol)  # добавляет пользователя в бд
                if function_of_cheking == "Такой логин уже существует! Придумайте другой":
                    message = "Такой логин уже существует! Придумайте другой"
                else:
                    message = "Вы успешно зарегистрированы!"
                self.lable00 = QtWidgets.QLabel(self.centralwidget)
                self.lable00.setGeometry(QtCore.QRect(160, 410, 331, 41))
                self.lable00.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.lable00.setObjectName("l")
                self.lable00.setText(message)
                self.lable00.show()

        def setupUi(self, MainWindow):

            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(536, 462)
            MainWindow.setStyleSheet("background-color: rgb(234, 239, 255);\n"
    "")
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(160, 20, 231, 61))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Black")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.label.setFont(font)
            self.label.setStyleSheet("\n"
    "color:rgb(109, 105, 143);")
            self.label.setObjectName("label")
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(60, 100, 161, 21))
            font = QtGui.QFont()
            font.setPointSize(13)
            self.label_2.setFont(font)
            self.label_2.setObjectName("label_2")
            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setGeometry(QtCore.QRect(60, 190, 171, 21))
            font = QtGui.QFont()
            font.setPointSize(13)
            self.label_3.setFont(font)
            self.label_3.setObjectName("label_3")

            self.lineEdit_login = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit_login.setGeometry(QtCore.QRect(60, 130, 351, 31))
            self.lineEdit_login.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.lineEdit_login.setObjectName("lineEdit_2")
            self.lineEdit_login.setMaxLength(6)


            self.lineEdit_parol = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit_parol.setGeometry(QtCore.QRect(60, 220, 351, 31))
            self.lineEdit_parol.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.lineEdit_parol.setObjectName("lineEdit_3")
            self.lineEdit_parol.setMaxLength(6)


            self.label_4 = QtWidgets.QLabel(self.centralwidget)
            self.label_4.setGeometry(QtCore.QRect(60, 290, 441, 61))
            self.label_4.setIndent(1)
            self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
            self.label_4.setObjectName("label_4")
            self.pushButton_regestration = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_regestration.setGeometry(QtCore.QRect(160, 350, 241, 61))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.pushButton_regestration.setFont(font)
            self.pushButton_regestration.setStyleSheet("background-color: rgb(161, 49, 181);\n"
    "color: rgb(255, 255, 255);")
            self.pushButton_regestration.setObjectName("pushButton_regestration")

            self.pushButton_regestration.clicked.connect(self.par)
            MainWindow.setCentralWidget(self.centralwidget)
            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)




        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "Регистрация"))
            self.label.setText(_translate("MainWindow", "Регистрация"))
            self.label_2.setText(_translate("MainWindow", "Введите логин"))
            self.label_3.setText(_translate("MainWindow", "Введите пароль"))
            self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\">Внимание! Логин и пароль должны "
                                                          "состоять только из латинских букв. </p><p>Допускается "
                                                          "использование цифр. Размер текста - не более 6 знаков!</p></body></html>"))
            self.pushButton_regestration.setText(_translate("MainWindow", "Зарегистрироваться"))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


