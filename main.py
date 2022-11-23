from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

BOT_TOKEN = "6367361791:AAFiC8C7kDveJpAYuC7wYniBfuekc66R63k"


async def start(update: Update, context_type: ContextTypes.DEFAULT_TYPE) -> None:
    print("Start Called")
    await update.message.reply_text("Welcome to ChatGPT telegram Bot!!!")


async def info(update: Update, context_type: ContextTypes.DEFAULT_TYPE) -> None:
    print("User Info")
    user_id = update.message.from_user.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    full_name = f"{first_name} {last_name}".strip()
    if full_name:
        await update.message.reply_text(f"{user_id}: {full_name}")
    else:
        await update.message.reply_text(f"User ID: {user_id}")


def run():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    print("Application started!")
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("info", info))
    application.run_polling()


if __name__ == "__main__":
    run()
