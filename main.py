# ponto de entrada

# pip install Flask
from flask import Flask, render_template
#from flask_admin import Admin

import api.alunoController

app = Flask(__name__)

if __name__ == "__main__":
  app.run(debug=True)