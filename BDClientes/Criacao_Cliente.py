import sqlite3

conexao = sqlite3.connect('banco_cliente')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE Clientes(id  PK,  nome Varchar(100), idade INT, saldo FLOAT);')

cursor.execute('INSERT INTO Clientes( id,nome, idade, saldo) VALUES ( 6,"Zé", 29, 100.1);')
cursor.execute('INSERT INTO Clientes( id,nome, idade, saldo) VALUES ( 7,"Conceição", 49, 100.1);')
cursor.execute('INSERT INTO Clientes( id,nome, idade, saldo) VALUES ( 8,"Carlos", 69, 100.1);')
cursor.execute('INSERT INTO Clientes( id,nome, idade, saldo) VALUES ( 9,"Eduarda", 39, 100.1);')

dados = cursor.execute ('SELECT * FROM Clientes ORDER BY nome,saldo')
for cl in dados:
    print(cl)


conexao.commit()
conexao.close