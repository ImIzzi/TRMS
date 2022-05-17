from abc import ABC, abstractmethod


class LoginRepo(ABC):

    @abstractmethod
    def create_login(self, login):
        pass

    @abstractmethod
    def employee_login(self, login):
        pass
