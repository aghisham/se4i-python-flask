from datetime import date, datetime
import json


class User:

    def __init__(self) -> None:
        self.users = []
        data = json.load(open('app/static/users_list.json'))
        if (len(data)):
            self.users = data

    def get_full_name(self, user):
        return "{firstName} {lastName}".format(firstName=user['firstName'], lastName=user['lastName'].upper())

    def get_age(self, user):
        today = date.today()
        birthDate = datetime.strptime(user['birthDate'], '%d-%m-%Y')
        return today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

    def store(self, id, firstName, lastName, email, password, birthDate):
        self.users.append({
            "id": id,
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "password": password,
            "birthDate": birthDate
        })
        with open('app/static/users_list.json', 'w') as outfile:
            json.dump(self.users, outfile)

    def update(self, id, firstName, lastName, email, password, birthDate):
        for user in self.users:
            if user['id'] == id:
                user['firstName'] = firstName
                user['lastName'] = lastName
                user['email'] = email
                user['password'] = password
                user['birthDate'] = birthDate
                with open('app/static/users_list.json', 'w') as outfile:
                    json.dump(self.users, outfile)
                return
        raise Exception("Not existe")
