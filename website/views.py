from flask import Blueprint, render_template
from .ADP import scrape_players_data

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("index.html")

@views.route('/adp.html')
def adp():
    players = scrape_players_data()
    return render_template('adp.html', players=players)