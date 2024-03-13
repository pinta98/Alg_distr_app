import client_style
import Pyro5.client
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton
from datetime import datetime

def set_events(self, username):
    self.ui.dash.setCurrentWidget(self.ui.notifiche)  
    self.ui.table_eventi.clear()
    self.ui.dati_personali_eventi.clear()
    reg = Pyro5.client.Proxy("PYRONAME:mythingy")
    data = reg.personal_data(username)
    msg_to_order = []
    for notifica in data["notifiche"]:
        msg_to_order.append(notifica)
    row=0
    list_ordered = sorted(msg_to_order, key=lambda x: datetime.strptime(x['data'], '%Y-%m-%d %H:%M:%S'), reverse = True)
    self.ui.table_eventi.setRowCount(len(list_ordered)) 

    for msg in list_ordered:
        time = datetime.strptime(msg["data"], '%Y-%m-%d %H:%M:%S')    
        self.ui.table_eventi.setItem(row, 0, QtWidgets.QTableWidgetItem(str(time.strftime("%H:%M %d-%m-%Y")))) 
        self.ui.table_eventi.setItem(row, 1, QtWidgets.QTableWidgetItem(msg["testo"]))
        
        if (msg["show"] == True):
            user_btn = QPushButton("PROFILO", self) 
            client_style.profile_btn_style(user_btn)                      
            self.ui.table_eventi.setCellWidget(row, 2, user_btn)        
            user_btn.clicked.connect(lambda checked, i=row: notification_profile(self, i, list_ordered))

        row = row+1
    
def notification_profile(self, i, user):
    self.ui.dati_personali_eventi.clear()
    reg = Pyro5.client.Proxy("PYRONAME:mythingy")
    data = reg.personal_data(user[i]["utente"]) 
    self.ui.dati_personali_eventi.addItem("NOME UTENTE:  " + data["username"])
    self.ui.dati_personali_eventi.addItem("NOME:  " + data["nome"])
    self.ui.dati_personali_eventi.addItem("COGNOME:  " + data["cognome"])
    self.ui.dati_personali_eventi.addItem("ETA :  " + data["eta"])
    self.ui.dati_personali_eventi.addItem("SESSO:  " + data["sesso"])
    self.ui.dati_personali_eventi.addItem("NAZIONALITA :  " + data["nazionalita"])
    self.ui.dati_personali_eventi.addItem("CITTA :  " + data["citta"])
    self.ui.dati_personali_eventi.addItem("TEMPO LIBERO:  " + data["tempo libero"])
    self.ui.dati_personali_eventi.addItem("ISCRIZIONE:  " + data["iscrizione"])
    self.ui.dati_personali_eventi.addItem("SEGUITI:  " + str(data["seguiti"]))
    self.ui.dati_personali_eventi.addItem("SEGUACI:  " + str(data["seguaci"]))
    self.ui.dati_personali_eventi.addItem("MESSAGGI:  " + str(len(data["messaggi"])))
    