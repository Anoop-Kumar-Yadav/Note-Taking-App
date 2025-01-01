import sqlite3
import json

class DatabaseManager:
    def __init__(self):

        self.conn = sqlite3.connect('note_taking_app.db')  
        self.cursor = self.conn.cursor()


        self.create_tables()

# --------------------------------------------------------------------------------------------------------------------------------
    def run_once_function(self):
        json_file_path = "./resources/current_user.json"

        data = {"currentUser": 0}

        try:
            with open(json_file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
            print(f"JSON file '{json_file_path}' created successfully with data: {data}")
        except Exception as e:
            print(f"Error creating JSON file: {e}")

# --------------------------------------------------------------------------------------------------------------------------------
    def initialize_settings_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
        """)

        self.cursor.execute("SELECT value FROM settings WHERE key = 'init_flag'")
        result = self.cursor.fetchone()

        if result is None:
            self.run_once_function()
            self.cursor.execute("INSERT INTO settings (key, value) VALUES ('init_flag', '1')")
            self.conn.commit()

        elif result[0] == '0':
            self.run_once_function()
            self.cursor.execute("UPDATE settings SET value = '1' WHERE key = 'init_flag'")
            self.conn.commit()

        else:
            print("Initialization already completed.")

# --------------------------------------------------------------------------------------------------------------------------------

    def create_tables(self):
        self.initialize_settings_table()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                gmail TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                full_name TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                note_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                subject TEXT NOT NULL,
                description TEXT NOT NULL,
                tags TEXT,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        ''')

        self.conn.commit()

# --------------------------------------------------------------------------------------------------------------------------------

    def get_user_id_by_gmail(self,email):
        self.cursor.execute("SELECT user_id FROM users WHERE gmail = ?", (email,))
        user = self.cursor.fetchone()
        if user:
            return user[0]
        return None

# --------------------------------------------------------------------------------------------------------------------------------

    def get_note_count(self, user_id):
        self.cursor.execute("SELECT COUNT(*) FROM notes WHERE user_id = ?", (user_id,))
        count = self.cursor.fetchone()
        return count[0] if count else 0

# --------------------------------------------------------------------------------------------------------------------------------

    def get_user_profile_by_email(self, email):
        self.cursor.execute("SELECT user_id, full_name, gmail FROM users WHERE gmail = ?", (email,))
        user = self.cursor.fetchone()
        if user:
            return {'user_id': user[0], 'full_name': user[1], 'gmail': user[2]}
        return None 
# --------------------------------------------------------------------------------------------------------------------------------

    def user_exists(self, email):
        self.cursor.execute("SELECT COUNT(*) FROM users WHERE gmail = ?", (email,))
        result = self.cursor.fetchone()
        return result[0] > 0 

# --------------------------------------------------------------------------------------------------------------------------------

    def register_user(self, email, password, full_name):
        """Register a new user in the users table."""
        if self.user_exists(email):
            return False  
        
        self.cursor.execute("INSERT INTO users (gmail, password, full_name) VALUES (?, ?, ?)", (email, password, full_name))
        self.conn.commit()
        return True 

# --------------------------------------------------------------------------------------------------------------------------------

    def authenticate_user(self, email, password):
        self.cursor.execute("SELECT * FROM users WHERE gmail = ? AND password = ?", (email, password))
        user = self.cursor.fetchone()
        if user:
            return {'user_id': user[0], 'gmail': user[1], 'full_name': user[3]}  
        return None 

# --------------------------------------------------------------------------------------------------------------------------------

    def add_note(self, user_id, title, subject, description, tags):
        self.cursor.execute("INSERT INTO notes (user_id, title, subject, description, tags) VALUES (?, ?, ?, ?, ?)", 
                            (user_id, title, subject, description, tags))
        self.conn.commit()

# --------------------------------------------------------------------------------------------------------------------------------

    def update_note(self, note_id, title, subject, description, tags):
        self.cursor.execute("""
            UPDATE notes 
            SET title = ?, subject = ?, description = ?, tags = ? 
            WHERE note_id = ?
        """, (title, subject, description, tags, note_id))

        self.conn.commit()

# --------------------------------------------------------------------------------------------------------------------------------

    def get_notes(self, user_id):
        self.cursor.execute("SELECT * FROM notes WHERE user_id = ?", (user_id,))
        notes = self.cursor.fetchall()
        return notes

# --------------------------------------------------------------------------------------------------------------------------------

    def get_note(self, user_id, note_id):
        notes = self.get_notes(user_id)
        self.cursor.execute("SELECT * FROM notes WHERE note_id = ?", (note_id,))
        note = self.cursor.fetchone()
        return note

# --------------------------------------------------------------------------------------------------------------------------------

    def update_note(self, note_id, title, subject, description, tags):
        self.cursor.execute('''UPDATE notes 
                               SET title = ?, subject = ?, description = ?, tags = ? 
                               WHERE note_id = ?''', 
                               (title, subject, description, tags, note_id))
        self.conn.commit()

# --------------------------------------------------------------------------------------------------------------------------------

    def delete_note(self, note_id):
        self.cursor.execute("DELETE FROM notes WHERE note_id = ?", (note_id,))
        self.conn.commit()

# --------------------------------------------------------------------------------------------------------------------------------

    def get_password(self,email):
        self.cursor.execute("SELECT password FROM users WHERE gmail = ?", (email,))
        result = self.cursor.fetchone()
        return result[0]

# --------------------------------------------------------------------------------------------------------------------------------

    def change_password(self,new_pass,email):
        self.cursor.execute("UPDATE users SET password = ? WHERE gmail = ?", (new_pass, email))
        self.conn.commit()

# --------------------------------------------------------------------------------------------------------------------------------

    def close(self):
        """Close the database connection."""
        self.conn.close()


# --------------------------------------------------------------------------------------------------------------------------------