# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_note_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ui.db_manager import DatabaseManager
from PyQt5.QtWidgets import QMessageBox, QDialog

# ==================================================================================================================================
# ==================================================================================================================================

class Ui_Form(object):
    def setupUi(self, Form, currentUser):
        self.currentUser = currentUser
        Form.setObjectName("Form")
        Form.setFixedSize(849, 765)

        self.db_manager = DatabaseManager()

        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 851, 791))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(-70, -20, 991, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(74, 111, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 150, 791, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 210, 791, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(30, 270, 791, 281))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 570, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.loginButton = QtWidgets.QPushButton(self.frame)
        self.loginButton.setGeometry(QtCore.QRect(580, 660, 241, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.loginButton.setFont(font)
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setStyleSheet("QPushButton {\n"
"    color: rgb(170, 170, 255);\n"
"                border: 2px solid rgb(170, 170, 255);\n"
"                border-radius: 4px;\n"
"                padding: 5px;\n"
"                font-size: 16px;\n"
"                font: 75 20pt \"MS Shell Dlg 2\";\n"
"                background: transparent;\n"
"            }\n"
"            QPushButton:hover {\n"
"                border: 2px solid rgba(43, 171, 218, 255);\n"
"                color:rgba(43, 171, 218, 255);\n"
"                background-color: rgba(255, 255, 255, 255);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                border: 2px solid darkblue;\n"
"                background-color: gray;\n"
"            }")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/add_notes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginButton.setIcon(icon)
        self.loginButton.setIconSize(QtCore.QSize(48, 48))
        self.loginButton.setObjectName("loginButton")
        
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
     
       
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.loginButton.clicked.connect(self.on_add_note_button_click)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add Note"))
        self.label_2.setText(_translate("Form", "Adding New Note"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter Title"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Enter Subject"))
        self.textEdit.setPlaceholderText(_translate("Form", "Description ..."))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "  Tags (e.g Science, CSE, Html etc)"))
        self.loginButton.setText(_translate("Form", " Add Note"))
     

# --------------------------------------------------------------------------------------------------------------------------------

    def on_add_note_button_click(self):
        title = self.lineEdit.text()
        subject = self.lineEdit_2.text()
        description = self.textEdit.toPlainText()
        tags = self.lineEdit_3.text()

        if not title or not subject or not description or not tags:
            QMessageBox.warning(None, "Input Error", "Please fill in all fields!")
            return


        user_id = self.db_manager.get_user_id_by_gmail(self.currentUser)
        self.db_manager.add_note(user_id,title, subject, description, tags)

        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.textEdit.clear()
        self.lineEdit_3.clear()

        QMessageBox.information(None, "Success", "Note added successfully!")

# --------------------------------------------------------------------------------------------------------------------------------

class AddNoteDialog(QDialog):
    def __init__(self, parent=None,currentUser=None):
        super().__init__(parent)
        self.currentUser = currentUser  
        
        self.add_note_ui = Ui_Form()
        self.add_note_ui.setupUi(self, currentUser) 
        self.setModal(True)
