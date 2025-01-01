from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QPoint, QTimer

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.setFixedSize(1003, 620)
        
        # Set up modern font
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setFamily("Segoe UI")  # More modern font
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

        # Login Button with enhanced styling
        self.loginButton = QtWidgets.QPushButton(Form)
        self.loginButton.setGeometry(QtCore.QRect(560, 410, 201, 71))
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

        # Join Button with matching style
        self.joinButton = QtWidgets.QPushButton(Form)
        self.joinButton.setGeometry(QtCore.QRect(250, 410, 201, 71))
        self.joinButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.joinButton.setStyleSheet(self.loginButton.styleSheet())

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

        # Copyright Label
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 490, 991, 121))
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

        # Button slide-in animations
        self.joinButtonAnimation = QPropertyAnimation(self.joinButton, b"geometry")
        self.joinButtonAnimation.setDuration(1000)
        self.joinButtonAnimation.setStartValue(QtCore.QRect(-250, 410, 201, 71))
        self.joinButtonAnimation.setEndValue(QtCore.QRect(250, 410, 201, 71))
        self.joinButtonAnimation.setEasingCurve(QEasingCurve.OutCubic)

        self.loginButtonAnimation = QPropertyAnimation(self.loginButton, b"geometry")
        self.loginButtonAnimation.setDuration(1000)
        self.loginButtonAnimation.setStartValue(QtCore.QRect(1003, 410, 201, 71))
        self.loginButtonAnimation.setEndValue(QtCore.QRect(560, 410, 201, 71))
        self.loginButtonAnimation.setEasingCurve(QEasingCurve.OutCubic)

        # Start animations with slight delays
        QTimer.singleShot(100, self.titleAnimation.start)
        QTimer.singleShot(300, self.joinButtonAnimation.start)
        QTimer.singleShot(500, self.loginButtonAnimation.start)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CodeHUB - Note Taker"))
        self.loginButton.setText(_translate("Form", "Log In"))
        self.joinButton.setText(_translate("Form", "Join"))
        self.label.setText(_translate("Form", "CodeHUB - Note Taker"))
        self.label_2.setText(_translate("Form", "© 2024 CodeHUB. All rights reserved."))
