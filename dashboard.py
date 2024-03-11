import Pyro5.client
from PyQt5.QtWidgets import QMessageBox

import client_style 
import profilo, utenti, bacheca


def main_dashboard(self, username):
    self.ui.stackedWidget.setCurrentWidget(self.ui.dashboard)
    client_style.dashboard_style(self)
    self.ui.dash.setCurrentWidget(self.ui.bacheca)
    bacheca.set_bacheca(self, username)
        
    self.ui.profilo_dati_btn.clicked.connect(lambda: profilo.profilo_utente(self, username))
    self.ui.seguiti_btn.clicked.connect(lambda: utenti.set_utenti(self, username))
    self.ui.bacheca_btn.clicked.connect(lambda: bacheca.set_bacheca(self, username))
    self.ui.logout_btn.clicked.connect(lambda: back_to_login(self))

def show_popup_exit(self):
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Critical)
        msg.setStyleSheet("color:black;background:white") 
        reply = QMessageBox.question(self, 'ATTENZIONE', 'Sei sicuro di voler uscire dal tuo account?',
        QMessageBox.Yes | QMessageBox.No) 
        if reply == QMessageBox.Yes:
            return True 
        
def back_to_login(self):
    exit = show_popup_exit(self)
    if(exit):
        self.ui.stackedWidget.setCurrentWidget(self.ui.login)

