# Modul with class player and some functions - predefined for web app kanasta

import sqlite3

connection = sqlite3.connect('kanasta.db')
cursor = connection.cursor()
players_list = []
couples_list = []

class Player():

    def __init__(self, ID, name):
        """Create player with name and score 0 for start"""
        self.ID = ID
        self.name = name
        self.score = 0
        players_list.append(self)

    def update_score(points):
        """Update players score after game"""
        self.score += points

class Couple():

    def __init__(self, ID, player_A, player_B):
        """Create couple of players playing together in partial games"""
        self.ID = ID
        self.player_A = player_A
        self.player_B = player_B
        self.name = '{} & {}'.format(player_A.name, player_B.name)
        self.score = 0
        couples_list.append(self)

    def update_score(points):
        """Update couples score after game"""
        self.score += points


def insert_player(player):
    """inserts player into table players"""
    with connection:
        cursor.execute("""INSERT INTO PLAYERS (PLAYER_ID, NAME, SCORE) 
        VALUES (?, ?, ?)""", (player.ID, player.name, player.score))

def insert_couple(couple):
    """inserts couple into table couples"""
    with connection:
        cursor.execute("""INSERT INTO COUPLES 
        VALUES (?, ?, ?, ?, ?)""", (couple.ID, couple.name, couple.player_A.ID, couple.player_B.ID, couple.score))





