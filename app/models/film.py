import json

from marshmallow import Schema, fields


class FilmSchema(Schema):
    """Film Schema"""

    title = fields.Str(required=True)
    Year = fields.Str(required=True)
    Rated = fields.Str(required=True)
    Released = fields.Str(required=True)
    Runtime = fields.Str(required=True)
    Genre = fields.Str(required=True)
    Director = fields.Str(required=True)
    Writer = fields.Str(required=True)
    Actors = fields.Str(required=True)
    Plot = fields.Str(required=True)
    Language = fields.Str(required=True)
    Country = fields.Str(required=True)
    Awards = fields.Str(required=True)
    Poster = fields.Str(required=True)
    Metascore = fields.Str(required=True)
    imdbRating = fields.Str(required=True)
    imdbVotes = fields.Str(required=True)
    imdbID = fields.Str(required=True)
    Type = fields.Str(required=True)
    Response = fields.Str(required=True)
    Images = fields.List(fields.Str(required=False))


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
