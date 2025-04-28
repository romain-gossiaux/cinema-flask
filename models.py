from . import app, db
from flask_sqlalchemy import SQLAlchemy

class film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    realisateur = db.Column(db.String)
    titre = db.Column(db.String)
    description = db.Column(db.String)
    duree = db.Column(db.Integer)
    date_sortie = db.Column(db.DateTime)
    affiche = db.Column(db.String)

    def __repr__(self):
        return '<film %r>' % self.id

class seance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_film = db.Column(db.Integer, db.ForeignKey('film.id'))
    date_heure = db.Column(db.DateTime)

    def __repr__(self):
        return '<seance %r>' % self.id

class vue_seances_films(db.Model):
    id_seance = db.Column(db.Integer, primary_key=True)
    date_heure = db.Column(db.DateTime)
    id_film = db.Column(db.Integer, db.ForeignKey('film.id'))
    titre = db.Column(db.String)
    duree = db.Column(db.Integer)
    affiche = db.Column(db.String)

    def __repr__(self):
        return '<vue_seances_films %r>' % self.id_seance