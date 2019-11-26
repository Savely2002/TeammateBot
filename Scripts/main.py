import telebot;
import types;
import requests;
bot = telebot.TeleBot('907919216:AAFBqAB3aUgIoFoSWbX_DjKBa5-Fv9eos30')
class Profile:
    SteamId = ''
    DiscordId = ''
    MainInf = ''
    Games = ''
    Hours = ''
Profile_key = ''
stopFinding_key = ''
checkMessages_key = ''
Help_key = ''
startFinding_key = ''
@bot.message_handler(commands = ['start'])
def raiseQuestion(message):
    keyboardFinction = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboardFinction.row('1', '2', '3')
    keyboardFinction.row('4', '5')
    bot.send_message(message.chat.id, '1 - Изменить свой профиль,2 - остановить поиcк, 3 - проверить личные сообщения,4 - Тех.поддержка,5-Искать тиммейтов')
    bot.send_message(message.chat.id, 'Что вы хотите сделать?', reply_markup=keyboardFinction)
    bot.register_next_step_handler(message, botOptions)
@bot.message_handler(content_types=['text'])
def botOptions(message):
    if message.text == '1':
        bot.register_next_step_handler(message, letContactFunc(message))
    else :
        bot.register_next_step_handler(HelpFunc(message))
def letContactSteam(message):
    bot.send_message(message.chat.id, 'Начинаем регистрацию...')
    bot.send_message(message.chat.id, 'Есть ли у вас Steam?(Да/Нет)')
    if message.text == 'Да':
        bot.send_message(message.chat.id, 'напиши ссылку Steam')
        Profile.SteamId = message.text
    else:
        bot.send_message(message.chat.id, 'ну как так')
    bot.register_next_step_handler(letContactDiscord(message))
def letContactDiscord(message):
    bot.send_message(message.chat.id, 'Есть ли у вас Discord?(Да/Нет)')
    if message.text == 'Да':
        bot.send_message(message.chat.id, 'Ваш DiscordId (qwerty#0000)')
        Profile.DiscordId = message.text
    else:
        bot.send_message(message.chat.id, 'а как же общение')
def startFindingFunc(message):
    fds = 0
def HelpFunc(message):
    bot.send_message(message.chat.id, 'напишите вашу проблему,желание')
    abc = message.text
    bot.send_message(message.chat.id, text=abc)
    bot.register_next_step_handler(message, raiseQuestion)
def checkMessagesFunc(message):
    dfd = 0
def stopFindingFunc(message):
    wferg = 0
bot.polling(none_stop=True, interval=0)
