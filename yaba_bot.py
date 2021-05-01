from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import re
import requests, json
from typing import List
from settings import token


def get_course() -> str:
    req = requests.get("https://blockchain.info/ticker")
    j = json.loads(req.text)
    return f"{j['USD']['last']} {j['USD']['symbol']}"

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Я бот, поговори со мной")


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Так как меня написал криворукий смарт,"
                                                                    " то я ничего не умею(\n"
                                                                    f"ну биток стоит {get_course()}")


def smart_self(update: Updater, context):
    replase_message = re.sub(r'[С,с]март ', "cам ", update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Бот говорит что ты {replase_message}")


start_handler = CommandHandler('start', start)
smart_handler = MessageHandler(Filters.regex(r'.*[С,с]март.*'), smart_self)
messege_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(smart_handler)
dispatcher.add_handler(messege_handler)


updater.start_polling()



