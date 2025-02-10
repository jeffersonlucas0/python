import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Mysql102030",
    "database": "concessionaria"
}

conexao = mysql.connector.connect(**db_config)
janelinha = conexao.cursor()
janelinha.execute("SELECT * FROM Veiculos")
lista_de_carros = janelinha.fetchall()
janelinha.close()
conexao.close()

print(lista_de_carros)

for carro_da_vez in lista_de_carros:
    print(f"""
    ID: {carro_da_vez[0]}
    Marca: {carro_da_vez[1]}
    Modelo: {carro_da_vez[2]}
    """)