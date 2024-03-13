import Pyro5.client
from datetime import datetime
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont

def set_bacheca(self, username):
    self.ui.stackedWidget.setCurrentWidget(self.ui.dashboard)
    self.ui.dash.setCurrentWidget(self.ui.bacheca)  
    set_msg(self, username)

def set_msg(self, username):
    self.ui.table_bacheca.clear() 
    self.ui.post_msg.clear()   
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
        if(msg["user"] == username): 
            font = QFont()
            font.setBold(True)
            self.ui.table_bacheca.setItem(row, 0, QtWidgets.QTableWidgetItem(msg["user"])) 
            self.ui.table_bacheca.item(row, 0).setFont(font)            
            self.ui.table_bacheca.setItem(row, 1, QtWidgets.QTableWidgetItem(msg["testo"])) 
            #self.ui.table_bacheca.item(row, 1).setFont(font)                   
        else:
            self.ui.table_bacheca.setItem(row, 0, QtWidgets.QTableWidgetItem(msg["user"])) 
            self.ui.table_bacheca.setItem(row, 1, QtWidgets.QTableWidgetItem(msg["testo"]))  
        time = datetime.strptime(msg["data"], '%Y-%m-%d %H:%M:%S')    
        self.ui.table_bacheca.setItem(row, 2, QtWidgets.QTableWidgetItem(str(time.strftime("%H:%M  %d-%m-%Y"))))  

        row = row + 1                                                                           
   
def post_msg(self, username):
    msg = self.ui.post_msg.text()
    data = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    reg = Pyro5.client.Proxy("PYRONAME:mythingy")
    data = reg.publish_msg([username, msg, data]) 
    set_msg(self, username)
