import telebot
from ETFParser.ExtraETFParser import ExtraetfETF

with open(".\SECRET", "r") as secret:
    TelegramBotApiKey = secret.readline()

bot = telebot.TeleBot(TelegramBotApiKey)

@bot.message_handler(commands=['Hello', 'hello'])
def hello(message):
    bot.send_message(message.chat.id, "Hello")

@bot.message_handler(commands=['ETF', 'etf'])
def etf(message):
    RequestISIN = message.text.split()[1]
    etf = ExtraetfETF(RequestISIN)
    etf.parse()
    data = etf.CreateString()

    bot.send_message(message.chat.id, data)

bot.polling()

