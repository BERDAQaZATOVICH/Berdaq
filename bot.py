import telebot 
import random

from telebot import types #keyboard module

TOKEN = "6202684917:AAGeVD9ghPFZAg3o2W0gE2cYgvdAqAzLLHY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def game_start(message):
  # Build keyboard
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn1 = types.KeyboardButton('Qudiq🤜')
  btn2 = types.KeyboardButton('Qayshi✌️')
  btn3 = types.KeyboardButton('Qagaz✋')
  keyboard.add(btn1, btn2, btn3)
  bot.send_message(message.chat.id, "Qudiq🤜,Qayshi✌️,Qagaz✋, bir, eki, u'sh! Birewini tanlan':", reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def game(message):
  choice = random.choice(['Qudiq🤜', 'Qayshi✌️', 'Qagaz✋'])
  if message.text == choice:
    bot.send_message(message.chat.id, "Ten'lik! Oynimizdi jan'adan baslaw ushin /start komandasini kiritin'")
  else:
    if message.text == 'Qudiq🤜':
      if choice == 'Qayshi✌️':
        bot.send_message(message.chat.id, "Je'nis penen Sizdi qutliqmayman! Men {}ni tankap edim. Oynimizdi jan'adan baslaw ushin /start komandasini kiritin'".format(choice))
      else:
        bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите /start'.format(choice))
    elif message.text == 'Qayshi✌️':
      if choice == 'Qagaz✋':
        bot.send_message(message.chat.id, "Je'nis penen Sizdi qutliqmayman! Men {}ni tankap edim. Oynimizdi jan'adan baslaw ushin /start komandasini kiritin'".format(choice))
      else:
        bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите /start'.format(choice))
    elif message.text == 'Qagaz✋':
      if choice == 'Qudiq🤜':
        bot.send_message(message.chat.id, "Je'nis penen Sizdi qutliqmayman! Men {}ni tankap edim. Oynimizdi jan'adan baslaw ushin /start komandasini kiritin'".format(choice))

      else:
        bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите /start'.format(choice))
            
bot.polling(none_stop=True)
