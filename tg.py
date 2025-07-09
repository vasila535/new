from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
import asyncio

Token = '7573903717:AAFvvMNkEQjq8en1JlUr1CDi0rRXQnX0M78'
bot = Bot(token=Token)
dp = Dispatcher()
user_data = {}
channel ="@Zayafkalar_kanali"

@dp.message(Command('start'))
async def starts(message:types.Message):
    user_id =message.from_user.id
    user_data[user_id] = {}

    await message.answer(f'Assalomu aleykum!/n'
                         f'Iltimos ism kiriting')
    print(1,user_data)
    await ask_phone(message)

async def ask_phone(message:types.Message):
    user_id = message.from_user.id
    name = message.text
    user_data[user_id]['name'] = name
    print(2,user_data)
    button =[[types.KeyboardButton(text='Raqam jomatish',request_contact=True)]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button,resize_keyboard=True)
    await message.answer(f'Iltimos telefon raqamni kiriting',reply_markup=keyboard)
    await ask_age(message)

async def ask_age(message:types.Message):
    user_id =message.from_user.id
    phone = message.text
    user_data[user_id]['phone']=phone
    print(3,user_data)
    await message.answer(f"Yosh kiriting:")
    await full_data(message)
