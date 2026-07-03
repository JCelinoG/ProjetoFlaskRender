from flask import Flask, render_template, request
from database.conexao import conexao, cursor

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/cadastro")
def cadastro():

    return render_template("cadastro_produto.html")


@app.route("/salvar", methods=["POST"])
def salvar():

    nome = request.form["nome"]
    preco = request.form["preco"]
    estoque = request.form["estoque"]
    categoria = request.form["categoria"]

    sql = """
    INSERT INTO produto(nome, preco, estoque, categoria)
    VALUES (%s,%s,%s,%s)
    """

    valores = (nome, preco, estoque, categoria)

    cursor.execute(sql, valores)

    conexao.commit()

    return render_template(
        "sucesso.html",
        nome=nome
    )


if __name__ == "__main__":

    app.run(debug=True)