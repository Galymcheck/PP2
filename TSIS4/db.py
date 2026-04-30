import json
from datetime import datetime

FILE = "leaderboard.json"


def load():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_score(username, score, level):
    data = load()

    data.append({
        "username": username,
        "score": score,
        "level": level,
        "time": str(datetime.now())[:19]
    })

    data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def get_top10():
    return sorted(load(), key=lambda x: x["score"], reverse=True)[:10]