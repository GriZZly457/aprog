
import sqlite3
from collections import OrderedDict

QUESTIONS = OrderedDict({
	"surname": "Назови свою фамилию",
	"age": "Сколько тебе лет?",
	"class": "Какая у тебя любимая игра?",
	"school": "Где ты учишься?",
	"fullness":"На сколько развит твой мозг(от 1 до 10)?"

})

class MyBot:
	

	def __init__(self,name):
		self.conn = sqlite3.connect("bot_data.db")
		self.curs = self.conn.cursor()
		self.name = name


	def __del__(self):
		self.curs.close()
		self.conn.close()


	def add_question(self):
		ins = "INSERT OR REPLACE INTO questions VALUES (?,?)"
		for key, values in QUESTIONS.items():
			self.curs.execute(ins,(key,values))
		self.conn.commit()


	def add_friend(self,*args):
		ins = "INSERT OR REPLACE INTO friends VALUES (?,?,?,?,?,?)"
		self.curs.execute(ins,args)
		self.conn.commit()


	def create_table(self):
		# self.curs.execute("DROP TABLE questions")
		self.curs.execute("""CREATE TABLE IF NOT EXISTS questions(
			qtype VARCHAR(30) PRIMARY KEY,
			question VARCHAR(50)
			)""")
		self.add_question()
		rows = self.curs.execute("SELECT * FROM questions")
		crt ="CREATE TABLE IF NOT EXISTS friends (name VARCHAR(60) PRIMARY KEY,"
		for row in rows:
			m = "{0} VARCHAR(30),".format(row[0])
			crt += m
		crt = crt[:-1] + ")"

		self.curs.execute(crt)

		self.add_friend("Аиемен", "Амиереко", "24", "Нет", "В мочкве", "Да")
		
		rows = self.curs.execute("SELECT * FROM friends")
		print(rows.fetchall())



	def ask_question(self,name):
		print("Рад знакомству", name)
		rows = self.curs.execute("SELECT * FROM questions")
		data = []
		for row in rows:
			print(row[1])
			answer = input()
			data.append(answer)
		self.add_friend(name,*data)

	def is_known(self,name):
		row = self.curs.execute("SELECT name FROM friends")
		# print(row.fetchall())
		names = [n[0] for n in row]
		print(names)
		return name in names


	def about_you(self,name):
		print("Лол , знаю тебя. Я вычислил тебя по IP")
		row = self.curs.execute("SELECT * FROM friends WHERE name = ?", (name,))
		row = row.fetchone()
		print("Тебя зовут {0[0]},твоя фамилия {0[1]},твой возраст {0[2]}, твоя любимая игра - {0[3]},учишься в {0[4]}е, твой мозг развит на  {0[5]} процентов".format(row))

	def start_chat(self):
		name = input("Меня зовут {0.name}, а как тебя?".format(self))
		if self.is_known(name):
		 	self.about_you(name)
		else:
			self.ask_question(name)


bot = MyBot("Бот Максим")


bot.create_table()
bot.start_chat()