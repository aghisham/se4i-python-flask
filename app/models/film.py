import json

from marshmallow import Schema, fields


class FilmSchema(Schema):
    """Film Schema"""

    title = fields.Str(required=True)
    year = fields.Str(required=True)


class Film:
    def __init__(self, title, year, rated):
        self.title = (title,)
        self.year = year
        self.rated = rated
        self.films_list = []

    def add_film(self):
        films_list = []
        parsed_films = json.load(open("app/static/users_list.json"))
        if len(parsed_films):
            films_list = parsed_films

        self.films_list.append(
            {"Title": self.title, "Year": self.year, "Rated": self.rated}
        )

        json.dump(
            films_list,
            json.load(open("app/static/users_list.json")),
            indent=4,
            separators=(",", ": "),
        )
