# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 23:14:21 2020

@author: SheilaCarolina
"""
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import MySQLdb as sql

conexao = sql.connect('localhost', 'root', 'bancodedados')
conexao.select_db('dbdhory')

#transacoes = conexao.cursor()

#transacoes.execute("INSERT INTO `conversas`(`conteudo`) VALUES ('Bora!!')")
#conexao.commit()

#transacoes.execute("SELECT `conteudo` FROM `conversas`")
#row = transacoes.fetchall()
#
#print('\n', row, '\n')

print(conexao)
#print(transacoes)
dhory = ChatBot("Dhory", storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///database.sqlite3')

conversa = ["Olá.", "Eu sou a Dhory.", "Como vai?", "Que legal!", "Posso lhe ajudar?", "Muito bem."]

treino = ListTrainer(dhory)
treino.train(conversa)

dialogo = []

while True:
    try:
        mensagem = input("Você: ")
        resposta = dhory.get_response(mensagem)
        if("tchau" in mensagem.lower()):
            print("Dhory: Tchau! Até mais")
            break
        else:
            print("Dhory: ", resposta)
        dialogo.append(mensagem)
    except(KeyboardInterrupt, EOFError, SystemExit):
        print("Finalizando o sistema.")
        break

print("Registrando conversa...")
transacoes = conexao.cursor()
for i in range(len(dialogo)):
    transacoes.execute("INSERT INTO `conversas`(`conteudo`) VALUES ('{}')".format(dialogo[i]))
    conexao.commit()
print("Conversa registrada!")

