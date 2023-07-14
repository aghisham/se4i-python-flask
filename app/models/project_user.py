import json


class Project_user:
    def __init__(self, dec) -> None:
        self.dec = dec

    def get_dec(self):
        return "{dec}".format(dec=self.dec)

    def home_page(self):
        return self
