import sqlite3
from background import Player, Couple, insert_player

connection = sqlite3.connect('kanasta.db')

cursor = connection.cursor()

cursor.execute("""DROP TABLE IF EXISTS PLAYERS""")
cursor.execute("""DROP TABLE IF EXISTS COUPLES""")
cursor.execute("""DROP TABLE IF EXISTS GAMES""")

############### CREATING TABLES: PLAYERS, COUPLES, GAMES ########################
cursor.execute("""
CREATE TABLE PLAYERS (
    PLAYER_ID INT PRIMARY KEY,
    NAME TEXT,
    SCORE INT)
""")

'''cursor.execute("""
CREATE TABLE COUPLES (
    COUPLE_ID INT PRIMARY KEY,
    PLAYER_1_ID INT,
    PLAYER_2_ID INT,
    FOREIGN KEY(PLAYER_1_ID) REFERENCES PLAYERS(PLAYER_ID),
    FOREIGN KEY(PLAYER_2_ID) REFERENCES PLAYERS(PLAYER_ID)
    )
""")

cursor.execute("""
CREATE TABLE GAMES (
    GAME_ID INT PRIMARY KEY,
    WINNER_ID INT,
    LOSER_ID INT,
    WINNER_POINTS INT,
    LOSER_POINTS INT,
    FOREIGN KEY(WINNER_ID) REFERENCES COUPLES(COUPLE_ID),
    FOREIGN KEY(LOSER_ID) REFERENCES COUPLES(COUPLE_ID)
    )
""")'''

################################ CREATING PLAYERS #############################
pl_1 = Player(1, 'Tonda')
pl_2 = Player(2, 'Vašek')

co_1 = Couple(1, pl_1, pl_2)

insert_player(pl_1)
insert_player(pl_2)

fff = cursor.execute("""SELECT * FROM PLAYERS""")
for f in fff:
    print(f)

print(co_1.ID, co_1.name, co_1.score)

connection.commit()
connection.close()