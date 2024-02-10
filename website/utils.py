# utils.py
import csv
from flask import current_app

def fetch_rookie_data():
    rookies = []

    with open('website/static/data/2024 Prospect Age Database.csv', 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)

        # Print the header row to identify the column names
        header_row = next(csv_reader)
        print("Column names:", header_row)

        for row in csv_reader:
            rookies.append({
                'Player': row['Player'],
                'Position': row['Position'],
                'Final Age': row['Final Age'],
                'School': row['School']
            })

    return rookies