import sqlite3

conexao = sqlite3.connect('banco_cliente')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE Compra_z(id  INTEGER PRIMARY KEY,cliente_id INTEGER,  produtos Varchar(100), valor FLOAT, FOREIGN KEY (cliente_id) REFERENCES Clientes(id));')


#cursor.execute ('INSERT INTO Compra_z (cliente_id, produtos, valor) VALUES (1, "Jeans", 50.99);')
#cursor.execute ('INSERT INTO Compra_z (cliente_id, produtos, valor) VALUES (2, "Copo Hérois", 20.99);')
#cursor.execute ('INSERT INTO Compra_z (cliente_id, produtos, valor) VALUES (3, "Camiseta", 29.00);')
#cursor.execute ('INSERT INTO Compra_z (cliente_id, produtos, valor) VALUES (4, "Kit de pratos", 154.986);')
#cursor.execute ('INSERT INTO Compra_z (cliente_id, produtos, valor) VALUES (5, "Panos de pratos", 10.20);')
#cursor.execute ('INSERT INTO Compra_z (cliente_id, produtos, valor) VALUES (6, "Lampada antiga", 200.15);')
#cursor.execute ('INSERT INTO Compra_z (cliente_id, produtos, valor) VALUES (7, "Espelho", 60.00);')
#cursor.execute ('INSERT INTO Compra_z (cliente_id, produtos, valor) VALUES (8, "Vassoura", 14.99);')
#cursor.execute ('INSERT INTO Compra_z (cliente_id, produtos, valor) VALUES (9, "Geladeira", 7000.99);')




dados = cursor.execute ('SELECT c.nome AS nome_cliente, cm.produtos, cm.valor FROM Compra_z cm JOIN Clientes c ON cm.cliente_id = c.id')
for cl in dados:
    print(cl) 