from flask import request, jsonify, render_template
import mysql.connector
from banco import conectar_banco


def registrar_rotas_login(app):
    @app.route("/")
    def login():
        return render_template("login.html")

    @app.route("/api/login", methods=["POST"])
    def fazer_login():
        dados = request.get_json(silent=True)
        if not isinstance(dados, dict):
            return jsonify({"erro": "Informe e-mail e senha."}), 400

        email = dados.get("email", "").strip()
        senha = dados.get("senha", "")
        if not email or not senha:
            return jsonify({"erro": "Informe e-mail e senha."}), 400

        conexao = None
        try:
            conexao = conectar_banco()
            cursor = conexao.cursor(dictionary=True)
            sql = """
                SELECT id, nome, email, senha, ativo
                FROM usuario
                WHERE email = %s
            """
            cursor.execute(sql, (email,))
            usuario = cursor.fetchone()
            cursor.close()

            if not usuario or not usuario["ativo"] or senha != usuario["senha"]:
                return jsonify({
                    "erro": "E-mail ou senha inválidos!"
                }), 401
            return jsonify({
                "mensagem": "Login realizado com sucesso!",
                "usuario": {
                    "id": usuario["id"],
                    "nome": usuario["nome"],
                    "email": usuario["email"]
                }
            }), 200
        except mysql.connector.Error:
            return jsonify({
                "erro": "Não foi possível conectar ao banco de dados."
            }), 503
        finally:
            if conexao is not None and conexao.is_connected():
                conexao.close()

    @app.route("/sistema")
    def sistema():
        return render_template("index.html")
