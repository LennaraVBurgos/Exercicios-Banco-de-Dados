import sqlite3

conexao = sqlite3.connect('banco_cliente')
cursor = conexao.cursor()

#  Atualize o saldo de um cliente específico.

cursor.execute ('UPDATE Clientes SET saldo = "20000" where nome="Matt"')




# Remova um cliente pelo seu ID.

cursor.execute ('DELETE FROM Clientes where id = 3')

dados = cursor.execute ('SELECT * FROM Clientes ORDER BY nome,id')
for cl in dados:
    print(cl) 









conexao.commit()
conexao.close