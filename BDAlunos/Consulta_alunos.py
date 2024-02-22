import sqlite3

conexao = sqlite3.connect('banco_alunos')
cursor = conexao.cursor()


# Selecionar todos os registros da tabela "alunos". 
dados = cursor.execute ('SELECT * FROM alunos ORDER BY nome,id')
for aluno in dados:
    print(aluno) 


# Selecionar o nome e a idade dos alunos com mais de 20 anos.
dados = cursor.execute ('SELECT nome,idade FROM alunos where idade > 20')
for aluno in dados:
    print(aluno) 


#Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dados = cursor.execute ('SELECT nome,curso FROM alunos where curso = "Engenharia" ORDER BY nome ASC')
for aluno in dados:
    print(aluno) 



# Contar o número total de alunos na tabela
dados = cursor.execute ('SELECT COUNT(*) AS  T_alunos FROM alunos')
for aluno in dados:
    print(aluno) 


