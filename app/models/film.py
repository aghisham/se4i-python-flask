import json

from marshmallow import Schema, fields


class Filmschema(Schema):
    """Film Schema"""
        Title: fields.Int(required=True)
        "Year": fields.Int(required=True)
        "Rated": "R",
        "Released": "09 Mar 2007",
        "Runtime": "117 min",
        "Genre": "Action, Drama, Fantasy",
        "Director": "Zack Snyder",
        "Writer": "Zack Snyder (screenplay), Kurt Johnstad (screenplay), Michael Gordon (screenplay), Frank Miller (graphic novel), Lynn Varley (graphic novel)",
        "Actors": "Gerard Butler, Lena Headey, Dominic West, David Wenham",
        "Plot": "King Leonidas of Sparta and a force of 300 men fight the Persians at Thermopylae in 480 B.C.",
        "Language": "English",
        "Country": "USA",
        "Awards": "16 wins & 42 nominations.",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BMjAzNTkzNjcxNl5BMl5BanBnXkFtZTYwNDA4NjE3._V1_SX300.jpg",
        "Metascore": "52",
        "imdbRating": "7.7",
        "imdbVotes": "611,046",
        "imdbID": "tt0416449",
        "Type": "movie",
        "Response": "True",
        "Images": [
            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMwNTg5MzMwMV5BMl5BanBnXkFtZTcwMzA2NTIyMw@@._V1_SX1777_CR0,0,1777,937_AL_.jpg",
            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQwNTgyNTMzNF5BMl5BanBnXkFtZTcwNDA2NTIyMw@@._V1_SX1777_CR0,0,1777,935_AL_.jpg",
            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc0MjQzOTEwMV5BMl5BanBnXkFtZTcwMzE2NTIyMw@@._V1_SX1777_CR0,0,1777,947_AL_.jpg"
        ]



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
