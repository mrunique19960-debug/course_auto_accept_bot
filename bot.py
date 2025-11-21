from telegram import Update
from telegram.ext import Application, ChatJoinRequestHandler, ContextTypes

TOKEN = "7898349005:AAGXxM_-L_GcNnqaaarme58ZaxgZc_zAdNE"

async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.chat_join_request.chat.id
    user_id = update.chat_join_request.from_user.id

    await context.bot.approve_chat_join_request(chat_id, user_id)
    print(f"Approved {user_id} to join {chat_id}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(approve))
    print("🤖 Bot is running... Waiting for join requests")
    app.run_polling()

if __name__ == "__main__":
    main()


