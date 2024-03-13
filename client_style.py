from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import  QStyledItemDelegate

class ReadOnly(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return
    
def login_style(self):
    self.ui.login_btn.setStyleSheet('QPushButton {background-color: white; color: black; border-radius: 8px; border: 1px solid black;}'
                           "QPushButton:pressed { background-color: grey; color: white; }")
    self.ui.register_btn.setStyleSheet('QPushButton {background-color: white; color: black; border-radius: 8px; border: 1px solid black;}'
                           "QPushButton:pressed { background-color: grey; color: white;}")
    self.ui.login_frame.setStyleSheet("QFrame {background-color: #e7e7e7; border-radius: 8px; border: 1px solid black;}")
    self.ui.label_pass_login.setStyleSheet("QLabel { border: 0}")
    self.ui.label_user_login.setStyleSheet("QLabel { border: 0}")
    self.ui.title_log.setStyleSheet("QLabel { border: 0}")
    self.ui.username.setStyleSheet("QLineEdit { border: 1px solid black}")
    self.ui.password.setStyleSheet("QLineEdit { border: 1px solid black}")
    self.ui.user_pass_err.setStyleSheet("QLineEdit { background-color: #e7e7e7; color: red;}")
    self.ui.title_log.setStyleSheet("QLabel { border: 1px solid black; border-radius: 0px; color: black; background-color: white;}")
    self.ui.password.setEchoMode(QtWidgets.QLineEdit.Password)

def register_style(self):
    self.ui.login_back_btn.setStyleSheet('QPushButton {background-color: white; color: black; border-radius: 10px; border: 1px solid black;}'
                           "QPushButton:pressed { background-color: grey; color: white;}")
    self.ui.register_new_btn.setStyleSheet('QPushButton {background-color: white; color: black; border-radius: 10px; border: 1px solid black;}'
                           "QPushButton:pressed { background-color: grey; color: white;}")
    self.ui.registration_frame.setStyleSheet("QFrame {background-color: #e7e7e7; border-radius: 8px; border: 1px solid black;}")
    self.ui.label_pass_register.setStyleSheet("QLabel { border: 0}")
    self.ui.label_user_register.setStyleSheet("QLabel { border: 0}")
    self.ui.title_reg.setStyleSheet("QLabel { border: 0}")
    self.ui.username_reg.setStyleSheet("QLineEdit { border: 1px solid black}")
    self.ui.password_reg.setStyleSheet("QLineEdit { border: 1px solid black}")
    self.ui.user_pass_err_reg.setStyleSheet("QLineEdit { background-color: #e7e7e7; color: red;}")
    self.ui.title_reg.setStyleSheet("QLabel { border: 1px solid black; border-radius: 0px; color: black; background-color: white;}")
    self.ui.min_max.setStyleSheet("QLabel { border: 0px ;}")
    self.ui.password_reg.setEchoMode(QtWidgets.QLineEdit.Password)

def dashboard_style(self):
    self.ui.profilo_frame.setStyleSheet("QFrame {background-color: #e7e7e7; border-radius: 10px; border: 1px solid black;}")
    self.ui.profilo_dati_btn.setStyleSheet('QPushButton {background-color: white; color: black; border-radius: 10px; border: 1px solid black;}'
                           "QPushButton:pressed { background-color: grey; color: white;}")
    self.ui.seguiti_btn.setStyleSheet('QPushButton {background-color: white; color: black; border-radius: 10px; border: 1px solid black;}'
                           "QPushButton:pressed { background-color: grey; color: white;}")
    self.ui.bacheca_btn.setStyleSheet('QPushButton {background-color: white; color: black; border-radius: 10px; border: 1px solid black; font-weight: bold;}'
                           "QPushButton:pressed { background-color: grey; color: white;}")
    self.ui.logout_btn.setStyleSheet('QPushButton {background-color: white; color: black; border-radius: 10px; border: 1px solid black;}'
                           "QPushButton:pressed { background-color: grey; color: white;}")
    self.ui.notifiche_btn.setStyleSheet('QPushButton {background-color: white; color: black; border-radius: 10px; border: 1px solid black;}'
                           "QPushButton:pressed { background-color: grey; color: white;}")

def profile_style(self):    
    self.ui.dati_personali.setStyleSheet("QListWidget {border: 1px solid black; background: white; border-radius: 0px;}")
    self.ui.mod_data_btn.setStyleSheet('QPushButton {background-color: white; color: black; border-radius: 10px; border: 1px solid black;}'
                           "QPushButton:pressed { background-color: grey; color: white;}")
    self.ui.data_mod.setStyleSheet("QLineEdit { border: 1px solid black}")
    self.ui.combo_mod_dati.setStyleSheet("QComboBox { background-color: white;}")    
    self.ui.personal_msg.setStyleSheet("QListWidget {border: 1px solid black; background: white; border-radius: 0px;} QListView::item {border : 1px solid black; background: white; color: black; height:100; width: 394;} QListView::item:selected {border : 1px solid red; border-radius: 0px; background: white; color: red;}")
    self.ui.el_sel_msg.setStyleSheet('QPushButton {background-color: white; color: red; border-radius: 10px; border: 1px solid red;}'
                           "QPushButton:pressed { background-color: red; color: white; }")

def user_style(self):
    self.ui.seguiti_frame.setStyleSheet("QFrame {background-color: #e7e7e7; border-radius: 8px; border: 1px solid black;}")
    self.ui.ricerca_utente.setStyleSheet("QLineEdit { border: 1px solid black}")
    self.ui.cerca_btn.setStyleSheet('QPushButton {background-color: white; color: black; border-radius: 10px; border: 1px solid black;}'
                           "QPushButton:pressed { background-color: grey; color: white;}")
    self.ui.follow_btn.setStyleSheet('QPushButton {background-color: white; color: black; border-radius: 10px; border: 1px solid black;}'
                           "QPushButton:pressed { background-color: grey; color: white;}")
    self.ui.table_utenti.setColumnWidth(0, 150)
    self.ui.table_utenti.setColumnWidth(1, 110)
    delegate = ReadOnly()
    self.ui.table_utenti.setItemDelegateForColumn(0, delegate)
    self.ui.table_utenti.setItemDelegateForColumn(1, delegate)
    self.ui.table_utenti.setItemDelegateForColumn(2, delegate)
    self.ui.table_utenti.setStyleSheet("QTableWidget {background-color:white; border-radius: 0px;}")
    self.ui.table_utenti_info.setStyleSheet("QTableWidget {background-color:white; border-radius: 0px;}")
    self.ui.table_utenti_info.setColumnWidth(0, 250)
    self.ui.table_utenti_info.setColumnWidth(1, 260)
    self.ui.table_utenti_info.setItemDelegateForColumn(0, delegate)
    self.ui.table_utenti_info.setItemDelegateForColumn(1, delegate)
    self.ui.utente_msg_list.setStyleSheet("QListWidget {border: 1px solid black; background: white; border-radius: 0px;} QListView::item {border: 1px solid black; background: white; color: black; height:100; width: 394;}")
    
def profile_btn_style(user_btn):
    user_btn.setFont(QFont('Gabriola', 16))
    user_btn.setStyleSheet('QPushButton {background-color: white; color: black; border-radius: 10px; border: 1px solid black; font-weight: bold;}'
                           "QPushButton:pressed { background-color: grey; color: white;}")

def notice_board_style(self):
    self.ui.table_bacheca.setColumnWidth(0, 120)
    self.ui.table_bacheca.setColumnWidth(1, 590)
    self.ui.table_bacheca.setColumnWidth(2, 140)   
    delegate = ReadOnly()
    self.ui.table_bacheca.setItemDelegateForColumn(0, delegate)
    self.ui.table_bacheca.setItemDelegateForColumn(1, delegate)
    self.ui.table_bacheca.setItemDelegateForColumn(2, delegate)   
    
    self.ui.bacheca_frame.setStyleSheet("QFrame {background-color: #e7e7e7; border-radius: 8px; border: 1px solid black;}")
    self.ui.post_btn.setStyleSheet('QPushButton {background-color: white; color: black; border-radius: 10px; border: 1px solid black;}'
                           "QPushButton:pressed { background-color: grey; color: white;}")
    self.ui.post_msg.setStyleSheet("QLineEdit { border: 1px solid black;}")
    self.ui.max_char.setStyleSheet("QLabel { border: 0}")
    self.ui.table_bacheca.setStyleSheet("QTableView {background-color:white; border-radius: 0px;}")
    self.ui.title_bacheca.setStyleSheet("QLabel { border: 0px ;}")

def events_style(self):
    self.ui.table_eventi.setColumnWidth(0, 150)
    self.ui.table_eventi.setColumnWidth(1, 250)
    self.ui.table_eventi.setColumnWidth(2, 10) 
    delegate = ReadOnly()
    self.ui.table_eventi.setItemDelegateForColumn(0, delegate)
    self.ui.table_eventi.setItemDelegateForColumn(1, delegate)
    self.ui.table_eventi.setItemDelegateForColumn(2, delegate)    
    self.ui.notifiche_frame.setStyleSheet("QFrame {background-color: #e7e7e7; border-radius: 8px; border: 1px solid black;}")
    self.ui.table_eventi.setStyleSheet("QTableView {background-color:white; border-radius: 0px;}")
    self.ui.dati_personali_eventi.setStyleSheet("QListWidget {border: 1px solid black; background: white; border-radius: 0px;}")