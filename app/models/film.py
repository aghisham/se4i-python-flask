from app import app
import json


class Film:
    def __init__(self):
        self.films_list = []
        parsed_films = json.load(open("app/static/users_list.json"))
        if len(parsed_films):
            self.films_list = parsed_films
