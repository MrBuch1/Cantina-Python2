from datetime import datetime

import MySQLdb

con = MySQLdb.connect('localhost', 'root', '')
con.select_db('cantina')

cursor = con.cursor()


class time:
    #pra que essa classe? o horário só é necessário na classe principal para limitar o horário e
    #cadastrar o pedido
    def imprimeTime(self):

        now = datetime.now()
        print(now.hour, ":", now.minute)
        print(now.day, "/", now.month, "/", now.year)

    def barrarhorario(self):
        now = datetime.now()
        if now.hour < 20 and now.minute == 0:
            print("Espere a hora do intervalo.")

        elif now.hour >= 20 and now.minute > 45:
            print("Já acabou o intervalo")

    def barrarhorario1(self):
        now = datetime.now()
        if now.hour < 20 and now.minute == 0:
            print("Espere a hora do intervalo.")

        elif now.hour >= 20 and now.minute > 45:
            print("Já acabou o intervalo")



class login:
    def __init__(self, usuario):

        self.__login = usuario

        user = input("Insira seu rg: \n")
        cursor.execute('insert into pessoa (rg) values ("%s")' % (user))
        con.commit()


class Pessoa:

    def __init__(self, nome, cpf, datanasc, rg):

        self.__Nome = nome
        self.__CPF = cpf
        self.__Datanasc = datanasc
        self.__RG = rg


class Administrador(Pessoa):

    def __init__(self, nome, cpf, datanasc, rg, car, numma):

        super().__init__(nome, cpf, datanasc, rg)
        self.__Cargo = car
        self.__nAdmin = numma

    def cadastraAluno(self):
        #SQL de cadastro
        aluno1 = input("Digite o nome do aluno: \n")
        tur1 = input("Digite a turma do aluno: \n")
        cpf1 = input("Digite o cpf do aluno: \n")
        nasc1 = input("Digite a data de nascimento do aluno: \n")
        rg1 = input("Digite o rg do aluno: \n")
        numma1 = input("Digite o número de matrícula do aluno: \n")
        #sala1 = input("Digite a sala do aluno: \n")
        cursor.execute(
            'insert into aluno (nome, turma, cpf, datanasc, rg, nummatri) values ("%s", "%s", "%s", "%s", "%s", "%s")' %
            (aluno1, tur1, cpf1, nasc1, rg1, numma1))
        con.commit()
        condicao1 = input("Deseja cadastrar outro aluno? Digite 's' para SIM ou 'n' para NÃO \n")
        if condicao1 == "s":
            while (condicao1 == "s"):
                aluno1 = input("Digite o nome do aluno: \n")
                tur1 = input("Digite a turma do aluno: \n")
                cpf1 = input("Digite o cpf do aluno: \n")
                nasc1 = input("Digite a data de nascimento do aluno: \n")
                rg1 = input("Digite o rg do aluno: \n")
                numma1 = input("Digite o número de matrícula do aluno: \n")
                # sala1 = input("Digite a sala do aluno: \n")
                cursor.execute(
                    'insert into aluno (nome, turma, cpf, datanasc, rg, nummatri) values ("%s", "%s", "%s", "%s", "%s", "%s")' %
                    (aluno1, tur1, cpf1, nasc1, rg1, numma1))
                con.commit()
                #condicao1 = input("Deseja cadastrar outro aluno? Digite 's' para SIM ou 'n' para NÃO \n")

        elif condicao1 == 'n':
            print("Alunos cadastrados com sucesso.")

       #nome = input("Insira o nome do aluno:\n")
       #cpf = input("Insira o CPF do aluno:\n")
       #nasc = input("Insira a data de nascimento do aluno:\n")
       #rg = input("Insira o RG do aluno:\n")
       #numma = input("Insira o número de matríucula do aluno:\n")
       #turma = input("Insira a turma do aluno:\n")
       ##sala = input("Insira a sala do aluno:\n")
       #cursor.execute('insert into aluno (nome, turma, cpf, datanasc, rg, nummatri) values ("%s", "%s", "%s", "%s", "%s", "%s")' % (nome, turma, cpf, nasc, rg, numma))
       #con.commit()

    def cadastraTurma(self):
        #SQL de cadastro de turma
        #aqui talvez na Tabela turma tenha a sala
        turma1 = input("Digite a turma que deseja cadastrar: \n")
        horario1 = input("Digite o horário de intervalo da turma: \n")
        cursor.execute('insert into turma (nomeTurma, horario) values ("%s", "%s")' % (turma1, horario1))
        con.commit()
        condicao = input("Deseja cadastrar outra turma? Digite 's' para SIM ou 'n' para NÃO \n")
        if condicao == "s":
            while (condicao == "s"):
                turma1 = input("Digite a turma que deseja cadastrar: \n")
                horario1 = input("Digite o horário de intervalo da turma: \n")
                cursor.execute('insert into turma (nomeTurma, horario) values ("%s", "%s")' % (turma1, horario1))
                con.commit()

        elif condicao == 'n':
            print("Turmas cadastradas com sucesso.")

    def cadastraSala(self):
        #SQL de cadastro de sala
        #Aqui talvez na tabela sala tenha o horário de intervalo
        sala1 = input("Digite a sala que deseja cadastrar: \n")
        horario2 = input("Digite o horário de intevalo da sala: \n")
        cursor.execute('insert into sala (nome, hora_interv) values ("%s", "%s")' % (sala1, horario2))
        con.commit()
        condicao = input("Deseja cadastrar outra sala? Digite 's' para SIM ou 'n' para NÃO \n")
        if condicao == "s":
            while (condicao == "s"):
                sala1 = input("Digite a sala que deseja cadastrar: \n")
                horario2 = input("Digite o horário de intervalo da sala: \n")
                cursor.execute('insert into sala (nome, hora_interv) values ("%s", "%s")' % (sala1, horario2))
                con.commit()

        elif condicao == 'n':
            print("Salas cadastradas com sucesso.")


