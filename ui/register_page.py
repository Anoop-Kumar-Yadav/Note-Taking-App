from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QTimer

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.setFixedSize(1003, 788)
        
        # Set up modern font
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setFamily("Segoe UI")
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

        # Title Label
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 60, 991, 121))
        self.label.setStyleSheet("""
            QLabel {
                background: transparent;
                color: white;
                font: 600 80px 'Segoe UI';
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            }
        """)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        # Common style for input fields
        input_style = """
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
        """

        # Input Fields
        self.fullNameText = QtWidgets.QLineEdit(Form)
        self.fullNameText.setGeometry(QtCore.QRect(270, 230, 481, 51))
        self.fullNameText.setStyleSheet(input_style)

        self.emailText = QtWidgets.QLineEdit(Form)
        self.emailText.setGeometry(QtCore.QRect(270, 300, 481, 51))
        self.emailText.setStyleSheet(input_style)

        self.passText = QtWidgets.QLineEdit(Form)
        self.passText.setGeometry(QtCore.QRect(270, 370, 481, 51))
        self.passText.setStyleSheet(input_style)
        self.passText.setEchoMode(QtWidgets.QLineEdit.Password)

        self.repassText = QtWidgets.QLineEdit(Form)
        self.repassText.setGeometry(QtCore.QRect(270, 440, 481, 51))
        self.repassText.setStyleSheet(input_style)
        self.repassText.setEchoMode(QtWidgets.QLineEdit.Password)

        # Sign Up Button
        self.signupButton = QtWidgets.QPushButton(Form)
        self.signupButton.setGeometry(QtCore.QRect(400, 560, 201, 71))
        self.signupButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signupButton.setStyleSheet("""
            QPushButton {
                color: white;
                border: 2px solid rgba(255, 255, 255, 0.8);
                border-radius: 35px;
                padding: 5px;
                font: 600 20pt 'Segoe UI';
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

        # Login Link Button
        self.loginButton = QtWidgets.QPushButton(Form)
        self.loginButton.setGeometry(QtCore.QRect(345, 510, 351, 28))
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                font: 500 12pt 'Segoe UI';
                color: rgba(255, 255, 255, 0.9);
            }
            QPushButton:hover {
                color: white;
            }
        """)

        # Back Button
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
        self.passErrorLabel.setGeometry(QtCore.QRect(270, 500, 481, 21))
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
        self.label_2.setGeometry(QtCore.QRect(10, 670, 991, 121))
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
        # Title animation
        self.titleAnimation = QPropertyAnimation(self.label, b"geometry")
        self.titleAnimation.setDuration(1000)
        self.titleAnimation.setStartValue(QtCore.QRect(20, 0, 991, 121))
        self.titleAnimation.setEndValue(QtCore.QRect(20, 60, 991, 121))
        self.titleAnimation.setEasingCurve(QEasingCurve.OutBack)

        # Input fields animations
        self.inputs = [
            (self.fullNameText, 230),
            (self.emailText, 300),
            (self.passText, 370),
            (self.repassText, 440)
        ]
        
        self.inputAnimations = []
        for i, (widget, y) in enumerate(self.inputs):
            anim = QPropertyAnimation(widget, b"geometry")
            anim.setDuration(800)
            anim.setStartValue(QtCore.QRect(-481, y, 481, 51))
            anim.setEndValue(QtCore.QRect(270, y, 481, 51))
            anim.setEasingCurve(QEasingCurve.OutCubic)
            self.inputAnimations.append(anim)

        # Button animation
        self.signupAnimation = QPropertyAnimation(self.signupButton, b"geometry")
        self.signupAnimation.setDuration(1000)
        self.signupAnimation.setStartValue(QtCore.QRect(400, 788, 201, 71))
        self.signupAnimation.setEndValue(QtCore.QRect(400, 560, 201, 71))
        self.signupAnimation.setEasingCurve(QEasingCurve.OutBack)

        # Start animations with delays
        QTimer.singleShot(100, self.titleAnimation.start)
        for i, anim in enumerate(self.inputAnimations):
            QTimer.singleShot(300 + i * 150, anim.start)
        QTimer.singleShot(900, self.signupAnimation.start)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CodeHUB - Register"))
        self.signupButton.setText(_translate("Form", "Sign Up"))
        self.label.setText(_translate("Form", "Sign Up"))
        self.label_2.setText(_translate("Form", "© 2024 CodeHUB. All rights reserved."))
        self.fullNameText.setPlaceholderText(_translate("Form", "Full Name"))
        self.loginButton.setText(_translate("Form", "Already have an account? Login →"))
        self.backButton.setText(_translate("Form", "Back"))
        self.emailText.setPlaceholderText(_translate("Form", "Email"))
        self.passText.setPlaceholderText(_translate("Form", "Password"))
        self.repassText.setPlaceholderText(_translate("Form", "Confirm Password"))