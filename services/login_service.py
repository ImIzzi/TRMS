from repository.login_repo import LoginRepo


class LoginService:

    def __init__(self, login_repo: LoginRepo):
        self.login_repo = login_repo

    def create_login(self, login):
        return self.login_repo.create_login(login)

    def employee_login(self, login):
        return self.login_repo.employee_login(login)

