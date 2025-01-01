import sys,re
import json
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QDialog, QTableWidgetItem, QPushButton,QWidget, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import ui.dashboard_page
import ui.home_page
import ui.login_page
import ui.register_page
import ui.add_note_form
from ui.dialogBox import Ui_errorDialog,Ui_successDialog


import ui.db_manager
import ui.update_note_form

# ==================================================================================================================================
# ==================================================================================================================================

class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.db_manager = ui.db_manager.DatabaseManager()

        self.currentUser = self.load_current_user()

        self.home_page = QMainWindow()
        self.login_page = QMainWindow()
        self.register_page = QMainWindow()
        self.dashboard_page = QMainWindow()
        self.dashboard_page.closeEvent = self.closeEvent

        self.home_ui = ui.home_page.Ui_Form()
        self.home_ui.setupUi(self.home_page)

        self.login_ui = ui.login_page.Ui_Form()
        self.login_ui.setupUi(self.login_page)

        self.register_ui = ui.register_page.Ui_Form()
        self.register_ui.setupUi(self.register_page)

        self.dashboard_ui = ui.dashboard_page.Ui_Form()
        self.dashboard_ui.setupUi(self.dashboard_page)

        # Connect buttons for switching windows
        self.home_ui.loginButton.clicked.connect(self.open_login_window)
        self.home_ui.joinButton.clicked.connect(self.open_register_window)

        self.register_ui.backButton.clicked.connect(self.open_home_window)
        self.register_ui.loginButton.clicked.connect(self.open_login_window)
        self.register_ui.signupButton.clicked.connect(self.handle_register)

        self.login_ui.backButton.clicked.connect(self.open_home_window)
        self.login_ui.loginButton.clicked.connect(self.open_dashboard_window)

        self.dashboard_ui.loginButton.clicked.connect(self.open_add_note_window)

        self.dashboard_ui.loginButton_3.clicked.connect(self.logout)
        self.init_startup_window()

# --------------------------------------------------------------------------------------------------------------------------------
    def load_current_user(self):
        try:
            with open("resources//current_user.json", "r") as file:
                data = json.load(file)
                return data.get("currentUser", None)
        except FileNotFoundError:
            return None
        
    def save_current_user(self):
        with open("resources//current_user.json", "w") as file:
            json.dump({"currentUser": self.currentUser}, file)

    def init_startup_window(self):
        if self.currentUser != 0:
            self.init_dashboard()
            self.dashboard_page.show()
        else:
            self.home_page.show()

    def logout(self):
        self.currentUser = 0
        self.save_current_user()
        self.dashboard_page.close()
        self.open_home_window()

    def closeEvent(self, event):
        if self.show_error_dialog("Do you want to exit ?") :
            self.save_current_user()
            event.accept()
        else:
            event.ignore() 

# --------------------------------------------------------------------------------------------------------------------------------
    def add_buttons_to_row(self, row, note_id):
        # Create buttons
        update_button = QPushButton()        
        delete_button = QPushButton()

        update_icon = QIcon('resources\\edit.png') 
        delete_icon = QIcon('resources\\delete.png') 
        update_button.setIcon(update_icon)
        delete_button.setIcon(delete_icon)

        update_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 4px;
                font-family: 'Segoe UI';
                font-size: 10px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #218838;
            }
            QPushButton:pressed {
                background-color: #1e7e34;
            }
        """)

        delete_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 4px;
                font-family: 'Segoe UI';
                font-size: 13px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
            QPushButton:pressed {
                background-color: #bd2130;
            }
        """)


        update_button.clicked.connect(lambda _, note_id=note_id: self.update_note_action(note_id))
        delete_button.clicked.connect(lambda _, note_id=note_id: self.delete_note_action(note_id))


        action_widget = QWidget()
        action_layout = QHBoxLayout(action_widget)
        action_layout.addWidget(update_button)
        action_layout.addSpacing(8)  
        action_layout.addWidget(delete_button)
        action_layout.setContentsMargins(5, 2, 5, 2) 
        action_layout.setAlignment(Qt.AlignCenter) 

        action_widget.setLayout(action_layout)


        self.dashboard_ui.tableWidget.setCellWidget(row, 5, action_widget)

