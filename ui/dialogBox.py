from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QTimer, Qt

class Ui_errorDialog(object):
    def setupUi(self, errorDialog):
        errorDialog.setObjectName("errorDialog")
        errorDialog.resize(400, 200)
        errorDialog.setWindowFlags(Qt.FramelessWindowHint)
        
        # Clean white background with subtle shadow
        errorDialog.setStyleSheet("""
            QDialog {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
            }
        """)
        
        # Message label
        self.label = QtWidgets.QLabel(errorDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 360, 100))
        self.label.setStyleSheet("""
            QLabel {
                color: #333333;
                font: 500 12pt 'Segoe UI';
            }
        """)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        
        # Button box
        self.buttonBox = QtWidgets.QDialogButtonBox(errorDialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 140, 360, 40))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        
        # Clean button style
        self.buttonBox.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 2px solid #ff4444;
                border-radius: 5px;
                color: #ff4444;
                min-width: 80px;
                padding: 5px 15px;
                font: 500 10pt 'Segoe UI';
            }
            QPushButton:hover {
                background-color: #ff4444;
                color: white;
            }
            QPushButton[text="Cancel"] {
                border: 2px solid #666666;
                color: #666666;
            }
            QPushButton[text="Cancel"]:hover {
                background-color: #666666;
                color: white;
            }
        """)
        
        self.buttonBox.accepted.connect(errorDialog.accept)
        self.buttonBox.rejected.connect(errorDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(errorDialog)

class Ui_successDialog(object):
    def setupUi(self, successDialog):
        successDialog.setObjectName("successDialog")
        successDialog.resize(400, 200)
        successDialog.setWindowFlags(Qt.FramelessWindowHint)
        
        # Clean white background with subtle shadow
        successDialog.setStyleSheet("""
            QDialog {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
            }
        """)
        
        # Message label
        self.label = QtWidgets.QLabel(successDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 360, 100))
        self.label.setStyleSheet("""
            QLabel {
                color: #333333;
                font: 500 12pt 'Segoe UI';
            }
        """)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        
        # Button box
        self.buttonBox = QtWidgets.QDialogButtonBox(successDialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 140, 360, 40))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        
        # Clean button style
        self.buttonBox.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 2px solid #44aa44;
                border-radius: 5px;
                color: #44aa44;
                min-width: 80px;
                padding: 5px 15px;
                font: 500 10pt 'Segoe UI';
            }
            QPushButton:hover {
                background-color: #44aa44;
                color: white;
            }
        """)
        
        self.buttonBox.accepted.connect(successDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(successDialog)