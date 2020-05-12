# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:15:08 2020

@author: SheilaCarolina
"""
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

dhory = ChatBot("Dhory")

conversa = ["Olá", "Eu sou a Dhory", "Como vai?", "Que legal!", "Posso lhe ajudar?"]

treino = ListTrainer(dhory)
treino.train(conversa)

resposta = dhory.get_response("Oi")
print("Dhory: ", resposta)
