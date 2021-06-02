import requests
import random

SOURCES = [
    "https://haiku-json-db.herokuapp.com/issa",
    "https://haiku-json-db.herokuapp.com/basho",
    "https://haiku-json-db.herokuapp.com/buson",
]


def get_random():
    url = random.choice(SOURCES)
    r = requests.get(url)
    haikus = r.json()
    return {
        "author": haikus["author"],
        "haiku": random.choice(haikus["haikus"])
    }
