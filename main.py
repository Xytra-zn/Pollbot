import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your poll bot. Use /createpoll to start a poll.')

def create_poll(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Creating a poll. Use /endpoll to finish it.')

def end_poll(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Poll ended. Results: ...')  # Add logic for displaying results.

def main() -> None:
    token = os.getenv("TOKEN")
    if not token:
        raise ValueError("Telegram bot token not found. Make sure to set the TOKEN environment variable.")

    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('createpoll', create_poll))
    dispatcher.add_handler(CommandHandler('endpoll', end_poll))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
