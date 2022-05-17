from repository.employee_info_repo import EmployeeInfoRepo


class EmployeeInfoService:

    def __init__(self, employee_info_repo: EmployeeInfoRepo):
        self.employee_info_repo = employee_info_repo

    def get_all_employees(self):
        return self.employee_info_repo.get_all_employees()

    def get_employee_info_by_id(self, employee_id):
        return self.employee_info_repo.get_employee_info_by_id(employee_id)

    def create_employee(self, employee_info):
        return self.employee_info_repo.create_employee(employee_info)

    def delete_employee(self, employee_id):
        return self.employee_info_repo.delete_employee(employee_id)
