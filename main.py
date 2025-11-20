from pyrogram import Client, filters

api_id = 30885867
api_hash = "215559ea97000a748b444f3330f76659"
bot_token = "7898349005:AAGXxM_-L_GcNqaaarme58ZaxgZc_zAdNE"

app = Client(
    "/tmp/auto_accept_bot",   # Important for Render
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_chat_join_request()
async def approve_request(_, req):
    try:
        await req.approve()
        print(f"Approved: {req.from_user.first_name}")
        await app.send_message(
            req.chat.id,
            f"👋 Welcome {req.from_user.mention}! You are approved automatically."
        )
    except Exception as e:
        print("Error:", e)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply("🔥 Auto Accept Bot is active and running!")

print("Bot is running...")
app.run()
