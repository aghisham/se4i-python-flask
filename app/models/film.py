import json


class Film:
    def __init__(self, title, year, rated):
        self.title = (title,)
        self.year = year
        self.rated = rated

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
