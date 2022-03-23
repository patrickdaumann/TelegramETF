from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

#Api Key aus SECRET Datei auslesen
with open(".\Telegram\SECRET", "r") as secret:
    TelegramBotApiKey = secret.readline()

#Quelle: https://python-telegram-bot.org/
def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def test(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hallo, das ist ein Test. Und es funktioniert!")


updater = Updater(TelegramBotApiKey)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('test', test))

updater.start_polling()
updater.idle()
