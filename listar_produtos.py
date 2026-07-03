import mysql.connector

conexao = mysql.connector.connect(
    host="mysql-1d4ea698-crud-teste.f.aivencloud.com",
    port=11712,
    user="avnadmin",
    password="AVNS_YVkVhfC9EsuI9R77hI2",
    database="defaultdb",
    ssl_disabled=False
)

cursor = conexao.cursor(dictionary=True)

cursor.execute("SELECT * FROM produto")

produtos = cursor.fetchall()

for produto in produtos:
    print(produto)

cursor.close()
conexao.close()