import os
import logging
from pyrogram import Client

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name)

# Initialize the Pyrogram Client
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

if __name__ == "__main__":
    logger.info("Bot Started, Monitoring for Members Leaving and Banning Them")
    app.run()
