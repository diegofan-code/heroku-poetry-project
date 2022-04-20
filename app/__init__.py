from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()


class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    comentario = db.Column(db.String(), nullable=False)


def create_app():
    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://nphajkcsngocil:c3569318c79331ebeaddc991aa54de2eac6de0f0871a10ebcc0ab3e76b8d41a3@ec2-44-199-143-43.compute-1.amazonaws.com:5432/d891ht8h9jog3g"
    app.db = db.init_app(app)
    Migrate(app, db)

    @app.route("/")
    def index():
        return render_template(
            'index.html',
             comments = Comentario.query.order_by(
                 Comentario.id
             ).limit(20).all()
                 
        )
    @app.route('/post', methods=['POST'])
    def post():
        form= request.form
        comment = Comentario(
            nome=form['nome'],
            comentario=form['comentario']
        )
        db.session.add(comment)
        db.session.commit()
        
        return redirect('/')

    return app
