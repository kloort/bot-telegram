import telebot
from telebot import types



token = "токен"
bot = telebot.TeleBot(token)

name = ''
surname = ''
age = 0


@bot.message_handler(commands=['button']) #Обработчик команды  button
def button_message(message): 
    """Функция создаёт клавиатуру и кнопки"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # клавиатура
    item1 = types.KeyboardButton("Регистрация") # кнопка 1
    item2 = types.KeyboardButton("Хренатень") # кнопка 2
    markup.add(item1, item2)                # Добавление кноопок на клавиатуру
    bot.send_message(message.chat.id,'Выберите функцию',reply_markup=markup)

@bot.message_handler(content_types=['text']) # Обработчик текста (любого)
def start(message):
    if message.text == 'Регистрация' or message.text == "/reg":
        form_reg(message)# вызов функции form_reg с аргументом message
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Команды: \n/reg - Регистрация\n/button - Кнопки\n')
    else:
        bot.send_message(message.from_user.id, 'Привет 🤖✋\nДля помощи пиши команду: /help')

def form_reg(message):
    bot.send_message(message.from_user.id, "Как тебя зовут?")
    bot.register_next_step_handler(message, get_name )

def get_name(message): 
    """Функция получения имени"""
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname, )

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id,'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    age = message.text
    # Нужно дописать исключение, если пользователь введёт не цифру, а букву!!!
    bot.send_message(message.from_user.id, "Имя: "+name+"\nФамилия: "+surname+"\nВозвраст: "+age)
    # Дальше можно записать данные (name, surname, age) в БД

bot.polling(none_stop=True, interval=0)
