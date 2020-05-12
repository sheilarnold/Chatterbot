# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:29:38 2020

@author: SheilaCarolina
"""
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

dhory = ChatBot("Dhory")

conversa = ["Olá.", "Eu sou a Dhory.", "Como vai?", "Que legal!", "Posso lhe ajudar?", "Muito bem."]

treino = ListTrainer(dhory)
treino.train(conversa)

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