class pedido:



    def __init__(self, numpedido, valorpedido, produto):

        self.__numero = numpedido
        self.__valor = valorpedido
        self.__produto = produto

class Produto:

    def __init__(self, produto, valor, nome, codigo):

        self.__produto = produto
        self.__valor = valor
        self.__nomeProd = nome
        self.__codigo = codigo

    def cadasProduto (self, produto, valor, nome, codigo):

        self.__produto = produto
        self.__valor = valor
        self.__nomeProd = nome
        self.__codigo = codigo

    def produto(self, produto):

        self.__produto = produto

    def valor(self, valor):

        self.__valor = valor

    def nome(self, nome):

        self.__nome = nome

    def codigo(self, codigo):

        self.__codigo = codigo

    def mostrarProduto (self):

         print("Código do produto: " +str (self.__produto)
            + "O valor do produto é: " +str (self.__valor)
            + "O nome do produto é: " +str (self.__nomeProd)
            + "O seu produto é : " +str (self.__codigo))

class Atendente (Pessoa):

    def __init__(self, nome, cpf, datanasc, rg):

        super().__init__(nome, cpf, datanasc, rg)


   #def cadasProduto (self, cadasProduto, produto):
   #    produto.Produto(cadasProduto)

   #def cadasProd (self, prod):
   #    self.__prod = prod

    def cadastraProduto(self):

        produto1 = input("Digite o produto: \n")
        preço1 = input("Digite o valor do produto: \n")
        cursor.execute('insert into produto (nomeProduto, preço) values ("%s", "%s")' % (produto1, preço1))
        con.commit()
        condicao = input("Deseja cadastrar outro produto? Digite 's' para SIM ou 'n' para NÃO \n")
        if condicao == "s":
            while (condicao == "s"):
                produto1 = input("Digite o produto: \n")
                preço1 = input("Digite o valor do produto: \n")
                condicao = input("Deseja cadastrar outro produto? Digite 's' para SIM ou 'n' para NÃO \n")
                cursor.execute('insert into produto (nomeProduto, preço) values ("%s", "%s")' % (produto1, preço1))
                con.commit()

        elif condicao == 'n':
            print("Produtos cadastrados com sucesso.")



        #cursor.execute('insert into produto (preço, nomeProduto) values ("%s", "%s")' % (produto2, preço1))
        #cursor.execute('insert into produto (preço, nomeProduto) values ("%s", "%s")' % (produto3, preço1))
        #cursor.execute('insert into produto (preço, nomeProduto) values ("%s", "%s")' % (produto4, preço2))
        #cursor.execute('insert into produto (preço, nomeProduto) values ("%s", "%s")' % (produto5, preço2))
        #cursor.execute('insert into produto (preço, nomeProduto) values ("%s", "%s")' % (produto6, preço3))
        con.commit()

    def verLucro(self, lucro):

        self.__lucro = lucro




