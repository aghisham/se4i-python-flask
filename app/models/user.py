from datetime import date, datetime
import json


class User:
    def __init__(self, id, firstName, lastName, email, password, birthDate) -> None:
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.birthDate = birthDate

    def get_full_name(self):
        return "{firstName} {lastName}".format(
            firstName=self.firstName, lastName=self.lastName.upper()
        )

    def get_age(self):
        today = date.today()
        birthDate = datetime.strptime(self.birthDate, "%d-%m-%Y")
        return (today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)))

    def store(self):
        data = json.load(open("app/static/users_list.json"))
        users_list = data if (len(data)) else []
        users_list.append(
            {
                "id": self.id,
                "firstName": self.firstName,
                "lastName": self.lastName,
                "email": self.email,
                "password": self.password,
                "birthDate": self.birthDate,
            }
        )
        with open("app/static/users_list.json", "w") as outfile:
            json.dump(users_list, outfile)

    def update(self):
        data = json.load(open("app/static/users_list.json"))
        users_list = data if (len(data)) else []
        for user in users_list:
            if user["id"] == self.id:
                user["firstName"] = self.firstName
                user["lastName"] = self.lastName
                user["email"] = self.email
                user["password"] = self.password
                user["birthDate"] = self.birthDate
                with open("app/static/users_list.json", "w") as outfile:
                    json.dump(users_list, outfile)
                return
        raise Exception("Not existe")
