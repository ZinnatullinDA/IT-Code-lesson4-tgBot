from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    # Command '/start' handler
    await message.answer(text='Привет!\nЯ могу отправлять фото gif с собачками'
                              '\nЧтобы получить:'
                              '\nФото - напиши "фото", "картинка" или "собачка"'
                              '\ngif - напиши "видео" или "гифка"'
                              '\nСсылку - на собачку напиши "ссылка"')
