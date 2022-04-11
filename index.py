import json
import os
from aiogram import Bot, Dispatcher, types as aiotypes
TOKEN = os.getenv("TOKEN")

async def process_event(event, dp: Dispatcher):
    update = json.loads(event['body'])
    Bot.set_current(dp.bot)
    update = aiotypes.Update.to_object(update)
    await dp.process_update(update)

async def handler(event, context):
    print(event)
    bot = Bot(TOKEN)
    dp = Dispatcher(bot)
    @dp.message_handler(commands=['start'])
    async def send_message(message: aiotypes.Message):
        await message.reply("Hello user")
    await process_event(event, dp)
    return {'statusCode': 200, 'body': 'ok'}
