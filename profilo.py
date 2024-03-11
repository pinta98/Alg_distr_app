import Pyro5.client
from PyQt5.QtWidgets import QMessageBox
import client_style
from datetime import datetime

account_data = None

def profilo_utente(self, username):
    self.ui.dash.setCurrentWidget(self.ui.profilo)
    set_personal_data(self, username)
    self.ui.profilo_dati_btn.clicked.connect(lambda: set_personal_data(self, username))
    self.ui.mod_data_btn.clicked.connect(lambda: set_mod_data(self, username))
    self.ui.el_sel_msg.clicked.connect(lambda: del_msg(self, username))
     
def show_popup_msg_delete(self):
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Critical)
        msg.setStyleSheet("color:black;background:white") 
        reply = QMessageBox.question(self, 'ATTENZIONE', 'Sei sicuro di voler eliminare questo messaggio?',
        QMessageBox.Yes | QMessageBox.No) 
        if reply == QMessageBox.Yes:
            return True 

def set_personal_data(self, username):
    client_style.profilo_style(self) 
    global account_data
    self.ui.dati_personali.clear()
    self.ui.personal_msg.clear()
    reg = Pyro5.client.Proxy("PYRONAME:mythingy")
    data = reg.personal_data(username) 
    account_data = data
    self.ui.dati_personali.addItem("NOME UTENTE:  " + data["username"])
    self.ui.dati_personali.addItem("NOME:  " + data["nome"])
    self.ui.dati_personali.addItem("COGNOME:  " + data["cognome"])
    self.ui.dati_personali.addItem("ETA :  " + data["eta"])
    self.ui.dati_personali.addItem("SESSO:  " + data["sesso"])
    self.ui.dati_personali.addItem("NAZIONALITA :  " + data["nazionalita"])
    self.ui.dati_personali.addItem("CITTA :  " + data["citta"])
    self.ui.dati_personali.addItem("TEMPO LIBERO:  " + data["tempo libero"])
    self.ui.dati_personali.addItem("DATA D'ISCRIZIONE:  " + data["iscrizione"])
    self.ui.dati_personali.addItem("SEGUITI:  " + str(data["seguiti"]))
    self.ui.dati_personali.addItem("SEGUACI:  " + str(data["seguaci"]))
    
    msg_to_order = []
    for msg in data["messaggi"]:
        msg_to_order.append(msg)
    
    list_ordered = sorted(msg_to_order, key=lambda x: datetime.strptime(x['data'], '%Y-%m-%d %H:%M:%S'), reverse = True)

    for i in list_ordered:
        self.ui.personal_msg.addItem(i["testo"] + "\n" + str(i["data"]))     
    
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

def del_msg(self, username):   
    global account_data
    current_row = self.ui.personal_msg.currentRow()
    if (current_row > -1):
        to_delete = len(account_data["messaggi"]) - current_row - 1
        id_msg = []
        i = len(account_data["messaggi"])   
        for a in account_data["messaggi"].keys():
            id_msg.append(a)          
        if(show_popup_msg_delete(self)):
            reg = Pyro5.client.Proxy("PYRONAME:mythingy")
            success = reg.delete_msg([username, id_msg[to_delete], account_data["messaggi"][str(id_msg[to_delete])]["testo"]])
            if(success):
                msg = QMessageBox() 
                msg.setIcon(QMessageBox.Information)
                msg.setText("Messaggio eliminato correttamente")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setStyleSheet("color:black;background:white") 
                x = msg.exec_()
                set_personal_data(self, username)
            else:
                msg = QMessageBox() 
                msg.setIcon(QMessageBox.Information)
                msg.setText("Riprova, qualcosa è andato storto")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setStyleSheet("color:black;background:white") 
                x = msg.exec_()
                set_personal_data(self, username)     
    else:
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Information)
        msg.setText("Devi selezionare un messaggio per eliminarlo")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setStyleSheet("color:black;background:white") 
        x = msg.exec_()
        
    