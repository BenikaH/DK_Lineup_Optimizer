import csv
from Player import Player

BASE_PATH = "text/"

def get_all_players(file_path):
    file_path = BASE_PATH + file_path
    players = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == "Position":
                continue
            else:
                players.append(Player(row[1], row[5], row[0], row[2], row[4]))
    return players

def get_all_games(file_path):
    file_path = BASE_PATH + file_path
    games = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == "Position":
                continue
            else:
                game = _game_parser(row[3])
                if game not in games:
                    games.append(game)
    return games


def _game_parser(game_string):
    first_team = game_string.split("@")[0]
    second_team = game_string.split("@")[1].split(" ")[0]
    return (first_team, second_team)