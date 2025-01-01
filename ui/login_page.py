from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QTimer

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.setFixedSize(1003, 620)
        
        # Set up modern font
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setFamily("Segoe UI")  # Modern font
        Form.setFont(font)
        
        # Enhanced gradient background
        Form.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(43, 171, 218, 255),
                    stop:0.5 rgba(115, 134, 213, 255),
                    stop:1 rgba(235, 103, 255, 255)
                );
            }
        """)

        # Title Label with enhanced styling
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 60, 991, 121))
        self.label.setStyleSheet("""
            QLabel {
                background: transparent;
                color: white;
                font: 600 80px 'Segoe UI';
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            }
        """)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        # Modern Email Input
        self.emailText = QtWidgets.QLineEdit(Form)
        self.emailText.setGeometry(QtCore.QRect(270, 200, 481, 51))
        self.emailText.setStyleSheet("""
            QLineEdit {
                background-color: rgba(255, 255, 255, 0.9);
                border: 2px solid rgba(255, 255, 255, 0.8);
                border-radius: 25px;
                padding: 10px 20px;
                font: 500 12pt 'Segoe UI';
                color: rgb(48, 169, 219);
            }
            QLineEdit:focus {
                border: 2px solid white;
                background-color: white;
            }
        """)

        # Modern Password Input
        self.passText = QtWidgets.QLineEdit(Form)
        self.passText.setGeometry(QtCore.QRect(270, 280, 481, 51))
        self.passText.setStyleSheet(self.emailText.styleSheet())
        self.passText.setEchoMode(QtWidgets.QLineEdit.Password)

        # Login Button with enhanced styling
        self.loginButton = QtWidgets.QPushButton(Form)
        self.loginButton.setGeometry(QtCore.QRect(400, 380, 201, 71))
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setStyleSheet("""
            QPushButton {
                color: white;
                border: 2px solid rgba(255, 255, 255, 0.8);
                border-radius: 35px;
                padding: 5px;
                font: 600 20pt 'Segoe UI';
                background: rgba(255, 255, 255, 0.1);
                transition: all 0.3s ease;
            }
            QPushButton:hover {
                border: 2px solid white;
                background-color: rgba(255, 255, 255, 0.2);
                transform: scale(1.05);
            }
            QPushButton:pressed {
                background-color: rgba(255, 255, 255, 0.3);
                transform: scale(0.95);
            }
        """)

        # Back Button with matching style
        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(30, 30, 151, 51))
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setStyleSheet("""
            QPushButton {
                color: white;
                border: 2px solid rgba(255, 255, 255, 0.8);
                border-radius: 25px;
                padding: 5px;
                font: 500 16pt 'Segoe UI';
                background: rgba(255, 255, 255, 0.1);
            }
            QPushButton:hover {
                border: 2px solid white;
                background-color: rgba(255, 255, 255, 0.2);
            }
            QPushButton:pressed {
                background-color: rgba(255, 255, 255, 0.3);
            }
        """)

        # Error Label
        self.passErrorLabel = QtWidgets.QLabel(Form)
        self.passErrorLabel.setGeometry(QtCore.QRect(270, 340, 481, 21))
        self.passErrorLabel.setStyleSheet("""
            QLabel {
                background: transparent;
                color: rgb(255, 80, 80);
                font: 500 12pt 'Segoe UI';
            }
        """)
        self.passErrorLabel.setText("")

        # Copyright Label
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 490, 991, 121))
        self.label_2.setStyleSheet("""
            QLabel {
                background: transparent;
                color: rgba(255, 255, 255, 0.8);
                font: 400 20px 'Segoe UI';
            }
        """)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        # Set up animations
        self.setupAnimations()

    def setupAnimations(self):
        # Fade-in animation for title
        self.titleAnimation = QPropertyAnimation(self.label, b"geometry")
        self.titleAnimation.setDuration(1000)
        self.titleAnimation.setStartValue(QtCore.QRect(0, 0, 991, 121))
        self.titleAnimation.setEndValue(QtCore.QRect(0, 60, 991, 121))
        self.titleAnimation.setEasingCurve(QEasingCurve.OutBack)

        # Input fields slide-in animations
        self.emailAnimation = QPropertyAnimation(self.emailText, b"geometry")
        self.emailAnimation.setDuration(1000)
        self.emailAnimation.setStartValue(QtCore.QRect(-481, 200, 481, 51))
        self.emailAnimation.setEndValue(QtCore.QRect(270, 200, 481, 51))
        self.emailAnimation.setEasingCurve(QEasingCurve.OutCubic)

        self.passAnimation = QPropertyAnimation(self.passText, b"geometry")
        self.passAnimation.setDuration(1000)
        self.passAnimation.setStartValue(QtCore.QRect(1003, 280, 481, 51))
        self.passAnimation.setEndValue(QtCore.QRect(270, 280, 481, 51))
        self.passAnimation.setEasingCurve(QEasingCurve.OutCubic)

        # Button animation
        self.loginAnimation = QPropertyAnimation(self.loginButton, b"geometry")
        self.loginAnimation.setDuration(1000)
        self.loginAnimation.setStartValue(QtCore.QRect(400, 620, 201, 71))
        self.loginAnimation.setEndValue(QtCore.QRect(400, 380, 201, 71))
        self.loginAnimation.setEasingCurve(QEasingCurve.OutBack)

        # Start animations with delays
        QTimer.singleShot(100, self.titleAnimation.start)
        QTimer.singleShot(300, self.emailAnimation.start)
        QTimer.singleShot(500, self.passAnimation.start)
        QTimer.singleShot(700, self.loginAnimation.start)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CodeHUB - Login"))
        self.loginButton.setText(_translate("Form", "Log In"))
        self.backButton.setText(_translate("Form", "Back"))
        self.label.setText(_translate("Form", "Login"))
        self.label_2.setText(_translate("Form", "© 2024 CodeHUB. All rights reserved."))
        self.emailText.setPlaceholderText(_translate("Form", "Enter User Email"))
        self.passText.setPlaceholderText(_translate("Form", "Enter Password"))