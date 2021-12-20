

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Rules(object):
    def setupUi(self, Rules):
        Rules.setObjectName("Rules")
        Rules.resize(1091, 709)
        self.centralwidget = QtWidgets.QWidget(Rules)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 90, 1071, 551))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 20, 241, 51))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        Rules.setCentralWidget(self.centralwidget)

        self.retranslateUi(Rules)
        QtCore.QMetaObject.connectSlotsByName(Rules)

    def retranslateUi(self, Rules):
        _translate = QtCore.QCoreApplication.translate
        Rules.setWindowTitle(_translate("Rules", "Правила"))
        self.label.setText(_translate("Rules", "<html><head/><body><p><span style=\" font-size:10pt;\">Викторина, "
                                               "состоящая из 10 вопросов на различные темы. </span></p><p><span "
                                               "style=\" font-size:10pt;\">-Вопросы генерируются рандомно при каждом "
                                               "новом прохождении игры. </span></p><p align=\"justify\"><span "
                                               "style=\" font-size:10pt;\">-Вопросы с 1ого по 8ой включительно "
                                               "являются более упрощенными. "
                                               "</span></p><p align=\"justify\"><span style=\" font-size:10pt;\">"
                                               ".</span></p><p><span style=\" font-size:10pt;\">-Вопросы с 9ого "
                                               "по 10ый включительно – усложненные, в них пользователь должен сам "
                                               "вписать ответ в отведенный для ответа блок. </span></p><p><span "
                                               "style=\" font-size:10pt;\"></span></p><p><span style=\" "
                                               "font-size:10pt;\">- Максимальное кол-во баллов за викторину: 10 "
                                               "баллов.</span></p><p><span style=\" font-size:10pt;\">- В базе данных "
                                               "упрощенных вопросов будет храниться 20 штук, усложненных – "
                                               "10.</span></p><p><span style=\" "
                                               "font-size:10pt;\"><br/></span></p><p><span style=\" "
                                               "font-size:10pt;\">При открытии интерфейса пользователь должен либо "
                                               "ввести свое уникальное имя и пароль, которое он сохранил при "
                                               "регистрации, </span></p><p><span style=\" font-size:10pt;\">либо если "
                                               "этого еще не произошло, зарегистрироваться. После этого он отвечает "
                                               "на 10 вопросов."
                                               "</span></p><p><span style=\" font-size:10pt;\">При окончании "
                                               "прохождении викторины визуализируется прогресс в графике, "
                                               "с шкалой номера попытки прохождения и кол-ва</span></p><p><span "
                                               "style=\" font-size:10pt;\"> набранных баллов пользователем за "
                                               "попытки, когда он проходил эту игру.</span></p><p><span style=\" "
                                               "font-size:10pt;\"><br/></span></p></body></html>"))
        self.label_2.setText(_translate("Rules", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Правила викторины:</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Rules = QtWidgets.QMainWindow()
    ui = Ui_Rules()
    ui.setupUi(Rules)
    Rules.show()
    sys.exit(app.exec_())
