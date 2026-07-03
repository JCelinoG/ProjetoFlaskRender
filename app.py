from flask import Flask, render_template, request, redirect
from database.conexao import conexao, cursor

app = Flask(__name__)


@app.route("/")
def home():

    cursor.execute("SELECT * FROM produto")
    produtos = cursor.fetchall()

    return render_template("index.html", produtos=produtos)


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

    return redirect("/") 


if __name__ == "__main__":
    app.run(debug=True)