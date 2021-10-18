connection = sqlite3.connect("quizdb.sqlite3")
cursor = connection.cursor()
cursor.execute("CREATE TABLE Quiz (id TEXT, qunum TEXT, question TEXT, answers TEXT, "
               "correct_answer INTEGER);")
for i in range(5):
    cursor.execute('INSERT INTO (id) Quiz VALUES (' + str(i) + ");")
for i in range(10):
    cursor.execute("INSERT INTO Quiz (qunum) VALUES (" + str(1) + ");")
    cursor.execute("INSERT INTO Quiz (qunum) VALUES (" + str(2) + ");")
for i in range(5):
    for j in range(2):
        cursor.execute("INSERT INTO Quiz")