# -*- coding: utf-8 -*-
"""
Created on Thu May  7 21:45:30 2020

@author: SheilaCarolina
"""
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

dhory = ChatBot("Dhory")
trainer = ChatterBotCorpusTrainer(dhory)

trainer.train("chatterbot.corpus.portuguese")

while True:
    try:
        mensagem = input("Você: ")
        resposta = dhory.get_response(mensagem)
        print("Dhory: ", resposta)
        if(mensagem.lower() == "tchau"):
            print("Dhory: Tchau! Até mais")
            break
    except(KeyboardInterrupt, EOFError, SystemExit):
        print("Finalizando o sistema.")
        break

