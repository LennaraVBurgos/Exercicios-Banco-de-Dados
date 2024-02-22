import sqlite3

conexao = sqlite3.connect('banco_cliente')
cursor = conexao.cursor()


# Calcule o saldo médio dos clientes.

dados = cursor.execute ('SELECT AVG(saldo)  AS SD_Media FROM Clientes ')
for cl in dados:
    print(cl)

# Encontre o cliente com o saldo máximo
dados = cursor.execute ('SELECT * FROM Clientes ORDER BY saldo LIMIT 1 ')
for cl in dados:
    print(cl)    


# Conte quantos clientes têm saldo acima de 1000.
dados = cursor.execute ('SELECT COUNT (saldo) FROM Clientes where saldo > 1000 ')
for cl in dados:
    print(cl) 








conexao.commit()
conexao.close