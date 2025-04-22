import sqlite3
import os
import json

# Definitions
# Kit / Kits    = Total of 16 DP controls
# Profile / Profiles = Total of 3 Profiles

class Database:
    _instance = None

    def __init__(self):
        if not os.path.exists('drumx.db'):
            self.conn = sqlite3.connect('drumx.db')
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS kits (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    sounds TEXT
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS profiles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    sounds TEXT,
                    loops TEXT
                )
            ''')
            self.conn.commit()
            cursor.close()
        else:
            self.conn = sqlite3.connect('drumx.db')
            self.kits, self.profiles = self.load_data()

    def load_data(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM kits ORDER BY id DESC LIMIT 1')
        kits = cursor.fetchall()
        cursor.execute('SELECT * FROM profiles ORDER BY id DESC LIMIT 1')
        profiles = cursor.fetchall()
        cursor.close()
        return kits, profiles
        pass

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Database()
        return cls._instance

    def close(self):
        self.conn.close()

    def save_kit(self, kit):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO kits (name, sounds) VALUES (?,?)',(kit.name, json.dumps(kit.sounds)))
        self.conn.commit()
        cursor.close()
        pass
    
    def load_kit(self, kit):
        pass


