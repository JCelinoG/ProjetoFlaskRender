import mysql.connector

conexao = mysql.connector.connect(

    host="localhost",

    user="root",

    password="root",      

    database="loja"

)

cursor = conexao.cursor()