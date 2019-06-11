import sqlite3
from background import players_list, couples_list, Player, Couple, insert_player, insert_couple
from itertools import combinations

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

cursor.execute("""
CREATE TABLE COUPLES (
    COUPLE_ID INT PRIMARY KEY,
    NAME TEXT,
    PLAYER_1_ID INT,
    PLAYER_2_ID INT,
    SCORE INT,
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
""")

################################ CREATING PLAYERS #############################

pl_1 = Player(1, "Tonda")
pl_2 = Player(2, 'Vašek')
pl_3 = Player(3, 'Vojta')
pl_4 = Player(4, 'Jirka')

insert_player(pl_1)
insert_player(pl_2)
insert_player(pl_3)
insert_player(pl_4)

connection.commit()

############################### CREATING COUPLES ##############################

players_combinations = list(combinations(range(1, len(players_list)+1), 2))
for tupl in players_combinations:
    lis = list(tupl)
    players_combinations[players_combinations.index(tupl)] = lis

for x in players_combinations:
    pl_A = players_list[x[0]-1]
    pl_B = players_list[x[1]-1]
    new_couple = Couple(players_combinations.index(x)+1, pl_A, pl_B)
    insert_couple(new_couple)

################################ CREATING GAMES ###############################

# Tohle by se melo zadavat v aplikaci na strance games
# loser a winner couple by se vybiraly z rozbalovaci zalozky, body by se psaly rucne
# ID by se generovalo podle poradi
# A pak by to pripocitavalo score prislusnym couple a players

cursor.execute("""INSERT INTO GAMES VALUES 
    (1, 1, 2, 6000, 3000),
    (2, 3, 2, 5820, 2600),
    (3, 4, 1, 4000, 3000),
    (4, 3, 2, 8520, 500)
""")

cursor.execute("""SELECT * FROM GAMES""")
print(cursor.fetchall())

connection.commit()
connection.close()