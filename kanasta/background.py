# Modul with class player and some functions - predefined for web app kanasta

import sqlite3

connection = sqlite3.connect('kanasta.db')
cursor = connection.cursor()

class Player():

    def __init__(self, ID, name):
        """Create player with name and score 0 for start"""
        self.ID = ID
        self.name = name
        self.score = 0

    def update_score(points):
        """Update players score after game"""
        self.score += points

class Couple():

    def __init__(self, ID, player_1, player_2):
        self.ID = ID
        self.name = '{} a {}'.format(player_1.name, player_2.name)
        self.score = 0

def insert_player(player):
    """inserts player into table players"""
    with connection:
        cursor.execute("""INSERT INTO PLAYERS VALUES (?, ?, ?)""", (player.ID, player.name, player.score))