# --------------------------------------------------------------------------------------------------------------------------------

    def update_note_action(self, note_id):
        
        dialog = ui.update_note_form.UpdateNoteDialog(self.dashboard_page,self.currentUser,note_id)
        dialog.exec_()

        self.populate_notes_table(str(self.db_manager.get_user_id_by_gmail(self.currentUser)))
        user_id = str(self.db_manager.get_user_id_by_gmail(self.currentUser))
        self.dashboard_ui.label_3.setText(str( self.db_manager.get_note_count(user_id)))
        
# --------------------------------------------------------------------------------------------------------------------------------

    def delete_note_action(self, note_id):
      
        self.db_manager.delete_note(note_id)

        self.populate_notes_table(str(self.db_manager.get_user_id_by_gmail(self.currentUser)))
        user_id = str(self.db_manager.get_user_id_by_gmail(self.currentUser))
        self.dashboard_ui.label_3.setText(str( self.db_manager.get_note_count(user_id)))

# --------------------------------------------------------------------------------------------------------------------------------

    def populate_notes_table(self, user_id):
        notes = self.db_manager.get_notes(user_id)

        self.dashboard_ui.tableWidget.setRowCount(0)


        self.dashboard_ui.tableWidget.setRowCount(len(notes))
        self.dashboard_ui.tableWidget.setColumnCount(6)  
        self.dashboard_ui.tableWidget.setHorizontalHeaderLabels(["Note ID", "Title", "Subject", "Description", "Tags", "Actions"])

        row_height = 60  
        for row in range(len(notes)):
            self.dashboard_ui.tableWidget.setRowHeight(row, row_height)

       
        column_widths = [80, 200, 150, 300, 120, 100]  
        for col, width in enumerate(column_widths):
            self.dashboard_ui.tableWidget.setColumnWidth(col, width)

 
        for row, note in enumerate(notes):

            self.dashboard_ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(note[0])))  
            self.dashboard_ui.tableWidget.setItem(row, 1, QTableWidgetItem(note[2]))  
            self.dashboard_ui.tableWidget.setItem(row, 2, QTableWidgetItem(note[3]))  
            self.dashboard_ui.tableWidget.setItem(row, 3, QTableWidgetItem(note[4]))  
            self.dashboard_ui.tableWidget.setItem(row, 4, QTableWidgetItem(note[5] or "")) 

      
            self.add_buttons_to_row(row, note[0])

    
        self.dashboard_ui.tableWidget.horizontalHeader().setStretchLastSection(True)

# --------------------------------------------------------------------------------------------------------------------------------

    def is_valid_email(self, email):
        if not email:
            return False, "Email is empty."

        if '@' not in email:
            return False, "Email must contain '@'."

        local_part, domain_part = email.split('@', 1)

        if not local_part:
            return False, "Local part (before '@') is missing."

        if not domain_part:
            return False, "Domain part (after '@') is missing."

        if len(local_part) > 64:
            return False, "Local part is too long. Max length is 64 characters."

        if len(domain_part) > 255:
            return False, "Domain part is too long. Max length is 255 characters."

        if not re.match(r'^[a-zA-Z0-9_.+-]+$', local_part):
            return False, "Local part contains invalid characters."

        if not re.match(r'^[a-zA-Z0-9-]+$', domain_part.replace('.', '')):
            return False, "Domain part contains invalid characters."

        if '.' not in domain_part:
            return False, "Domain part must contain at least one period (.)"

        tld = domain_part.split('.')[-1]
        if len(tld) < 2 or len(tld) > 6: 
            return False, "Invalid TLD length. TLD should be between 2 and 6 characters."

        if '..' in email:
            return False, "Email contains consecutive dots (..) which is invalid."

        if len(email) > 320:
            return False, "Email is too long. Max length is 320 characters."

        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_pattern, email):
            return False, "Email format is incorrect."

        return True, "Valid email."

