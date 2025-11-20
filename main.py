import os
from pyrogram import Client, filters

# Read credentials from environment variables (recommended)
# If you prefer hardcoding (not recommended), replace os.environ.get(...) with the literal values.
API_ID = int(os.environ.get("API_ID", "30885867"))
API_HASH = os.environ.get("API_HASH", "215559ea97000a748b444f3330f76659")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# Use /tmp session on Render (writable)
SESSION_NAME = "/tmp/auto_accept_bot"

app = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workdir="/tmp"  # ensure working dir is writable (optional)
)


@app.on_chat_join_request()
async def approve_request(client, req):
    try:
        # Approve the join request
        await req.approve()
        name = req.from_user.first_name or str(req.from_user.id)
        print(f"Approved: {name}")

        # Send a welcome message in the chat (optional)
        try:
            await app.send_message(
                req.chat.id,
                f"👋 Welcome {req.from_user.mention}! You have been approved automatically."
            )
        except Exception as send_exc:
            print("Failed to send welcome message:", send_exc)

    except Exception as e:
        print("Error while approving join request:", e)


@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply("🔥 Auto Accept Bot is active and running!")


if __name__ == "__main__":
    print("Bot is starting...")
    # This will block and run the bot until stopped
    app.run()
