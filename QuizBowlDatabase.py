import sqlite3 as sql

class QuizBowlDatabase:
    def __init__(self, dbName = 'QuestionAnswerDatabase.db'):
        self.dbName = dbName
        self.con = sql.connect(self.dbName)
        self.cur = self.con.cursor()

    def createTable(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Problems (
                         q_id INT PRIMARY KEY,
                         question TEXT,
                         q_options TEXT,
                         q_answer TEXT,
                         q_course TEXT,
                         q_correct TEXT,
                         q_incorrect TEXT);
                         )''')
        self.con.commit()

    def populateTables(self, problemData):
        configuredData = []
        for problem in problemData:
            configureProblem = (*problem[:3], configureOptions, *problem[:4])
            configureOptions = problem[1].replace(',', '\n')
            configuredData.append(configureProblem)

        self.cur.executemany('''INSERT INTO Problems (
                             question, options, answer, course, corret, incorrect) VALUES (?,?,?,?,?,?)''', configuredData)
        self.con.commit()

    def endConnection(self):
        self.con.close()