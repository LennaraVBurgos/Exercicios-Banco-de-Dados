import sqlite3


conexao = sqlite3.connect('banco_alunos')
cursor = conexao.cursor()


cursor.execute('INSERT INTO alunos(id,  nome, idade, curso) VALUES (1 , "Savannah", 21, "Engenharia");')
cursor.execute('INSERT INTO alunos(id,  nome, idade, curso) VALUES (2 , "Tom Erichsen", 25, "Computação");')
cursor.execute('INSERT INTO alunos(id,  nome, idade, curso) VALUES (3 , "Matt", 19, "Engenharia");')
cursor.execute('INSERT INTO alunos(id,  nome, idade, curso) VALUES (4 , "Camilla", 22, "Sistema de Informação");')
cursor.execute('INSERT INTO alunos(id,  nome, idade, curso) VALUES (5 , "Jade", 29, "Engenharia");')



conexao.commit()
conexao.close