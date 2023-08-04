from datetime import date, datetime
from marshmallow import Schema, fields
from app import DB


class DataSchema(Schema):
    """User Schema"""

    id = fields.Int(required=True)
    brand = fields.Str(required=True)
    model = fields.Str(required=True)
    year = fields.Int(required=True)
    des = fields.Str(required=True)
    
class LoginSchema(Schema):
    """User Schema"""
    id = fields.Int(required=True)
    user_name = fields.Str(required=True)
    password = fields.Str(required=True)

class Project_user:
    def __init__(self, dec) -> None:
        self.dec = dec

    def get_dec(self):
        return "{dec}".format(dec=self.dec)

    def home_page(self):
        return self


class Data:
    def __init__(self, id, brand, model, year, des):
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.description = des


class DataStore:
    def __init__(self):
        self.datas = []
        self.next_id = 1

    def create_data(self, id, brand, model, year, des):
        data = Data(self, id, brand, model, year, des)
        self.datas.append(data)
        self.next_id += 1
        return data

    def get_data(self, id):
        for data in self.datas:
            if data.id == id:
                return data
        return None

    def update_data(self):
        DB.datas.update_one(
            {"id": self.id},
            {
                "$set": {
                    "brand": self.brand,
                    "model": self.model,
                    "year": self.year,
                    "des": self.des,
                }
            },
        )

    def delete_data(self, id):
        data = self.get_data(id)
        if data:
            self.datas.remove(data)
            return data
        return None
