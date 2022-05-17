from exceptions.login_exception import LoginException
from models.login import Login
from repository.login_repo import LoginRepo
from util.db_connection import connection


def build_login(record):
    return Login(id=record[0], username=record[1], password=record[2])


class LoginRepoImpl(LoginRepo):

    def create_login(self, login):
        sql = "INSERT INTO login VALUES(default, %s, %s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (login.username, login.password))
        connection.commit()

    def employee_login(self, login):
        sql = "SELECT * FROM login WHERE username = %s AND password = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (login.username, login.password))
        connection.commit()
        record = cursor.fetchone()
        if record:
            return build_login(record)
        else:
            raise LoginException("Incorrect username or password, try again")
