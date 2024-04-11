from flask import Blueprint, render_template, request
from flask_paginate import Pagination
from .ADP import scrape_players_data
from .utils import *

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("index.html")

@views.route('/adp.html')
def adp():
    page = request.args.get('page', 1, type=int)  # Get the requested page from the URL query parameter
    per_page = request.args.get('per_page', 20, type=int)  # Get per_page from URL query parameter

    # Fetch all players data
    all_players = scrape_players_data()

    # Calculate the start and end indices for the current page
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page

    # Get the subset of players for the current page
    players_subset = all_players[start_idx:end_idx]

    # Create a Pagination object for the players data
    pagination = Pagination(page=page, per_page=per_page, total=len(all_players), max_items=2)

    return render_template('adp.html', players=players_subset, pagination=pagination, per_page=per_page)

@views.route('/rookie-rankings.html')
def rookieRankings():
    rookies = fetch_rookie_data()
    return render_template("rookie-rankings.html", rookies=rookies)

@views.route('/league-data.html')
def league_data():
    return render_template("league-data.html")

@views.route('/bankroll-tracker.html')
def bankroll_tracker():
    return render_template("bankroll-tracker.html")

