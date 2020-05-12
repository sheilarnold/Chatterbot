# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:06:42 2020

@author: SheilaCarolina
"""
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

dhory = ChatBot("Dhory")
trainer = ChatterBotCorpusTrainer(dhory)

trainer.train("chatterbot.corpus.portuguese")

resposta = dhory.get_response("Perfeito")
print("Dhory: ", resposta)