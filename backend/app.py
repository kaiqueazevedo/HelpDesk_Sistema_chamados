from flask import Flask
from flask_cors import CORS
from database.db import db
from routes.usuario_routes import usuario_bp
from routes.chamado_routes import chamado_bp

app = Flask(__name__)
CORS(app)  # Permite CORS para todas as origens

# Configuração do banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///helpdesk.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Registra Blueprints
app.register_blueprint(usuario_bp)
app.register_blueprint(chamado_bp)

@app.route("/")
def home():
    return {"message": "HelpDesk API rodando"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Cria tabelas
    app.run(debug=True)



app = Flask(__name__)
CORS(app)  # Permite requisições do front

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///helpdesk.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(usuario_bp)
app.register_blueprint(chamado_bp)

@app.route("/")
def home():
    return {"message": "HelpDesk API rodando"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # cria tabelas se não existirem
    app.run(debug=True)