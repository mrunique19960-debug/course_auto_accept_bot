from pyrogram import Client, filters

api_id = 30885867  # FIXED
api_hash = "215559ea97000a748b444f3330f76659"
bot_token = "7898349005:AAGnYnhIgODx3iIAC417yWDd_Fgr-y8F9G8"

app = Client(
    "/tmp/auto_accept_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_chat_join_request()
async def approve_request(client, req):
    try:
        await req.approve()
        print(f"Approved: {req.from_user.first_name}")
        await app.send_message(
            req.chat.id,
            f"👋 Welcome {req.from_user.mention}, you are approved automatically!"
        )
    except Exception as e:
        print("Error:", e)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply("🔥 Auto Accept Bot is active!")

print("Bot is running...")
app.run()
