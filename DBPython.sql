create database if not exists cantina;
use cantina;

#create schema DBPython;

create table if not exists turma (
idTurma int auto_increment not null,
horario time,
nomeTurma varchar (30),
primary key (idTurma)
);

create table if not exists sala(
idSala int not null auto_increment,
idTurma int not null,
nome varchar(15),
hora_interv time,
primary key (idSala),
foreign key (idTurma) references turma(idTurma)
);

create table if not exists pessoa(
idPessoa int not null auto_increment,
nome varchar(50),
cpf int, 
datanasc date,
rg int,
primary key (idPessoa)
);

create table if not exists administrador(
idAdmin int not null auto_increment,
idPessoa int,
nome varchar(50),
cpf int, 
datanasc date,
rg int,
cargo varchar (20),
nummatri int,
primary key (idAdmin),
foreign key (idPessoa) references pessoa (idPessoa)
);

create table if not exists aluno (
idAluno int auto_increment not null,
idTurma int,
idPessoa int,
nome varchar (30),
turma varchar (20),
cpf int, 
datanasc date,
rg int,
nummatri int,
primary key (idAluno),
foreign key (idTurma) references turma(idTurma),
foreign key (idPessoa) references pessoa (idPessoa)
);

create table if not exists atendente(
idAtendente int not null auto_increment,
idPessoa int,
nome varchar(50),
cpf int, 
datanasc date,
rg int,
primary key (idAtendente),
foreign key (idPessoa) references pessoa (idPessoa)
);
 
 create table if not exists pedido (
idPedido int auto_increment not null,
horario time,
numPedido varchar (15),
#peca varchar (25),
#casadinha varchar (25),
#suco varchar (25),
primary key (idPedido)
);
        
create table if not exists produto (
idProduto int auto_increment not null,
idPedido int,
nomeProduto varchar (15),
preço varchar (25),
primary key (idProduto),
foreign key (idPedido) references pedido(idPedido)
);

create table if not exists lucro (
IdLucro int auto_increment not null,
idPedido int,
valLucro varchar (25),
primary key (idLucro),
foreign key (idPedido) references pedido(idPedido)	
);

create table if not exists dados (
idBanco int auto_increment,
idPedido int,
primary key (idBanco),
foreign key (idPedido) references pedido(idPedido)
); 

alter table aluno add natanasc date