import Pyro5.client
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime

account_data = None

def user_profile(self, username):
    self.ui.dash.setCurrentWidget(self.ui.profilo)
    set_personal_data(self, username)
     
def show_popup_msg_delete(self):
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Critical)
        msg.setStyleSheet("color:black;background:white") 
        reply = QMessageBox.question(self, 'ATTENZIONE', 'Sei sicuro di voler eliminare questo messaggio?',
        QMessageBox.Yes | QMessageBox.No) 
        if reply == QMessageBox.Yes:
            return True 

def set_personal_data(self, username):
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
    self.ui.dati_personali.addItem("HOBBY:  " + data["tempo libero"])
    self.ui.dati_personali.addItem("ISCRIZIONE:  " + str(data["iscrizione"]))  
    self.ui.dati_personali.addItem("SEGUITI:  " + str(data["seguiti"]))
    self.ui.dati_personali.addItem("SEGUACI:  " + str(data["seguaci"]))    
    self.ui.personal_msg_title.setText("MESSAGGI PUBBLICATI: " + str(len(data["messaggi"])))
    msg_to_order = []
    for msg in data["messaggi"]:
        msg_to_order.append(msg)
    
    list_ordered = sorted(msg_to_order, key=lambda x: datetime.strptime(x['data'], '%Y-%m-%d %H:%M:%S'), reverse = True)

    for i in list_ordered:
        time = datetime.strptime(i["data"], '%Y-%m-%d %H:%M:%S')        
        self.ui.personal_msg.addItem(i["testo"] + "\n" + str(time.strftime("%H:%M  %d-%m-%Y")))     
    
def set_mod_data(self, username):
    data_field = self.ui.combo_mod_dati.currentText().lower()
    data = self.ui.data_mod.text() 
    time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    reg = Pyro5.client.Proxy("PYRONAME:mythingy")
    success = reg.mod_personal_data([username, data_field, data, time])

    if data_field == "nome":
        self.ui.dati_personali.item(1).setText("NOME:  " +data)
    if data_field == "cognome":
        self.ui.dati_personali.item(2).setText("COGNOME:  " +data)
    if data_field == "eta":
        self.ui.dati_personali.item(3).setText("ETA:  " +data)
    if data_field == "sesso":
        self.ui.dati_personali.item(4).setText("SESSO:  " +data)
    if data_field == "nazionalita":
        self.ui.dati_personali.item(5).setText("NAZIONALITA:  " +data)
    if data_field == "citta":
        self.ui.dati_personali.item(6).setText("CITTA:  " +data)
    if data_field == "hobby":
        self.ui.dati_personali.item(7).setText("HOBBY:  " +data)

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

def del_msg(self, username):   
    global account_data
    current_row = self.ui.personal_msg.currentRow()
    if (current_row > -1):
        
        msg_to_order = []
        for msg in account_data["messaggi"]:
            msg_to_order.append(msg)
            
        list_ordered = sorted(msg_to_order, key=lambda x: datetime.strptime(x['data'], '%Y-%m-%d %H:%M:%S'), reverse = True)

        for i in list_ordered:
            self.ui.utente_msg_list.addItem(i["testo"] + "\n" + str(i["data"]))           
        
        if(show_popup_msg_delete(self)):
            reg = Pyro5.client.Proxy("PYRONAME:mythingy")
            success = reg.delete_msg([username, list_ordered[current_row]["data"]])
        
            if(success):
                msg = QMessageBox() 
                msg.setIcon(QMessageBox.Information)
                msg.setText("Messaggio eliminato correttamente")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setStyleSheet("color:black;background:white") 
                x = msg.exec_()
                self.ui.personal_msg.takeItem(current_row)
            else:
                msg = QMessageBox() 
                msg.setIcon(QMessageBox.Information)
                msg.setText("Riprova, qualcosa è andato storto")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setStyleSheet("color:black;background:white") 
                x = msg.exec_()  
    else:
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Information)
        msg.setText("Devi selezionare un messaggio per eliminarlo")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setStyleSheet("color:black;background:white") 
        x = msg.exec_()
        
    