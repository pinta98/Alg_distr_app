import Pyro5.client
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QPushButton


def main_dashboard(self, username):
    self.ui.stackedWidget.setCurrentWidget(self.ui.dashboard)
    self.ui.mod_data_btn.clicked.connect(lambda: set_mod_data(self, username))
    self.ui.profilo_dati.clicked.connect(lambda: set_personal_data(self, username))


def set_personal_data(self, username):
    self.ui.dati_personali.clear()
    reg = Pyro5.client.Proxy("PYRONAME:mythingy")
    data = reg.personal_data(username) 
    self.ui.dati_personali.addItem("NOME UTENTE:  " + data["username"])
    self.ui.dati_personali.addItem("NOME:  " + data["nome"])
    self.ui.dati_personali.addItem("COGNOME:  " + data["cognome"])
    self.ui.dati_personali.addItem("ETA :  " + data["eta"])
    self.ui.dati_personali.addItem("SESSO:  " + data["sesso"])
    self.ui.dati_personali.addItem("NAZIONALITA :  " + data["nazionalita"])
    self.ui.dati_personali.addItem("CITTA :  " + data["citta"])
    self.ui.dati_personali.addItem("TEMPO LIBERO:  " + data["hobby"])
    self.ui.dati_personali.addItem("DATA D'ISCRIZIONE:  " + data["iscrizione"])

def set_mod_data(self, username):
    data_field = self.ui.combo_mod_dati.currentText().lower()
    data = self.ui.data_mod.text() 
    reg = Pyro5.client.Proxy("PYRONAME:mythingy")
    success = reg.mod_personal_data([username, data_field, data])
    if(success):
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Information)
        msg.setText(data_field.upper() + " ha subito una modifica correttamente")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setStyleSheet("color:black;background:white") 
        x = msg.exec_()
    else:
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Information)
        msg.setText("Riprova, qualcosa è andato storto")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setStyleSheet("color:black;background:white") 
        x = msg.exec_()

    set_personal_data(self, username)