# --------------------------------------------------------------------------------------------------------------------------------

    def show_error_dialog(self, message):
        dialog = QDialog(None)
        ui = Ui_errorDialog() 
        ui.setupUi(dialog)

        ui.label.setText(message)

        result = dialog.exec_()

        if result == QDialog.Accepted:
            return 1
        else:
            return 0

# --------------------------------------------------------------------------------------------------------------------------------

    def show_success_dialog(self, message):
        dialog = QDialog(None)
        ui = Ui_successDialog()
        ui.setupUi(dialog)

        ui.label.setText(message)

        result = dialog.exec_()

# --------------------------------------------------------------------------------------------------------------------------------

    def open_dashboard_window(self):  

        email = self.login_ui.emailText.text()
        password = self.login_ui.passText.text()

        is_valid, message = self.is_valid_email(email)
        if not is_valid:
            self.show_error_dialog(message)
            return  

        user = self.db_manager.authenticate_user(email, password)
        if user:
            self.currentUser = email 
            self.login_page.hide()
            self.dashboard_page.show()
            self.init_dashboard()
        else:
            self.show_error_dialog("Incorrect email or password!")

# --------------------------------------------------------------------------------------------------------------------------------

    def update_profile(self,user):
        self.dashboard_ui.label_24.setText(str(user['user_id']))
        self.dashboard_ui.label_8.setText(str(user['full_name']))
        self.dashboard_ui.label_9.setText( str(user['gmail']))
               
    def init_dashboard(self):
        user = self.db_manager.get_user_profile_by_email(self.currentUser)
        self.dashboard_ui.infolabel.setText("Welcome " + user['full_name'])
        self.dashboard_ui.label_3.setText(str( self.db_manager.get_note_count(user["user_id"])))

        self.update_profile(user)
        
        self.populate_notes_table(user["user_id"])

# --------------------------------------------------------------------------------------------------------------------------------

    def handle_register(self):
        email = self.register_ui.emailText.text()
        password = self.register_ui.passText.text()
        full_name = self.register_ui.fullNameText.text()

    
        is_valid, message = self.is_valid_email(email)
        if not is_valid:
            self.show_error_dialog(message)
            return  

        if not password or not full_name:
            self.show_success_dialog("All fields are required!")
            return

    
        if self.db_manager.user_exists(email):
            self.show_success_dialog("Email already exists!")
            return

        if self.db_manager.register_user(email, password, full_name):
            self.show_success_dialog("Registration Successful. You can now log in!")
            self.open_login_window() 
        else:
            self.show_success_dialog("An error occurred while registering.")

# --------------------------------------------------------------------------------------------------------------------------------

    def open_login_window(self):
        self.login_ui.emailText.clear()
        self.login_ui.emailText.clear()

        if self.home_page.isVisible():  
            self.home_page.hide()
        elif self.register_page.isVisible():
            self.register_page.hide() 
        self.login_page.show()

# --------------------------------------------------------------------------------------------------------------------------------
   
    def open_register_window(self):
        self.home_page.hide()
        self.register_page.show()

# --------------------------------------------------------------------------------------------------------------------------------

    def open_home_window(self):
        if (self.login_page.isVisible() ):
            self.login_page.hide()
            
        elif (self.register_page.isVisible()):
            self.register_page.hide()

        self.home_page.show()

# --------------------------------------------------------------------------------------------------------------------------------

    def open_add_note_window(self):
        if not self.currentUser:
            QMessageBox.warning(None, "Login Required", "Please login first!")
            return

        dialog = ui.add_note_form.AddNoteDialog(self.dashboard_page,self.currentUser)
        dialog.exec_()
        self.populate_notes_table(str(self.db_manager.get_user_id_by_gmail(self.currentUser)))
        user_id = str(self.db_manager.get_user_id_by_gmail(self.currentUser))
        self.dashboard_ui.label_3.setText(str( self.db_manager.get_note_count(user_id)))

# --------------------------------------------------------------------------------------------------------------------------------

    def run(self):
        self.init_startup_window()
        sys.exit(self.app.exec_())

# --------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = MainApp()
    app.run()
