import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="mysql-1d4ea698-crud-teste.f.aivencloud.com",
        port=11712,
        user="avnadmin",
        password="AVNS_YVkVhfC9EsuI9R77hI2",
        database="defaultdb",
        ssl_disabled=False
    )

    print("Conectado com sucesso!")

    cursor = conexao.cursor()

    cursor.execute("SELECT VERSION();")

    print(cursor.fetchone())

except Exception as erro:
    print(erro)