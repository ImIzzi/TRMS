from abc import ABC, abstractmethod


class EmployeeInfoRepo(ABC):

    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def get_employee_info_by_id(self, employee_id):
        pass

    @abstractmethod
    def create_employee(self, employee_info):
        pass

    @abstractmethod
    def delete_employee(self, employee_id):
        pass





