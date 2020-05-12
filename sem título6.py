# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:09:43 2020

@author: SheilaCarolina
"""
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import MySQLdb as sql

conexao = sql.connect('localhost', 'root', 'bancodedados')
conexao.select_db('dbdhory')

print(conexao)
dhory = ChatBot("Dhory", storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///database.sqlite3')

trainer = ChatterBotCorpusTrainer(dhory)

trainer.train("chatterbot.corpus.portuguese")
dialogo = {'user': [], 'dhory':[]}

while True:
    try:
        mensagem = input("Você: ")
        dialogo['user'].append(mensagem)
        resposta = dhory.get_response(mensagem)
        if("tchau" in mensagem.lower()):
            print("Dhory: Tchau! Até mais")
            break
        else:
            print("Dhory: ", resposta)
        dialogo['dhory'].append(resposta)
    except(KeyboardInterrupt, EOFError, SystemExit):
        print("Finalizando o sistema.")
        break

conversa = ', '.join(dialogo)

print("Registrando conversa...")
transacoes = conexao.cursor()
transacoes.execute("INSERT INTO `registro_conversas`(`conversa`) VALUES ('{}')".format(dialogo))
conexao.commit()
print("Conversa registrada!")