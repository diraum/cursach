from PyQt5 import QtCore
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QWidget
from registr import Ui_MainWindow1
from Rules import Ui_Rules
from quastion import Ui_quastion
from cheking_vhod import cheking
import user

# окно входа
class Ui_MainWindow(QWidget):
    # Функция, которая срабатывает при нажатии на кнопку регистрации

    def bd(self):
        login = self.lineEdit_login.text()
        self.label_message = QtWidgets.QLabel(self.centralwidget)
        self.label_message.setGeometry(QtCore.QRect(140, 460, 661, 31))
        self.label_message.setObjectName("label_message")
        if (self.lineEdit_login.text() == '') and (self.lineEdit_parol.text() == ''):
            message = "Пустые поля!"
            self.label_message.setText(message)
            self.label_message.show()

        else:
            message = cheking(1,login,self.lineEdit_parol.text())
            if message == "Пользователь не существует с таким логином. Пожалуйста, проверьте логин или зарегистрируйтесь.":
                message_button = "Пользователь не существует с таким логином. Пожалуйста, проверьте логин или " \
                                 "зарегистрируйтесь. "
                self.label_message.setText(message)
                self.label_message.show()
            else:
                if message == "Пароль неверен!":
                    message_button = "Пароль неверен!"
                    self.label_message.setText(message)
                    self.label_message.show()

                else:

                    self.ui = Ui_quastion(None,user.User(login))
                    self.ui.show()





    def show_window_2(self): # открытие 2  окна
        if (self.lineEdit_login.text() == '') and (self.lineEdit_parol.text() == ''):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow1()
            self.ui.setupUi(self.window)
            self.window.show()

    def rules (self):
        self.window_rules = QtWidgets.QMainWindow()
        self.ui = Ui_Rules()
        self.ui.setupUi(self.window_rules)
        self.window_rules.show()

    def start_q(self):
        self.ui = Ui_quastion()

        self.ui.show()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(234, 239, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(54, 30, 351, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(85, 0, 127);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 50, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(29)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 200, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 252, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 410, 191, 21))
        self.label_4.setIndent(1)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 250, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 340, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        #### кнопка "Зарегистрироваться"
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 410, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(170, 0, 0);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        # привязка события к кнопке
        self.pushButton.clicked.connect(self.show_window_2)


        ##### кнопка начала
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 510, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        # привязка события к кнопке
        self.pushButton_2.clicked.connect(self.bd)


        #### кнопка правила
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 520, 93, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(248, 193, 255);\n"
                                        "color: rgb(0, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.rules)

        self.lineEdit_login = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_login.setGeometry(QtCore.QRect(230, 280, 351, 31))
        self.lineEdit_login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_login.setObjectName("lineEdit_2")

        # проверка на ввод символы и цифры
        log_chek = QRegExp("[A-zA-Z0-9]{6}")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(log_chek)
        self.lineEdit_login.setValidator(pValidator)



        self.lineEdit_parol = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_parol.setGeometry(QtCore.QRect(230, 370, 351, 31))
        self.lineEdit_parol.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_parol.setObjectName("lineEdit_3")
        self.lineEdit_parol.setEchoMode(QtWidgets.QLineEdit.Password)

        # проверка на ввод символы и цифры
        par_chek = QRegExp("[A-zA-Z0-9]{6}")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(par_chek)
        self.lineEdit_parol.setValidator(pValidator)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Викторина"))
        self.label.setText(_translate("MainWindow", "ВИКТОРИНА"))
        self.label_2.setText(_translate("MainWindow", "COSMO"))
        self.label_3.setText(_translate("MainWindow", "вход"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600;\">Еще не зарегистрированы?</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Введите логин"))
        self.label_6.setText(_translate("MainWindow", "Введите пароль"))
        self.pushButton.setText(_translate("MainWindow", "регистрация"))
        self.pushButton_2.setText(_translate("MainWindow", "Начать викторину"))
        self.pushButton_3.setText(_translate("MainWindow", "правила"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
