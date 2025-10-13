import sqlite3

connexion = sqlite3.connect('./data/database')
cursor = connexion.cursor()

# print(cursor.execute('''
#                      SELECT *
#                      FROM students
#                      '''))