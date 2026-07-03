import mysql.connector

conexao = mysql.connector.connect(
    host="mysql-1d4ea698-crud-teste.f.aivencloud.com",
    port=11712,
    user="avnadmin",
    password="AVNS_YVkVhfC9EsuI9R77hI2",
    database="defaultdb",
    ssl_disabled=False
)

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produto (

    id INT AUTO_INCREMENT PRIMARY KEY,

    nome VARCHAR(100) NOT NULL,

    preco DECIMAL(10,2) NOT NULL,

    estoque INT NOT NULL,

    categoria VARCHAR(50)

)
""")

conexao.commit()

print("Tabela criada com sucesso!")

cursor.close()
conexao.close()