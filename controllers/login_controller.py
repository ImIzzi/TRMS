from models.login import Login
from repository.login_repo_impl import LoginRepoImpl
from services.login_service import LoginService
from flask import request
from exceptions.login_exception import LoginException


def build_login(record):
    return Login(id=record[0], username=record[1], password=record[2])


lr = LoginRepoImpl()
ls = LoginService(lr)


def run(app):

    @app.route("/home/register", methods=["POST"])
    def post_login():
        body = request.json

        login = Login(username=body["username"], password=body["password"])
        login = ls.create_login(login)
        return login.json(), 200

    @app.route("/login", methods=["POST"])
    def employee_login():
        body = request.json

        login = Login(username=body["username"], password=body["password"])
        login = ls.employee_login(login)
        try:
            return login.json, 200
        except LoginException as r:
            return r.message, 404

        # try:
        #     return login.json(), 200
        # except ValueError as e:
        #     return "Not a valid ID", 400
        # except LoginException as r:
        #     return r.message, 404

        # try:
        #     return ls.employee_login(login), 200
        # except TypeError:
        #     return "Username or Password is incorrect, please try again", 404
