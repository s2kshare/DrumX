import sqlite3
import os
import json
import datetime

from DrumX.AudioSuite import AudioEngine

# Definitions
# Kit / Kits    = Total of 16 DP controls
# Profile / Profiles = Total of 3 Profiles

class Database:
    _instance = None

    def __init__(self):
        is_new = not os.path.exists('drumx.db')
        self.conn = sqlite3.connect('drumx.db')
        if is_new:
            self._create_tables()
            self.kits = []
            self.profiles = []
        else:
            self.kits, self.profiles = self.load_data()

    def _create_tables(self):
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

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Database()
        return cls._instance

    def close(self):
        self.conn.close()
    
    def load_initial_data(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM kits ORDER BY id DESC LIMIT 1')
        kits = cursor.fetchall()
        cursor.execute('SELECT * FROM profiles ORDER BY id DESC LIMIT 1')
        profiles = cursor.fetchall()
        cursor.close()
        return kits, profiles
    
    def load_kit(self, name=None):
        if name is None:
            pass
        pass

    def save_kit(self, name=None):
        if name is None:
            latest_id = self.kits[0][0] if self.kits else 0
            name = f"Session {latest_id + 1} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

        kit = AudioEngine.get_instance().sounds
        print(kit)
        cursor = self.conn.cursor()
        print(kit)
        cursor.execute('INSERT INTO kits (name, sounds) VALUES (?,?)', (name, json.dumps(kit)))
        self.conn.commit()
        cursor.close()

        # Update internal cache
        self.kits, self.profiles = self.load_data()

    def load_kit(self, kit):
        pass
