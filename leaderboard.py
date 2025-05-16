
import json
import os

LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, "r") as file:
        return json.load(file)

def save_leaderboard(data):
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_score(nickname, score, time_taken):
    leaderboard = load_leaderboard()
    leaderboard.append({"nickname": nickname, "score": score, "time": time_taken})
    leaderboard.sort(key=lambda x: (-x["score"], x["time"]))
    save_leaderboard(leaderboard)

def get_leaderboard():
    return load_leaderboard()
