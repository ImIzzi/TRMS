

class Login:

    def __init__(self, id=0, username="", password=""):
        self.id = id
        self.username = username
        self.password = password

    def json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password
        }

    @staticmethod
    def json_parse(json):
        login = Login()
        login.id = json["id"] if "id" in json else 0
        login.username = json["username"]
        login.password = json["password"]
        return login

    def __repr__(self):
        return str(self.json())
