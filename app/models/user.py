import json
from datetime import date, datetime


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
<<<<<<< HEAD
        birthDate = datetime.strptime(self.birthDate.replace("/", "-"), "%d-%m-%Y")
=======
        birth_date = datetime.strptime(self.birth_date.replace("/", "-"), "%d-%m-%Y")
>>>>>>> 5da2c8726fd05c03480cad620d87e1a03b73faf9
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
        data = json.load(open("app/static/users_list.json", mode="r", encoding="utf-8"))
        users_list = data if (len(data)) else []
        users_list.append(
            {
                "id": self.id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "email": self.email,
                "password": self.password,
                "birth_date": self.birth_date,
            }
        )
        with open("app/static/users_list.json", mode="w", encoding="utf-8") as outfile:
            json.dump(users_list, outfile)

    def update(self):
        """Update user

        Returns:
            void
        """
        data = json.load(open("app/static/users_list.json", mode="r", encoding="utf-8"))
        users_list = data if (len(data)) else []
        for user in users_list:
            if user["id"] == self.id:
                user["first_name"] = self.first_name
                user["last_name"] = self.last_name
                user["email"] = self.email
                user["password"] = self.password
                user["birth_date"] = self.birth_date
                with open(
                    "app/static/users_list.json", mode="w", encoding="utf-8"
                ) as outfile:
                    json.dump(users_list, outfile)
                return
        raise Exception("Not existe")
