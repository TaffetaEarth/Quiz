import sqlite3
import random


def level(levelnum):
    data = cursor.execute("SELECT question, answers, correct_answer FROM quiz WHERE id = " + str(levelnum) + ";")
    quest = random.choice([data.fetchone(), data.fetchone()])
    print(quest[0])
    print("Варианты ответов:")
    print(str(quest[1]))
    print("Введите ваш ответ:")
    answinput = input()
    if answinput.isdigit() and int(answinput) < 5:
        answ = int(answinput)
        if quest[2] == answ:
            if levelnum == 5:
                print("Вы справились!")
            else:
                print("Вы ответили верно! Следующий вопрос:\n")
                level(levelnum + 1)
        else:
            print("Вы ответили неверно!")
    else:
        print("Неправильный ввод!")


connection = sqlite3.connect("/home/sirius/Quiz/main/quizdb.db")
cursor = connection.cursor()
level(1)
