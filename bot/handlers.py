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
