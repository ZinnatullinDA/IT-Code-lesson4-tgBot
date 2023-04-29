from aiogram import types

from loader import dp
from utils.dog_generator import Dog

@dp.message_handler()
async def dog_generator(message: types.Message):
    command = message.text.lower()
    dog = Dog()

    if command == 'ссылка':
        await message.answer(dog.get_any_dog())
    elif command in ('гифка', 'видео'):
        await message.answer_video(dog.get_vid_dog())
    elif command in ('фото', 'картинка', 'собачка'):
        await message.answer_photo(dog.get_pic_dog())
    else:
        await message.answer('Неизвестая команда :(')
    return