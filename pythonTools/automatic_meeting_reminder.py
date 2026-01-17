import schedule, time
import telebot

bot = telebot.TeleBot("TELEGRAM_BOT_TOKEN")
CHAT_ID = "CHAT_ID"

def reminder():
    bot.send_message(CHAT_ID, "Meeting starts in 5 minutes ⏰")

schedule.every().day.at("09:55").do(reminder)

while True:
    schedule.run_pending()
    time.sleep(30)
