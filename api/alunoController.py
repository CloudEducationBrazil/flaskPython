# são as routes
# ponto de entrada

# pip install Flask
from flask import Flask, render_template
#from flask_admin import Admin

rotas = Flask(__name__)

# 1. routes (endpoint = URL)
# ex.: https://casasbahia.com/contato
# 2. function executa uma solicitação do route
# 3. templates (design da tela solicitada)

# rota da página principal
# home page = domínio do site
# ex.: / == https://casasbahia.com
# Rodando local = http://127.0.0.1:5000/
# Rodando local = localhost:5000/
# Criar arquivo Procfile com o conteúdo: # web: gunicorn projectTeste:app
# 
#  # depois de instalado gunicorn

# 1. Criar o projeto no VsCode
# 2. Integrar com o Github
# 3. Criar/Login Netlify
# 4. Criar site e importar projeto do Github
# 5. Selecionar o projeto e vai realizar o deploy

import requests as request
import entities.AlunoClass as aluno
import db.conn as conn

@rotas.route("/")
def homepage():
    return render_template("index.html")

# rota de contato
@rotas.route("/contato")
def contato():
    return render_template("contato.html")

# rota de usuários
@rotas.route("/usuarios/<nom_user>,<email_user>")
def usuarios(nom_user, email_user):
    return render_template("/usuarios.html", nom_user_id = nom_user, 
                                             email_user_id = email_user)

@rotas.route("/aluno/create", methods=("GET", "POST"))
def serviceCreate():
   """Create a new post for the current user."""
   if request.method == "POST":
       mat = request.form["mat"]
       nom = request.form["nom"]

       print(mat)
       error = None

       if not mat:
           error = "Mat is required."

       if not nom:
           error = "Nom is required."

       if error is not None:
           print(error)
       else:
           db = conn #get_db()
           db.execute(
               "INSERT INTO aluno (mat, nom) VALUES (?, ?, ?)",
               (mat, nom),
               #(mat, nom, g.user["id"]),
           )
           db.commit()
           #return redirect(url_for("templates.index"))
           return render_template("templates/index.html")

   return render_template("templates/index.html")

if __name__ == "__main__":
  rotas.run(debug=True)