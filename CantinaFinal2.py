from Avaliação2.CantinaFinal1 import time, Pessoa, Administrador, Produto, Atendente, Aluno, pedido
import MySQLdb

#aqui talvez tenha a parte principal do teu programa, onde o usuário vai fazer um "login" e o sistema saberá
#se ele é adm, tia da cantina ou aluno e a depender do que seja, o fluxo do programa sera diferente
admin = Administrador("Lucas", "123456", "123456", "123456", "administrador", "654321")
atend = Atendente("Maria", "102938", "15/08/1987", "123567")
alu = Aluno ("Tininzinho", "234516", "31/07/1999", "087965", "123456", "51175", "Cisco")

alu.verCardapio(alu.pedido())
#atend.cadastraProduto()
