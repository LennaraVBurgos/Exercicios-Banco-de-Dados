import sqlite3


conexao = sqlite3.connect('banco_alunos')
cursor = conexao.cursor()


cursor.execute('CREATE TABLE alunos(id  INT,  nome Varchar(100), idade INT, curso Varchar(100));')



conexao.commit()
conexao.close