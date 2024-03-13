from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import Pyro5.client
import Pyro5.core
import Pyro5.api
import sys
from datetime import datetime

from login import Ui_MainWindow
import bacheca, utenti, profilo, client_style, eventi

global active_user

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):       
        super(MainWindow, self).__init__() 
        self.ui = Ui_MainWindow()               
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.login) 

        client_style.login_style(self) 
        client_style.register_style(self) 
        client_style.user_style(self)
        client_style.events_style(self)
        client_style.notice_board_style(self) 
        client_style.profile_style(self) 
        client_style.dashboard_style(self) 

        global active_user
        self.ui.login_btn.clicked.connect(lambda: user_login(self))
        self.ui.register_btn.clicked.connect(lambda: user_register(self))
        self.ui.register_new_btn.clicked.connect(lambda: new_user(self))
        self.ui.login_back_btn.clicked.connect(lambda: back_to_login(self))
        self.ui.logout_btn.clicked.connect(lambda: logout(self))
        self.ui.bacheca_btn.clicked.connect(lambda: bacheca.set_bacheca(self, active_user))
        self.ui.post_btn.clicked.connect(lambda: bacheca.post_msg(self, active_user))
        self.ui.seguiti_btn.clicked.connect(lambda: utenti.set_user(self, active_user))
        self.ui.cerca_btn.clicked.connect(lambda: utenti.search(self, active_user))
        self.ui.follow_btn.clicked.connect(lambda: utenti.follow(self, active_user))
        self.ui.profilo_dati_btn.clicked.connect(lambda: profilo.set_personal_data(self, active_user))
        self.ui.mod_data_btn.clicked.connect(lambda: profilo.set_mod_data(self, active_user))
        self.ui.el_sel_msg.clicked.connect(lambda: profilo.del_msg(self, active_user))
        self.ui.profilo_dati_btn.clicked.connect(lambda: profilo.user_profile(self, active_user))
        self.ui.notifiche_btn.clicked.connect(lambda: eventi.set_events(self, active_user))

def logout(self):
    msg = QMessageBox() 
    msg.setIcon(QMessageBox.Critical)
    msg.setStyleSheet("color:black;background:white") 
    reply = QMessageBox.question(self, 'ATTENZIONE', 'Sei sicuro di voler uscire dal tuo account?',
    QMessageBox.Yes | QMessageBox.No) 
    if reply == QMessageBox.Yes:
        self.ui.stackedWidget.setCurrentWidget(self.ui.login)
        self.ui.username.clear()
        self.ui.password.clear()
        self.ui.user_pass_err.clear()

def user_login(self):
    username = self.ui.username.text()
    password = self.ui.password.text() 
    global active_user 
    active_user = None
    if len(username) > 0 and len(password) > 0:
        log = Pyro5.client.Proxy("PYRONAME:mythingy")
        success = log.login([username, password]) 
        
        if (success == "USER_OK"):
            active_user = username           
            bacheca.set_bacheca(self, active_user)
        else:
            self.ui.user_pass_err.setText("NOME UTENTE/PASSWORD ERRATI")        
    else: 
        self.ui.user_pass_err.setText("NOME UTENTE/PASSWORD MANCANTI")      

def new_user(self):
    username = self.ui.username_reg.text()
    password = self.ui.password_reg.text() 
    self.ui.user_pass_err_reg.setText("") 

    if len(username) > 0 and len(username) < 11 and len(password) > 0 and len(password) < 11:
        data = datetime.utcnow().strftime("%d-%m-%Y")
        reg = Pyro5.client.Proxy("PYRONAME:mythingy")
        success = reg.register([username, password, data]) 
        
        if (success == "DUPLICATO"):
            self.ui.user_pass_err_reg.setStyleSheet("QLineEdit { background-color: #e7e7e7; color: red;}")
            self.ui.user_pass_err_reg.setText("ERRORE - NOME UTENTE ESISTENTE")
        else:
            if(success == "INSERITO"):
                    self.ui.user_pass_err_reg.setStyleSheet("QLineEdit { background-color: #e7e7e7; color: green;}")
                    self.ui.user_pass_err_reg.setText("PROFILO CREATO CORRETTAMENTE")
            else:
                self.ui.user_pass_err_reg.setStyleSheet("QLineEdit { background-color: #e7e7e7; color: red;}")
                self.ui.user_pass_err_reg.setText("ERRORE D'INSERIMENTO - RIPROVA")        
    else: 
        self.ui.user_pass_err_reg.setStyleSheet("QLineEdit { background-color: #e7e7e7; color: red;}")
        self.ui.user_pass_err_reg.setText("INSERISCI NOME UTENTE/PASSWORD")  

def user_register(self):
    self.ui.stackedWidget.setCurrentWidget(self.ui.registration)

def back_to_login(self):
    self.ui.username_reg.setText("")
    self.ui.password_reg.setText("")
    self.ui.user_pass_err_reg.setText("")
    self.ui.stackedWidget.setCurrentWidget(self.ui.login)
    
app = QtWidgets.QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setWindowTitle("DISTRIBUTED SOCIAL") 
widget.showMaximized() 
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("exit")
