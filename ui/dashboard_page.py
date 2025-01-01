from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1107, 733)
        Form.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
                color: #212529;
            }
            QTabWidget::pane {
                border: none;
                background: #f8f9fa;
            }
            QTabWidget::tab-bar {
                alignment: center;
            }
            QTabBar::tab {
                background: #ffffff;
                color: #495057;
                padding: 12px 30px;
                margin: 0 2px;
                border: none;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
            }
            QTabBar::tab:selected {
                background: #4a6fff;
                color: white;
            }
            QTabBar::tab:hover:!selected {
                background: #e9ecef;
            }
        """)

        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1181, 741))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(24, 24))
        self.tabWidget.setObjectName("tabWidget")

        # Dashboard Tab
        self.Dashboard = QtWidgets.QWidget()
        self.Dashboard.setObjectName("Dashboard")
        self.frame_3 = QtWidgets.QFrame(self.Dashboard)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 1101, 711))
        self.frame_3.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border-radius: 10px;
            }
        """)
        self.frame_3.setObjectName("frame_3")

        # Stats Card
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setGeometry(QtCore.QRect(30, 150, 321, 151))
        self.frame_2.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border: 1px solid #e9ecef;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            }
        """)
        self.frame_2.setObjectName("frame_2")

        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 30, 70, 70))
        self.label.setStyleSheet("background: transparent;")
        self.label.setPixmap(QtGui.QPixmap("./resources/note_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(110, 40, 171, 20))
        self.label_2.setStyleSheet("""
            font-family: 'Segoe UI';
            font-size: 14px;
            color: #6c757d;
        """)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(110, 60, 141, 41))
        self.label_3.setStyleSheet("""
            color: #4a6fff;
            font-family: 'Segoe UI';
            font-size: 28px;
            font-weight: bold;
        """)
        self.label_3.setObjectName("label_3")

        self.forgetButton = QtWidgets.QPushButton(self.frame_2)
        self.forgetButton.setGeometry(QtCore.QRect(110, 110, 121, 32))
        self.forgetButton.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #4a6fff;
                border: none;
                font-family: 'Segoe UI';
                font-size: 13px;
                text-align: left;
                padding: 0;
            }
            QPushButton:hover {
                color: #2d46cc;
                text-decoration: underline;
            }
        """)
        self.forgetButton.setObjectName("forgetButton")

        # Welcome Text
        self.infolabel = QtWidgets.QLabel(self.frame_3)
        self.infolabel.setGeometry(QtCore.QRect(30, 30, 1041, 60))
        self.infolabel.setStyleSheet("""
            font-family: 'Segoe UI';
            font-size: 32px;
            font-weight: bold;
            color: #212529;
            padding-left: 20px;
        """)
        self.infolabel.setObjectName("infolabel")

        # Footer
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(60, 590, 991, 121))
        self.label_7.setStyleSheet("""
            color: #6c757d;
            font-family: 'Segoe UI';
            font-size: 14px;
        """)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        # Notes Tab
        self.Notes = QtWidgets.QWidget()
        self.Notes.setObjectName("Notes")
        self.frame_4 = QtWidgets.QFrame(self.Notes)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 1101, 711))
        self.frame_4.setStyleSheet("background-color: #ffffff;")
        self.frame_4.setObjectName("frame_4")

        self.loginButton = QtWidgets.QPushButton(self.frame_4)
        self.loginButton.setGeometry(QtCore.QRect(50, 50, 200, 50))
        self.loginButton.setStyleSheet("""
            QPushButton {
                background-color: #4a6fff;
                color: white;
                border: none;
                border-radius: 6px;
                font-family: 'Segoe UI';
                font-size: 15px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #2d46cc;
            }
            QPushButton:pressed {
                background-color: #1e32b6;
            }
        """)
        self.loginButton.setObjectName("loginButton")

        # Table Widget
        self.tableWidget = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget.setGeometry(QtCore.QRect(50, 140, 991, 461))
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: #ffffff;
                border: 1px solid #e9ecef;
                border-radius: 8px;
                gridline-color: #e9ecef;
            }
            QTableWidget::item {
                padding: 12px;
                border-bottom: 1px solid #e9ecef;
            }
            QHeaderView::section {
                background-color: #f8f9fa;
                padding: 12px;
                border: none;
                font-weight: bold;
                color: #495057;
            }
        """)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        # Profile Tab
        self.Profile = QtWidgets.QWidget()
        self.Profile.setObjectName("Profile")
        self.frame_5 = QtWidgets.QFrame(self.Profile)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 1101, 711))
        self.frame_5.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border-radius: 10px;
            }
        """)
        self.frame_5.setObjectName("frame_5")

        # Profile Image
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(80, 140, 250, 250))
        self.label_4.setStyleSheet("""
            background-color: transparent;
            border-radius: 125px;
        """)
        self.label_4.setPixmap(QtGui.QPixmap("./resources/admin3.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        # Create Profile Labels first
        self.label_23 = QtWidgets.QLabel(self.frame_5)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_24 = QtWidgets.QLabel(self.frame_5)
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_9 = QtWidgets.QLabel(self.frame_5)

        # Profile Labels
        labels = [
            (self.label_23, "User ID : ", 490, 130),
            (self.label_5, "Name   : ", 490, 190),
            (self.label_6, "Email   : ", 490, 260),
        
            (self.label_24, "UID454", 620, 130),
            (self.label_8, "CODEHUB", 620, 190),
            (self.label_9, "codehub@gmail.com", 620, 260)
        ]

        for label, text, x, y in labels:
            label.setGeometry(QtCore.QRect(x, y, 451, 51))
            label.setStyleSheet("""font-family: 'Segoe UI'; font-size: 16px; color: #212529;""")
            label.setText(text)
            label.setObjectName(f"label_{text.strip()}")


        # Logout Button
        self.loginButton_3 = QtWidgets.QPushButton(self.frame_5)
        self.loginButton_3.setGeometry(QtCore.QRect(830, 370, 200, 50))
        self.loginButton_3.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;
                color: white;
                border: none;
                border-radius: 6px;
                font-family: 'Segoe UI';
                font-size: 15px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
            QPushButton:pressed {
                background-color: #bd2130;
            }
        """)
        self.loginButton_3.setObjectName("loginButton_3")

        # Set up icons and complete the UI
        self.setupIcons()
        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def setupIcons(self):
        # Setup tab icons
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/dashboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Dashboard, icon, "")

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./resources/notes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Notes, icon2, "")

        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./resources/profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Profile, icon5, "")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dashboard"))
        self.label_2.setText(_translate("Form", "Total Uploaded Notes"))
        self.label_3.setText(_translate("Form", "12"))
        self.forgetButton.setText(_translate("Form", "View Details"))
        self.label_7.setText(_translate("Form", "© 2024 CodeHUB. All rights reserved."))
        self.infolabel.setText(_translate("Form", "Welcome Anoop Kumar Yadav"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Dashboard), _translate("Form", "Dashboard"))
        self.loginButton.setText(_translate("Form", "Add Note"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Notes), _translate("Form", "Notes"))
        self.loginButton_3.setText(_translate("Form", "Logout"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Profile), _translate("Form", "Profile"))

        