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

@views.route('/expert-rankings.html')
def expertRankings():
    return render_template("expert-rankings.html")

@views.route('/league-data.html')
def league_data():
    return render_template("league-data.html")

@views.route('/stats.html')
def stats():
    return render_template("stats.html")

@views.route('/account.html')
def account():
    return render_template("account.html")