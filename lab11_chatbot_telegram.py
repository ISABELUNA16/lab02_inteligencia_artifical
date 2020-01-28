import time
import telepot
import httplib2
import json
import html2text
from telepot.loop import MessageLoop


BOTKEY = "1082283705:AAFWGYLA8Xq1bT-aaiBZDid5JnNKv_W_Uwk"
bot = telepot.Bot(BOTKEY)


def getChuckNorrisQuote():
    ICNDB ="http://api.icndb.com/jokes/random"
    resp, content = httplib2.Http().request(ICNDB)
    parsed_content = json.loads(content)
    joke = "\n\n** Chiste Random de Chuck Norris **:\n" + html2text.html2text(parsed_content['value']['joke'])
    return joke


def getNumberTrivia():
    NUMDB = "http://numbersapi.com/random/trivia?json"
    resp, content = httplib2.Http().request(NUMDB)
    parsed_content = json.loads(content)
    trivia = "\n\n** Curiosidad del Numero " + str(parsed_content['number']) + "**\n"
    trivia = trivia + parsed_content['text']
    return trivia


def botSupervisor(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        MENSAJE = msg['text']
        if MENSAJE == "/start":
            bot.sendMessage(chat_id,"Bienvenido a Joker 504mmm Bot utiliza los sigientes comandos: \n/chucknorris\n/numbertrivia")
        elif MENSAJE == "/chucknorris":
            joke = getChuckNorrisQuote()
            bot.sendMessage(chat_id, joke)
        elif MENSAJE == "/numbertrivia":
            trivia = getNumberTrivia()
            bot.sendMessage(chat_id, trivia)
        else:
            bot.sendMessage(chat_id, "No entiendo lo que pides")

# PROGRAMA PRINCIPAL
try:
    MessageLoop(bot, botSupervisor).run_as_thread()
    while True:
       time.sleep(10)

except KeyboardInterrupt:
    print("Proceso cancelado por el Usuario")
except SystemExit:
    print("Error al iniciar el proceso")







