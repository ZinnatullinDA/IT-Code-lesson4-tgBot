from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp


@dp.message_handler(CommandHelp())
async def cmd_help(message: types.Message):
    # Command '/help' handler
    await message.answer(text='Я могу отправлять фото или gif с собачками'
                              '\nЧтобы получить:'
                              '\nФото - напиши "фото", "картинка" или "собачка"'
                              '\ngif - напиши "видео" или "гифка"'
                              '\nСсылку - на собачку напиши "ссылка"')
