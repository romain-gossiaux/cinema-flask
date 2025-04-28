from flask import render_template, request
from sqlalchemy import text
from . import app, models, db

@app.context_processor
def inject_request():
    return dict(request=request)

@app.route('/')

@app.route('/accueil')
def accueil():
    result_get_next_seance = db.session.execute(text("SELECT * FROM get_next_seance();"))
    next_seance = result_get_next_seance.fetchone()
    result_get_films_a_l_affiche = db.session.execute(text("SELECT * FROM get_films_a_l_affiche(3);"))
    films_a_l_affiche = result_get_films_a_l_affiche.fetchall()
    return render_template('accueil.html', title='Accueil', next_seance = next_seance, films_a_l_affiche = films_a_l_affiche)

@app.route('/films')
def films():
    liste_films = models.film.query.all()
    return render_template('films.html', title='Films', liste_films = liste_films)

@app.route('/seances')
def seances():
    liste_seances = models.vue_seances_films.query.all()
    return render_template('seances.html', title='Seances', liste_seances = liste_seances)