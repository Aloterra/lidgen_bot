import telebot
from telebot import types
from config import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    first_level_button = types.KeyboardButton("Первый уровень")
    second_level_button = types.KeyboardButton("Второй уровень")
    third_level_button = types.KeyboardButton("Третий уровень")
    markup.add(first_level_button, second_level_button, third_level_button)
    bot.send_message(message.chat.id, '''Привет! Нажми на старт и выбери свой уровень для укрепления голеностопного сустава. 
P.S. 
1 уровень - Мобилизационные упражнения;
2 - уровень - Разогревающие упражнения;
3 - уровень - Укрепляющие упражнения''', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def button_answer(message):
    if message.text == "Первый уровень":
        bot.send_message(message.chat.id, 'Первый уровень')
        bot.send_video(message.chat.id, video=FIRST_VIDEO_ID)
    elif message.text == "Второй уровень" \
            and bot.get_chat_member(-1002079902941, message.from_user.id).status not in ['left', 'banned']:
        bot.send_message(message.chat.id, 'Второй уровень')
        bot.send_video(message.chat.id, video=SECOND_VIDEO_ID)
    elif message.text == "Третий уровень" \
            and bot.get_chat_member(-1002079902941, message.from_user.id).status not in ['left', 'banned']:
        bot.send_message(message.chat.id, 'Третий уровень')
        bot.send_video(message.chat.id,
                       video=THIRD_VIDEO_ID)
    elif bot.get_chat_member(-1002079902941, message.from_user.id).status in ['left', 'banned'] and message.text in ["Третий уровень", "Второй уровень"]:
        subscribe_markup = types.InlineKeyboardMarkup(row_width=1)
        subscribe_button = types.InlineKeyboardButton("Подписаться", url='https://t.me/kalderapro')
        subscribe_markup.add(subscribe_button)
        bot.send_message(message.chat.id, """Для продолжения просмотра упражнений, пожалуйста, подпишись сюда""", reply_markup=subscribe_markup)
    else:
        bot.send_message(message.chat.id, 'Неизвестная команда')


bot.polling()