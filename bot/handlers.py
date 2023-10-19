
from pyrogram import filters
from main import app, logger

# Define the chat or channel ID to monitor
chat_id = os.getenv("CHAT_ID")

# Member left handler
@app.on_message(filters.chat(chat_id) & filters.left_chat_member)
async def on_member_left(client, message):
    member = message.left_chat_member
    try:
        if member:
            user = member.user
            logger.info(f"Banning user: {user.first_name} (ID: {user.id})")
            await client.kick_chat_member(chat_id, user.id)
    except Exception as e:
        logger.error(f"An error occurred: {str(e})")

# Start command handler
@app.on_message(filters.command("start") & filters.chat(chat_id))
async def start_command(client, message):
    await message.reply_text("Welcome to the Channel Monitor Bot! I will automatically ban members who leave the channel.")

# Ping command handler
@app.on_message(filters.command("ping") & filters.chat(chat_id))
async def ping_command(client, message):
    await message.reply_text("Pong!")