class Aluno(Pessoa):

    def __init__(self, nome, cpf, datanasc, rg, numma, tur, sala):

        super().__init__(nome, cpf, datanasc, rg)

    #def __init__(self, numma, tur, sala):

     #   self.__nAluno = numma
      #  self.__turma = tur
       # self.__sala = sala
    def entrada(self):
        logintur = input("Digite sua turma: \n")
        loginsala = input("Digite a sua sala: \n")
        #if loginsala == "chp54125":





    def pedido(self):

        #self.__pedido = pedido
        #now = datetime.now()
        #hora = now.hour
        inserir = int(input("O que você quer comer?"
                        "\n 1 - Peça R$2,50"
                        "\n 2 - Suco R$2,50"
                        "\n 3 - Casadinha R$2,50\n"))

        if inserir == 1:
            preço1 = str("R$2,50")
            escolher1 = int(input("Escolha uma opção:"
                            "\n1 - Pastel"
                            "\n2 - Coxinha"
                            "\n3 - Enroladinho \n"))

            if escolher1 == 1:
                print("pegue seu Pastel")
                escolher1 = str("Pastel")

            elif escolher1 == 2:
                print("pegue sua Coxinha")
                escolher1 = str("Coxinha")

            elif escolher1 == 3:
                print("pegue seu Enroladinho")
                escolher1 = str("Enroladinho")

            cursor.execute('insert into pedido (numPedido, nomePedido, valorPedido) values ("%s", "%s", "%s")' %
                           (inserir, escolher1, preço1))
            con.commit()


        elif inserir == 2:
            preço2 = str("R$1,50")
            escolher2 = int(input("Escolha uma opção:"
                            "\n1 - Goiaba"
                            "\n2 - Manga \n"))

            if escolher2 == 1:
                print("pegue seu suco de Goiaba")
                escolher2 = str("Suco de Goiaba")

            elif escolher2 == 2:
                print("pegue seu suco de Manga")
                escolher2 = str("Suco de Manga")

            cursor.execute('insert into pedido (numPedido, nomePedido, valorPedido) values ("%s", "%s", "%s")' %
                           (inserir, escolher2, preço2))
            con.commit()


        elif inserir == 3:
            preço3 = str("R$4,00")
            escolher3 = str("Casadinha")
            #casadinha = print("Pegue o lanche e o suco de sua preferência na cantina.")

            cursor.execute('insert into pedido (numPedido, nomePedido, valorPedido) values ("%s", "%s", "%s")' %
                       (inserir, escolher3, preço3))
            con.commit()



    #def verCardapio(self):

        #self.__cardapio = pedido


class sala:

   def __init__(self, nome, horaintervalo, turma):

       self.__nome = nome
       self.__horaint = horaintervalo
       self.__turma = turma

   def criarsala(self, numero, horaintervalo):

        self.__numsala = numero
        self.__horaint = horaintervalo




"""" class administrador:

  def __init__(self, cadastAluno, cadastSala, cadastTurma, cadastHorario):
      self.__aluno = cadastAluno
      self.__sala = cadastSala
      self.__turma = cadastTurma
      self.__horario = cadastHorario

  def horario(self):
      from datetime import datetime
      now = datetime.now()
      print(now.hour, ":", now.minute)

  def cadastroA(self, aluno):
      self.__aluno = aluno

  def cadastroS(self, sala):
      self.__sala = sala
      print(now.day, "/", now.month, "/", now.year),

  def cadastroT(self, turma):
      self.__turma = turma

  def cadastroH(self, horario):
      self.__horario = horario """


