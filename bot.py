import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from deep_translator import GoogleTranslator

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Default target language. Users can change it with /setlang <code>
user_target_lang = {}
DEFAULT_LANG = "en"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hi! I'm a translator bot.\n\n"
        "Just send me any text and I'll translate it to English by default.\n\n"
        "Commands:\n"
        "/setlang <code> - set target language (e.g. /setlang fr)\n"
        "/help - show language codes info"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Use ISO language codes, e.g.:\n"
        "en=English, fr=French, es=Spanish, de=German, "
        "yo=Yoruba, ha=Hausa, ig=Igbo, ar=Arabic, zh-CN=Chinese\n\n"
        "Example: /setlang yo"
    )


async def set_lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /setlang <language_code>\nExample: /setlang fr")
        return
    lang_code = context.args[0].lower()
    user_id = update.effective_user.id
    user_target_lang[user_id] = lang_code
    await update.message.reply_text(f"✅ Target language set to: {lang_code}")


async def translate_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.effective_user.id
    target_lang = user_target_lang.get(user_id, DEFAULT_LANG)

    try:
        translated = GoogleTranslator(source="auto", target=target_lang).translate(text)
        await update.message.reply_text(translated)
    except Exception as e:
        logger.error(f"Translation error: {e}")
        await update.message.reply_text(
            "⚠️ Sorry, I couldn't translate that. Check your language code with /help."
        )


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is not set.")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("setlang", set_lang))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_message))

    logger.info("Bot starting...")
    app.run_polling()


if __name__ == "__main__":
    main()
