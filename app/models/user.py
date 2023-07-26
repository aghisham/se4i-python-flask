from datetime import date, datetime
from marshmallow import Schema, fields
from app import DB


class DefaultFileResponseSchema(Schema):
    """Default File Response Schema"""

    message = fields.Str()
    path = fields.Str()


class DefaultResponseSchema(Schema):
    """Default Response Schema"""

    message = fields.Str()


class UserSchema(Schema):
    """User Schema"""

    id = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Str()
    password = fields.Str()
    birth_date = fields.Str()


# pylint: disable=C0103
class User:
    """User Class"""

    def __init__(self, id, first_name, last_name, email, password, birth_date) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.birth_date = birth_date

    def get_full_name(self):
        """Get user full name

        Returns:
            str: full name
        """
        return f"{self.first_name} {self.last_name.upper()}"

    def get_age(self):
        """Get user age

        Returns:
            int: age
        """
        today = date.today()
        birth_date = datetime.strptime(self.birth_date.replace("/", "-"), "%d-%m-%Y")
        return (
            today.year
            - birth_date.year
            - ((today.month, today.day) < (birth_date.month, birth_date.day))
        )

    def store(self):
        """Add new user

        Returns:
            void
        """
        DB.users.insert_one(
            {
                "id": self.id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "email": self.email,
                "password": self.password,
                "birth_date": self.birth_date,
            }
        )

    def update(self):
        """Update user

        Returns:
            void
        """
        DB.users.update_one(
            {"id": self.id},
            {
                "$set": {
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "email": self.email,
                    "password": self.password,
                    "birth_date": self.birth_date,
                }
            },
        )
