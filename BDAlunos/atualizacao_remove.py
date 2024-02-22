import sqlite3

conexao = sqlite3.connect('banco_alunos')
cursor = conexao.cursor()


#Atualize a idade de um aluno específico na tabela.
cursor.execute ('UPDATE alunos SET idade = "26" where nome="Tom Erichsen"')


# Remova um aluno pelo seu ID.
cursor.execute ('DELETE FROM alunos where id = 2')

dados = cursor.execute ('SELECT * FROM alunos ORDER BY nome,id')
for aluno in dados:
    print(aluno) 