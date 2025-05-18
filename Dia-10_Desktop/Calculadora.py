import sys
from PyQt5 import QtWidgets, uic, QtCore

class Ui_MainWindow(QtWidgets.QMainWindow):
    result = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(249, 353)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #2c2c2c;")
        self.centralwidget.setObjectName("centralwidget")
        self.btnNumero7 = QtWidgets.QPushButton(self.centralwidget)
        self.btnNumero7.setGeometry(QtCore.QRect(10, 150, 51, 41))
        self.btnNumero7.setStyleSheet("background-color: #868382; border: none; border-radius: 5px;")
        self.btnNumero7.setObjectName("btnNumero7")
        self.btnNumero8 = QtWidgets.QPushButton(self.centralwidget)
        self.btnNumero8.setGeometry(QtCore.QRect(70, 150, 51, 41))
        self.btnNumero8.setStyleSheet("background-color: #868382; border: none; border-radius: 5px;")
        self.btnNumero8.setObjectName("btnNumero8")
        self.btnNumero9 = QtWidgets.QPushButton(self.centralwidget)
        self.btnNumero9.setGeometry(QtCore.QRect(130, 150, 51, 41))
        self.btnNumero9.setStyleSheet("background-color: #868382; border: none; border-radius: 5px;")
        self.btnNumero9.setObjectName("btnNumero9")
        self.btnNumero6 = QtWidgets.QPushButton(self.centralwidget)
        self.btnNumero6.setGeometry(QtCore.QRect(130, 200, 51, 41))
        self.btnNumero6.setStyleSheet("background-color: #868382; border: none; border-radius: 5px;")
        self.btnNumero6.setObjectName("btnNumero6")
        self.btnNumero5 = QtWidgets.QPushButton(self.centralwidget)
        self.btnNumero5.setGeometry(QtCore.QRect(70, 200, 51, 41))
        self.btnNumero5.setStyleSheet("background-color: #868382; border: none; border-radius: 5px;")
        self.btnNumero5.setObjectName("btnNumero5")
        self.btnNumero4 = QtWidgets.QPushButton(self.centralwidget)
        self.btnNumero4.setGeometry(QtCore.QRect(10, 200, 51, 41))
        self.btnNumero4.setStyleSheet("background-color: #868382; border: none; border-radius: 5px;")
        self.btnNumero4.setObjectName("btnNumero4")
        self.btnDot = QtWidgets.QPushButton(self.centralwidget)
        self.btnDot.setGeometry(QtCore.QRect(130, 300, 51, 41))
        self.btnDot.setStyleSheet("background-color: #424242; border: none; border-radius: 5px;")
        self.btnDot.setObjectName("btnDot")
        self.btnBackSpace = QtWidgets.QPushButton(self.centralwidget)
        self.btnBackSpace.setGeometry(QtCore.QRect(190, 150, 51, 41))
        self.btnBackSpace.setStyleSheet("background-color: #424242; border: none; border-radius: 5px;")
        self.btnBackSpace.setObjectName("btnBackSpace")
        self.btnNumero3 = QtWidgets.QPushButton(self.centralwidget)
        self.btnNumero3.setGeometry(QtCore.QRect(130, 250, 51, 41))
        self.btnNumero3.setStyleSheet("background-color: #868382; border: none; border-radius: 5px;")
        self.btnNumero3.setObjectName("btnNumero3")
        self.btnNumero0 = QtWidgets.QPushButton(self.centralwidget)
        self.btnNumero0.setGeometry(QtCore.QRect(70, 300, 51, 41))
        self.btnNumero0.setStyleSheet("background-color: #868382; border: none; border-radius: 5px;")
        self.btnNumero0.setObjectName("btnNumero0")
        self.btnNumero2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnNumero2.setGeometry(QtCore.QRect(70, 250, 51, 41))
        self.btnNumero2.setStyleSheet("background-color: #868382; border: none; border-radius: 5px;")
        self.btnNumero2.setObjectName("btnNumero2")
        self.btnNumero1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnNumero1.setGeometry(QtCore.QRect(10, 250, 51, 41))
        self.btnNumero1.setStyleSheet("background-color: #868382; border: none; border-radius: 5px;")
        self.btnNumero1.setObjectName("btnNumero1")
        self.btnMinus = QtWidgets.QPushButton(self.centralwidget)
        self.btnMinus.setGeometry(QtCore.QRect(130, 100, 51, 41))
        self.btnMinus.setStyleSheet("background-color: #424242; border: none; border-radius: 5px;")
        self.btnMinus.setObjectName("btnMinus")
        self.btnSum = QtWidgets.QPushButton(self.centralwidget)
        self.btnSum.setGeometry(QtCore.QRect(190, 100, 51, 41))
        self.btnSum.setStyleSheet("background-color: #424242; border: none; border-radius: 5px;")
        self.btnSum.setObjectName("btnSum")
        self.btnMult = QtWidgets.QPushButton(self.centralwidget)
        self.btnMult.setGeometry(QtCore.QRect(70, 100, 51, 41))
        self.btnMult.setStyleSheet("background-color: #424242; border: none; border-radius: 5px;")
        self.btnMult.setObjectName("btnMult")
        self.btnDiv = QtWidgets.QPushButton(self.centralwidget)
        self.btnDiv.setGeometry(QtCore.QRect(10, 100, 51, 41))
        self.btnDiv.setStyleSheet("background-color: #424242; border: none; border-radius: 5px;")
        self.btnDiv.setObjectName("btnDiv")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(10, 300, 51, 41))
        self.btnCancel.setStyleSheet("background-color: #424242; border: none; border-radius: 5px;")
        self.btnCancel.setObjectName("btnCancel")
        self.btnEquals = QtWidgets.QPushButton(self.centralwidget)
        self.btnEquals.setGeometry(QtCore.QRect(190, 200, 51, 141))
        self.btnEquals.setStyleSheet("background-color: #e9734c; border: none; border-radius: 5px;")
        self.btnEquals.setObjectName("btnEquals")
        self.lblResult = QtWidgets.QLabel(self.centralwidget)
        self.lblResult.setGeometry(QtCore.QRect(0, 10, 251, 71))
        self.lblResult.setStyleSheet("background-color: #3d3d3d; padding:5px; font-size:30px;")
        self.lblResult.setText("0")
        self.lblResult.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        # self.lblResult.setAlignment(QtCore.Qt.Qt::AlignmentFlag::AlignRight|QtCore.Qt.Qt::AlignmentFlag::AlignTrailing|QtCore.Qt.Qt::AlignmentFlag::AlignVCenter)
        self.lblResult.setObjectName("lblResult")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        for btn in [self.btnNumero0, self.btnNumero1, self.btnNumero2,
                    self.btnNumero3, self.btnNumero4, self.btnNumero5,
                    self.btnNumero6, self.btnNumero7, self.btnNumero8,
                    self.btnNumero9, self.btnDot, self.btnMinus,
                    self.btnSum, self.btnMult, self.btnDiv,
                    self.btnCancel, self.btnBackSpace, self.btnEquals]:
            btn.clicked.connect(self.mostrarNumero)
            btn.setCursor(QtCore.Qt.PointingHandCursor)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora"))
        self.btnNumero7.setText(_translate("MainWindow", "7"))
        self.btnNumero8.setText(_translate("MainWindow", "8"))
        self.btnNumero9.setText(_translate("MainWindow", "9"))
        self.btnNumero6.setText(_translate("MainWindow", "6"))
        self.btnNumero5.setText(_translate("MainWindow", "5"))
        self.btnNumero4.setText(_translate("MainWindow", "4"))
        self.btnDot.setText(_translate("MainWindow", "."))
        self.btnBackSpace.setText(_translate("MainWindow", "⌫"))
        self.btnNumero3.setText(_translate("MainWindow", "3"))
        self.btnNumero0.setText(_translate("MainWindow", "0"))
        self.btnNumero2.setText(_translate("MainWindow", "2"))
        self.btnNumero1.setText(_translate("MainWindow", "1"))
        self.btnMinus.setText(_translate("MainWindow", "-"))
        self.btnSum.setText(_translate("MainWindow", "+"))
        self.btnMult.setText(_translate("MainWindow", "x"))
        self.btnDiv.setText(_translate("MainWindow", "/"))
        self.btnCancel.setText(_translate("MainWindow", "C"))
        self.btnEquals.setText(_translate("MainWindow", "="))

    def mostrarNumero(self):
        sender = self.sender()
        if sender.text() == ".":
            if "." in self.lblResult.text():
                return
            elif self.lblResult.text() == "":
                self.lblResult.setText("0.")
            else:
                self.lblResult.setText(self.lblResult.text() + ".")
        elif sender.text() == "C":
            self.limpar()
        elif sender.text() == "⌫":
            if self.lblResult.text() == "0":
                return
            else:
                self.lblResult.setText(self.lblResult.text()[:-1])
                if self.lblResult.text() == "":
                    self.lblResult.setText("0")
        elif sender.text() in ["+", "-", "x", "/"]:
            if self.lblResult.text() == "0":
                return
            elif self.lblResult.text()[-1] in ["+", "-", "x", "/"]:
                self.lblResult.setText(self.lblResult.text()[:-1] + sender.text())
            else:
                self.lblResult.setText(self.lblResult.text() + sender.text())
        elif self.sender().text() == "=":
            if self.lblResult.text() == "0" and self.lblResult.text() == "Erro":
                return
            if ("+" not in self.lblResult.text() and
               "-" not in self.lblResult.text() and
               "x" not in self.lblResult.text() and
               "/" not in self.lblResult.text()):
                if self.lblResult.text() == "0":
                    self.lblResult.setText("0")
                elif self.lblResult.text() == "Erro":
                    self.lblResult.setText("0")
                else:
                    return
            else:
                if self.lblResult.text() == "0":
                    self.lblResult.setText("0")
                elif self.lblResult.text() == "Erro":
                    self.lblResult.setText("0")
                elif self.lblResult.text()[-1] in ["+", "-", "x", "/", "."]:
                    self.lblResult.setText(self.lblResult.text()[:-1])
                self.calcular()
        else:
            if self.lblResult.text() == "0" or self.lblResult.text() == "Erro":
                self.lblResult.setText(sender.text())
            else:
                if self.result:
                    self.lblResult.setText(sender.text())
                    self.result = False
                else:
                    self.lblResult.setText(self.lblResult.text() + sender.text())

    def limpar(self):
        self.lblResult.setText("0")

    def calcular(self):
        try:
            expressao = self.lblResult.text()
            expressao = expressao.replace("x", "*")
            resultado = eval(expressao)
            self.lblResult.setText(str(resultado))
            self.result = True
        except Exception as e:
            self.lblResult.setText("Erro")
            print(f"Error ao calcular: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())