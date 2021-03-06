create database if not exists cantina;
use cantina;
 
#create schema DBPython;
 
create table if not exists turma (
idTurma int auto_increment not null,
nomeTurma varchar(30),
horario time,
primary key (idTurma)
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
cpf int (20), 
datanasc varchar (50),
rg int (20),
nummatri int,
primary key (idAluno),
foreign key (idTurma) references turma(idTurma),
foreign key (idPessoa) references pessoa (idPessoa)
);
 
create table if not exists sala(
idSala int not null auto_increment,
idTurma int not null,
nome varchar(15),
hora_interv time,
primary key (idSala)
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
nomePedido varchar (50),
valorPedido float (3),
#peca varchar (25),
#casadinha varchar (25),
#suco varchar (25),
primary key (idPedido)
);

create table if not exists produto (
idProduto int auto_increment not null,
nomeProduto varchar (50),
preço varchar (25),
primary key (idProduto)
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

create table if not exists login(
log int not null auto_increment,
adm int,
atend int,
aluno int,
primary key (log)
);

insert into login (atend) values ("0987654321")