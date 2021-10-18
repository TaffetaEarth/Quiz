import sqlite3

connection = sqlite3.connect("quizdb.sqlite3")
cursor = connection.cursor()
cursor.execute("CREATE TABLE Quiz (id INTEGER, question TEXT, answers TEXT, "
               "correct_answer INTEGER);")
