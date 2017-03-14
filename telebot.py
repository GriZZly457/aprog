from telebot import TeleBot, types
from time import sleep
from random import choice

TOKEN = "338083790:AAEfqsdkS6DIMZDnd-6SXFmlFwAnDfCw5so"

bot = TeleBot(TOKEN)

@bot.message_handler(commands=["Где ты?","Кто ты?"])
def do_something(message):
	bot.send_message(message.chat.id, "Запускаю ракету на марс")

@bot.message_handler(regexp= "Спам")
def do_something(message):
	i = 0
while True:
	i += 1
bot.send_message(message.chat.id, "Спам" * i)
sleep(0.1)

@bot.message_handler(commands=["Command list:"])
def default_test(message):
	keyboard = types.InlineKeyboardMarkup()
# url_button = types.InlineKeyboardButton(text="ГДЗ", url="https://gdz.ru/")
# keyboard.add(url_button)
url_button = types.InlineKeyboardButton(text="Вот тебе гайд по Clash Royale", url="http://clashroyale-guide.ru/")
keyboard.add(url_button)
url_button = types.InlineKeyboardButton(text=" Вк", url="https://vk.com/")
keyboard.add(url_button)
url_button = types.InlineKeyboardButton(text="Официальный сайт Python", url="https://www.python.org/")
keyboard.add(url_button)
url_button = types.InlineKeyboardButton(text="Гид по Python на русском", url="https://pythonworld.ru/")
keyboard.add(url_button)
bot.send_message(message.chat.id, "Нажимай", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def do_callback(call):
	if call.data == "dead":
		mess = choice(["Ты умер", "Ты молодец", "Ты сдох"])
bot.send_message(call.message.chat.id, mess)
bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Пыщь!")

@bot.message_handler(func=lambda message: True)
def say_hello(message):
	if message.text.lower() == 'Привет':
		bot.send_message(message.chat.id, "Добрый День!")
	if message.text.lower() == 'СаламуАлейкум':
		bot.send_message(message.chat.id, 'ВаалейкумАссалам')
	if message.text.lower() == 'Как дела?':
		bot.send_message(message.chat.id, "Все хорошо")
	if message.text.lower() == 'Как тебя зовут?':
		bot.send_message(message.chat.id, "Меня зовут Махмудин :)")
	if message.text.lower() == 'Чем занимаешься?':
		bot.send_message(message.chat.id, "Нахожусь в разработке")
# if message.text.lower() == 'Сколько тебе лет?':
# bot.send_message(message.chat.id, "ХЗ")
	if message.text.lower() == 'Что делаешь?':
		bot.send_message(message.chat.id, "Выгуливаю покемона")
	if message.text.lower() == 'Кто ты?':
		bot.send_message(message.chat.id, "Я чат-бот, и пока что нахожусь в разработке :)")
	if message.text.lower() == 'На каких языках ты разговариваешь?':
		bot.send_message(message.chat.id, "Пока только на русском, но вскоре будут добавлены и другие языки")
	if message.text.lower() == 'Синий кит':
		bot.send_message(message.chat.id, "Я не занимаюсь такого рода деятельностью")
	else:
		bot.reply_to(message,'Этого вопроса пока нет в моей базе')


if __name__=='__main__':
	bot.polling()