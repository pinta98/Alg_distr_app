from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont, QColor


def login_style(self):
    self.ui.login_btn.setStyleSheet('QPushButton {background-color: white; color: black; border-radius: 8px; border: 1px solid black;}'
                           "QPushButton:pressed { background-color: grey }" )
    self.ui.register_btn.setStyleSheet('QPushButton {background-color: white; color: black; border-radius: 8px; border: 1px solid black;}'
                           "QPushButton:pressed { background-color: grey }" )
    self.ui.login_frame.setStyleSheet("QFrame {background-color: #e7e7e7; border-radius: 8px; border: 1px solid black;}")
    self.ui.label_pass_login.setStyleSheet("QLabel { border: 0}")
    self.ui.label_user_login.setStyleSheet("QLabel { border: 0}")
    self.ui.title_log.setStyleSheet("QLabel { border: 0}")
    self.ui.username.setStyleSheet("QLineEdit { border: 1px solid black}")
    self.ui.password.setStyleSheet("QLineEdit { border: 1px solid black}")
    self.ui.user_pass_err.setStyleSheet("QLineEdit { background-color: #e7e7e7; color: red;}")

def register_style(self):

    self.ui.login_back_btn.setStyleSheet('QPushButton {background-color: white; color: black; border-radius: 8px; border: 1px solid black;}'
                           "QPushButton:pressed { background-color: grey }" )
    self.ui.register_new_btn.setStyleSheet('QPushButton {background-color: white; color: black; border-radius: 8px; border: 1px solid black;}'
                           "QPushButton:pressed { background-color: grey }" )
    self.ui.registration_frame.setStyleSheet("QFrame {background-color: #e7e7e7; border-radius: 8px; border: 1px solid black;}")
    self.ui.label_pass_register.setStyleSheet("QLabel { border: 0}")
    self.ui.label_user_register.setStyleSheet("QLabel { border: 0}")
    self.ui.title_reg.setStyleSheet("QLabel { border: 0}")
    self.ui.username_reg.setStyleSheet("QLineEdit { border: 1px solid black}")
    self.ui.password_reg.setStyleSheet("QLineEdit { border: 1px solid black}")
    self.ui.user_pass_err_reg.setStyleSheet("QLineEdit { background-color: #e7e7e7; color: red;}")