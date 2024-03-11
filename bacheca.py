import Pyro5.client
from PyQt5.QtWidgets import QMessageBox
import client_style
from datetime import datetime
from PyQt5 import QtWidgets

def set_bacheca(self, username):
    self.ui.dash.setCurrentWidget(self.ui.bacheca)  
    client_style.bacheca_syle(self)    
    self.ui.post_btn.clicked.connect(lambda: post_msg(self, username))
    set_msg(self, username)
    

def set_msg(self, username):
    client_style.bacheca_syle(self)
    self.ui.table_bacheca.clear()    
    reg = Pyro5.client.Proxy("PYRONAME:mythingy")
    data = reg.get_followed_msg(username) 
    msg_to_order = []
    for k in data:
            for msg in data[k]:   
                if(len(msg) > 0):                
                    msg_to_order.append(msg)
    
    list_ordered = sorted(msg_to_order, key=lambda x: datetime.strptime(x['data'], '%Y-%m-%d %H:%M:%S'), reverse = True)
   
    self.ui.table_bacheca.setRowCount(len(list_ordered)) 
    row=0
    for msg in list_ordered:  
        self.ui.table_bacheca.setItem(row, 0, QtWidgets.QTableWidgetItem(msg["user"]))   
        self.ui.table_bacheca.setItem(row, 1, QtWidgets.QTableWidgetItem(msg["testo"])) 
        self.ui.table_bacheca.setItem(row, 2, QtWidgets.QTableWidgetItem(msg["data"]))  

        row = row + 1                                                                           
   
def post_msg(self, username):
    msg = self.ui.post_msg.text()
    data = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    reg = Pyro5.client.Proxy("PYRONAME:mythingy")
    data = reg.publish_msg([username, msg, data]) 
    set_msg(self, username)
    #self.ui.post_msg.setText(data)
