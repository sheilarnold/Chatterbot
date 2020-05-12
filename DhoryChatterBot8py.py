# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:21:36 2020

@author: SheilaCarolina
"""
from chatterbot.parsing import datetime_parsing
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from googletrans import Translator

bot = ChatBot(
    'Math & Time Bot',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    filters=[filters.get_recent_repeated_responses]
)

#trainer = ChatterBotCorpusTrainer(bot)
#trainer.train("chatterbot.corpus.portuguese")

# Print an example of getting one math based response
response = bot.get_response('Quanto é 4 + 9?')
print(response)

translator = Translator()

# Print an example of getting one time based response
response = bot.get_response('Que horas são?')
print(response)
resposta = bot.get_response('Que horas são?')
imp = translator.translate(str(resposta), src="en", dest="pt")
print(imp.text)

data = datetime_parsing("Hoje é dia 08/05/2020")
print(data)
print(data[0][0])
