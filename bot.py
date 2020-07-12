import requests 
from bs4 import BeautifulSoup as BS
import telebot
from telebot import types 
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['world'])
def world(message):
#    bot.send_message(message.chat.id, 'Если хотите узнать погоду со всего мира напишите боту название города которого вы хотите узнать(Примечание:Эта функция может вас не понять если вы введете некорректное названия городa/области )')
    bot.send_message(message.chat.id, 'Это функция в разработке:)')

@bot.message_handler(commands= ['start'])
def main(message):
    img = open('static/KG.png', 'rb')
    bot.send_sticker(message.chat.id, img)
    #keyboards
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Бишкек')
    item2 = types.KeyboardButton('Талас')
    item3 = types.KeyboardButton('Баткен')
    item4 = types.KeyboardButton('Каинды')
    item5 = types.KeyboardButton('Кант')
    item6 = types.KeyboardButton('Ат-Баши')
    item7 = types.KeyboardButton('Токмак')
    item8 = types.KeyboardButton('Кара-Балта')
    item9 = types.KeyboardButton('Каракол')
    item10 = types.KeyboardButton('Кызыл-суу')
    item11 = types.KeyboardButton('О боте')
    markup.add(item1,item2, item3, item4,item5,item6, item7, item8, item9, item10, item11)

    bot.send_message(message.chat.id, 'Привет {0.first_name}, этот бот создан для того, чтобы вам помочь узнать\n погоду Кыргызстана!\n '.format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types = 'text')
def speak(message):
    if message.chat.type == 'private':
        if message.text == 'Бишкек':

            town = 'Бишкек'
            url = requests.get('https://sinoptik.ua/погода-' + town)
            html = BS(url.content, 'html.parser')
                
            for el in html.select('#content'):
                t_min = el.select('.temperature .min')[0].text
                t_max = el.select('.temperature .max')[0].text
                text = el.select('.wDescription .description')[0].text


            bot.send_message(message.chat.id, t_min + ', ' + t_max + '\n' + text)

        elif message.text == 'Талас':

            town = 'Талас'
            url = requests.get('https://sinoptik.ua/погода-' + town)
            html = BS(url.content, 'html.parser')
                
            for el in html.select('#content'):
                t_min = el.select('.temperature .min')[0].text
                t_max = el.select('.temperature .max')[0].text
                text = el.select('.wDescription .description')[0].text


            bot.send_message(message.chat.id, t_min + ', ' + t_max + '\n' + text)



        elif message.text == 'Баткен':

            town = 'Баткен'
            url = requests.get('https://sinoptik.ua/погода-' + town)
            html = BS(url.content, 'html.parser')
                
            for el in html.select('#content'):
                t_min = el.select('.temperature .min')[0].text
                t_max = el.select('.temperature .max')[0].text
                text = el.select('.wDescription .description')[0].text
            
            bot.send_message(message.chat.id, t_min + ', ' + t_max + '\n' + text)       

        elif message.text == 'Каинды':

            town = 'Каинды'
            url = requests.get('https://sinoptik.ua/погода-' + town)
            html = BS(url.content, 'html.parser')
                
            for el in html.select('#content'):
                t_min = el.select('.temperature .min')[0].text
                t_max = el.select('.temperature .max')[0].text
                text = el.select('.wDescription .description')[0].text


            bot.send_message(message.chat.id, t_min + ', ' + t_max + '\n' + text)

        elif message.text == 'Кант':

            town = 'Кант'
            url = requests.get('https://sinoptik.ua/погода-' + town)
            html = BS(url.content, 'html.parser')
                
            for el in html.select('#content'):
                t_min = el.select('.temperature .min')[0].text
                t_max = el.select('.temperature .max')[0].text
                text = el.select('.wDescription .description')[0].text


            bot.send_message(message.chat.id, t_min + ', ' + t_max + '\n' + text)


        elif message.text == 'Ат-Баши':

            town = 'Ат-Баши'
            url = requests.get('https://sinoptik.ua/погода-' + town)
            html = BS(url.content, 'html.parser')
                
            for el in html.select('#content'):
                t_min = el.select('.temperature .min')[0].text
                t_max = el.select('.temperature .max')[0].text
                text = el.select('.wDescription .description')[0].text


            bot.send_message(message.chat.id, t_min + ', ' + t_max + '\n' + text)

        elif message.text == 'Токмак':

            town = 'Токмак'
            url = requests.get('https://sinoptik.ua/погода-' + town)
            html = BS(url.content, 'html.parser')
                
            for el in html.select('#content'):
                t_min = el.select('.temperature .min')[0].text
                t_max = el.select('.temperature .max')[0].text
                text = el.select('.wDescription .description')[0].text

            bot.send_message(message.chat.id, t_min + ', ' + t_max + '\n' + text)

        elif message.text == 'Кара-Балта':

            town = 'Кара-Балта'
            url = requests.get('https://sinoptik.ua/погода-' + town)
            html = BS(url.content, 'html.parser')
                
            for el in html.select('#content'):
                t_min = el.select('.temperature .min')[0].text
                t_max = el.select('.temperature .max')[0].text
                text = el.select('.wDescription .description')[0].text

            bot.send_message(message.chat.id, t_min + ', ' + t_max + '\n' + text)
        elif message.text == 'Каракол':

            town = 'Каракол'
            url = requests.get('https://sinoptik.ua/погода-' + town)
            html = BS(url.content, 'html.parser')
                
            for el in html.select('#content'):
                t_min = el.select('.temperature .min')[0].text
                t_max = el.select('.temperature .max')[0].text
                text = el.select('.wDescription .description')[0].text


            bot.send_message(message.chat.id, 'В Каракол\n ' + t_min + ', ' + t_max + '\n' + text)
        elif message.text == 'Кызыл-суу':

            town = 'Кызыл-суу'
            url = requests.get('https://sinoptik.ua/погода-' + town)
            html = BS(url.content, 'html.parser')
                
            for el in html.select('#content'):
                t_min = el.select('.temperature .min')[0].text
                t_max = el.select('.temperature .max')[0].text
                text = el.select('.wDescription .description')[0].text


            bot.send_message(message.chat.id, 'В Кызыл-суу\n' + t_min + ', ' + t_max + '\n' + text)

        elif message.text == 'О боте':
            bot.send_message(message.chat.id, 'Бот написан на языке программировании python,\n при помощи таких библиотек как: pyTelegramBotAPI, requests, BeautifulSoup4\nПарсинг зделан с сайта: sinoptik.ua/\nАвтор проекта: Саматов Дастан')

        else:
            bot.send_message(message.chat.id, 'Извините я вас не понял:( пропишите /start')


if __name__ == '__main__':
    bot.polling(none_stop = True)