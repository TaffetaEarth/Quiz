import sqlite3
import random


def level(levelnum, r_answ):
    data = cursor.execute("SELECT question, answers, correct_answer FROM quiz WHERE id = " + str(levelnum) + ";")
    print(data.fetchall())
    quest = random.choice([data.fetchall()[0], data.fetchall()[0]])
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
    level(levelnum+1, r_answ)


r_answ = 0
connection = sqlite3.connect("/home/sirius/Quiz/main/quizdb.db")
cursor = connection.cursor()
level(1, 0)
