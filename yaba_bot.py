from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from settings import token

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Я яба-бот, поговори со мной")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Так как меня написал криворукий смарт,"
                                                                    " то я ничего не умею(\n"
                                                                    "могу только повторить :"+update.message.text)

start_handler = CommandHandler('start', start)
messege_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(messege_handler)

updater.start_polling()



