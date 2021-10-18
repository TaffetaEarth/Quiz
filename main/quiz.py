import sqlite3
import random


def level(level, r_answ):
    cursor.execute("SELECT qu-text, answers, correct_answer FROM Quiz WHERE "
                   "id = " + str(level) + ";")
    quest = random.choice([cursor.fetchall()[0], cursor.fetchall()[1]])
    print(quest[0])
    print("Варианты ответов:")
    print(quest[1])
    answ = int(input())
    if quest[2] == answ:
        r_answ += 1
    if level == 5:
        if r_answ == level:
            print("Вы справились!")
        else:
            print("Вы не справились!")
    level(level+1, r_answ)


r_answ = 0
connection = sqlite3.connect("quizdb.sqlite3")
cursor = connection.cursor()
level(1, 0)
