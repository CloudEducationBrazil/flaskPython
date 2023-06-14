# ponto de entrada

# pip install Flask
from flask import Flask, render_template
#from flask_admin import Admin
import requests as request
import db.conn as conn

app = Flask(__name__)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/autenticar", methods=["GET"])
def autenticar():
   #if request. == "GET":
   if 1 == 1:
       #login = request.form["login"]
       #senha = request.form["senha"]
       
       login = request.get("login")
       senha = request.get("senha")

       dados = {"login":login, "senha":senha}

       print(login)
       error = None

       if not login:
           error = "Login is required."

       if not senha:
           error = "Senha is required."

       if error is not None:
           print(error)
       else:
           print('Conectado com sucesso!!!')
           return "login: {} e senha: {}".format(login, senha)

   #return render_template("index.html")
   return "Usuário não conectado!!!"

@app.route("/")
def homepage():
    return render_template("index.html")

# rota de contato
@app.route("/contato")
def contato():
    return render_template("contato.html")

# rota de usuários
@app.route("/usuarios/<nom_user>,<email_user>")
def usuarios(nom_user, email_user):
    return render_template("/usuarios.html", nom_user_id = nom_user, 
                                             email_user_id = email_user)

@app.route("/aluno/create", methods=["GET", "POST"])
def serviceCreate():
   """Create a new post for the current user."""
   dados = {"matricula":mat, "nome":nom}
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
           return render_template("templates/index.html", mat=mat, nom=nom)

   return render_template("templates/index.html")

if __name__ == "__main__":
  app.run(debug=True)