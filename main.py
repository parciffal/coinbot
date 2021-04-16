from aiogram.bot import Bot
from aiogram.dispatcher import Dispatcher
from config import TOKEN
import logging
from aiogram import types, executor


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.callback_query_handler(lambda call: call.data in ['verified'])
async def call_one(call):
    try:
        if call.data == 'verified':
            await bot.send_message(call.message.chat.id, 'You are now verified my friend,\nwelcome to the Ready Telegram 🎉')
    except Exception as e:
        print(repr(e))


@dp.message_handler(commands = ['chart'])
async def helo(message: types.Message):
    try:
        await bot.send_message(message.chat.id, '📈 The Ready chart is here my friend!: \nhttps://poocoin.app/tokens/0x264a603A40B7FF7B41dF141f836A38Dc93341eb3')
    except Exception as e:
        print(repr(e))


@dp.message_handler(commands=['price'])
async def hello(message: types.Message):
    try:
        await bot.send_message(message.chat.id, 'hello')

    except Exception as e:
        print(repr(e))


@dp.message_handler(commands=['verify'])
async def hell(message: types.Message):
    try:
        markup = types.InlineKeyboardMarkup()
        butt = types.InlineKeyboardButton('Click here to prove your not a robot', callback_data='verified')
        markup.add(butt)
        await bot.send_message(message.chat.id, 'Hello {username}'.format(username=message.from_user.username), reply_markup=markup)

    except Exception as e:
        print(repr(e))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

