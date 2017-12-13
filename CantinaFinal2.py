from Avaliação2.CantinaFinal1 import time, Pessoa, Administrador, Produto, Atendente, Aluno
import MySQLdb

#aqui talvez tenha a parte principal do teu programa, onde o usuário vai fazer um "login" e o sistema saberá
#se ele é adm, tia da cantina ou aluno e a depender do que seja, o fluxo do programa sera diferente
admin = Administrador("Lucas", "123456", "123456", "123456", "administrador", "654321")
Administrador.cadastraAluno()