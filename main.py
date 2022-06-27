from aiogram import Bot, types

from aiogram.dispatcher import Dispatcher  # отслеживание сообщений от пользователя

from aiogram.utils import executor

import markups as nav

import information

TOKEN = '5465375647:AAEPTkq8lk1s4GOFwR5fiwBeuXOUBDob644'

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])  # обозачает событие в чате, команда через /

async def command_start(message: types.Message):  # асинхронность

    await bot.send_message(message.from_user.id, "Здравствуйте, {0.first_name}!".format(message.from_user),

                           reply_markup=nav.mainMenu)  # на команду появляется меню

@dp.message_handler()

async def bot_message(message: types.Message):

    # await bot.send_message(message.from_user.id, message.text)

    if message.text == 'Кто мы?':

        photo = open('icon.jpeg', 'rb')

        text = '*Special Care* - организация, которая помогает родителям детей с ограниченными ' \

               'возможностями.\n\n\nС нашей помощью родители смогут узнать о _правильном воспитании, ' \

               'поддержке и развитии своего ребёнка._\n\n\nДля нас важно, чтобы каждый особый ребенок ' \

               'получил *должностный уход* и *заслуживаемую любовь.*\n\nИменно поэтому мы *не требуем ' \

               'никакой платы* за наши услуги и наши ресурсы доступны для *каждого!*\n\n\n*Помогаем ' \

               'сделать этот мир лучше! ✨*'

        await bot.send_photo(message.from_user.id, photo, caption=text, parse_mode="Markdown")

    if message.text == 'Консультация с экспертом':

        await bot.send_message(message.from_user.id,

                               'Для связи с экспертом Вам достаточно написать этому боту @QWANT2022bot и ваш запрос '

                               'попадет к профессионалам!')

    if message.text == 'Обратная связь':

        await bot.send_message(message.from_user.id, 'Переходим в меню обратной связи...', reply_markup=nav.otherMenu)

    if message.text == 'Главное меню':

        await bot.send_message(message.from_user.id, 'Переходим в главное меню...', reply_markup=nav.mainMenu)

    if message.text == 'Оставьте нам отзыв':

        await bot.send_message(message.from_user.id, "Оставьте этому боту @QWANT2022bot свой отзыв")


