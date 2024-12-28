import sqlite3

class DatabaseManager:
    def __init__(self):

        self.conn = sqlite3.connect('note_taking_app.db')  
        self.cursor = self.conn.cursor()


        self.create_tables()

# --------------------------------------------------------------------------------------------------------------------------------

    def create_tables(self):
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