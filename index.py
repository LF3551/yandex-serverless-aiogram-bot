import json
import os
from aiogram import Bot, Dispatcher, types as aiotypes
TOKEN = os.getenv("TOKEN")

async def process_event(event, dp: Dispatcher):
    print(event['body'])
    print(event)
    update = json.loads(event['body'])
    print("Got TG update, started processing")
    Bot.set_current(dp.bot)
    update = aiotypes.Update.to_object(update)
    await dp.process_update(update)

async def handler(event, context):
    print(event)
    bot = Bot(TOKEN)
    dp = Dispatcher(bot)
    @dp.message_handler(commands=['start'])
    async def get_voice(message: aiotypes.Message):
        await message.reply("Не получилось распознать")
    await process_event(event, dp)
    return {'statusCode': 200, 'body': 'ok'}
