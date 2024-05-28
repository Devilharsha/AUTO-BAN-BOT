import os
from pyrogram import filters
from main import logger

# Define the chat or channel ID to monitor
chat_id = os.getenv("CHAT_ID")

# Function to set up message handlers
def setup_handlers(client):
    @client.on_message(filters.chat(chat_id) & filters.left_chat_member)
    async def on_member_left(_, message):
        member = message.left_chat_member
        try:
            if member:
                user = member.user
                logger.info(f"Banning user: {user.first_name} (ID: {user.id})")
                await client.kick_chat_member(chat_id, user.id)
        except Exception as e:
            error_message = str(e)
            logger.error(f"An error occurred: {error_message}")

    @client.on_message(filters.command(["start", "/start"]) & filters.chat(chat_id) | filters.private)
    async def start_command(_, message):
        await message.reply_text("Welcome to the Channel Monitor Bot! I will automatically ban members who leave the channel andd never allow them.")

    @client.on_message(filters.command("ping") & filters.chat(chat_id) | filters.private)
    async def ping_command(_, message):
        await message.reply_text("Pong!")
