import logging
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from apscheduler.triggers.interval import IntervalTrigger

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

logging.basicConfig(
    level="INFO",
    format="%(asctime)s [%(levelname)s] %(message)s"
)

async def send_hourly_report(context: ContextTypes.DEFAULT_TYPE):
    text = "📊 Hourly Macro Report\n\n(Dies ist eine Testnachricht – Fetcher folgt)"
    await context.bot.send_message(chat_id=CHAT_ID, text=text)

async def start(update, context):
    await update.message.reply_text("Macro Bot läuft!")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    app.job_queue.run_repeating(
        send_hourly_report,
        interval=3600,
        first=10
    )

    logging.info("Bot gestartet. Scheduler aktiv.")
    app.run_polling()


if __name__ == "__main__":
    main()
