from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QPushButton, QWidget
import Pyro5.client
import sys

from login import Ui_MainWindow
from client_style import login_style, register_style
import dashboard



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):        
        super(MainWindow, self).__init__() 
        self.ui = Ui_MainWindow()     
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.login) 

        login_style(self) 
        register_style(self) 

        self.ui.login_btn.clicked.connect(lambda: user_login(self))
        self.ui.register_btn.clicked.connect(lambda: user_register(self))
        self.ui.register_new_btn.clicked.connect(lambda: new_user(self))
        self.ui.login_back_btn.clicked.connect(lambda: back_to_login(self))

        

def user_login(self):
    username = self.ui.username.text()
    password = self.ui.password.text() 

    if len(username) > 0 and len(password) > 0:
        log = Pyro5.client.Proxy("PYRONAME:mythingy")
        success = log.login([username, password]) 
        
        if (success == "USER_OK"):
            dashboard.main_dashboard(self, username)
        else:
            self.ui.user_pass_err.setText("NOME UTENTE/PASSWORD ERRATI")        
    else: 
        self.ui.user_pass_err.setText("NOME UTENTE/PASSWORD ERRATI")      

def new_user(self):
    username = self.ui.username_reg.text()
    password = self.ui.password_reg.text() 
    self.ui.user_pass_err_reg.setText("") 

    if len(username) > 0 and len(password) > 0:
        reg = Pyro5.client.Proxy("PYRONAME:mythingy")
        success = reg.register([username, password]) 
        
        if (success == "DUPLICATO"):
            self.ui.user_pass_err_reg.setStyleSheet("QLineEdit { background-color: #e7e7e7; color: red;}")
            self.ui.user_pass_err_reg.setText("ERRORE - NOME UTENTE ESISTENTE")
        else:
            if(success == "INSERITO"):
                    self.ui.user_pass_err_reg.setStyleSheet("QLineEdit { background-color: #e7e7e7; color: green;}")
                    self.ui.user_pass_err_reg.setText("ACCOUNT CREATO CORRETTAMENTE")
            else:
                self.ui.user_pass_err_reg.setStyleSheet("QLineEdit { background-color: #e7e7e7; color: red;}")
                self.ui.user_pass_err_reg.setText("ERRORE D'INSERIMENTO - RIPROVA")        
    else: 
        self.ui.user_pass_err_reg.setStyleSheet("QLineEdit { background-color: #e7e7e7; color: red;}")
        self.ui.user_pass_err_reg.setText("INSERISCI NOME UTENTE/PASSWORD")  




def user_register(self):
    self.ui.stackedWidget.setCurrentWidget(self.ui.registration)

def back_to_login(self):
    self.ui.stackedWidget.setCurrentWidget(self.ui.login)

    


app = QtWidgets.QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setWindowTitle("DARE UN NOME AL SOCIAL") 
widget.showMaximized() 
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("exit")



