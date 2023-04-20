from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

API_TOKEN = ''
with open('token.txt', 'r') as f:
    API_TOKEN = f.readline().rstrip()

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Hi, I am Echo echo, text me something')

@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Text me something, I\'ll echo your message')

@dp.message()
async def send_echo(message):
    await message.reply(text=message.text)

if __name__ == '__main__':
    dp.run_polling(bot)
