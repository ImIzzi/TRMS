from exceptions.employee_info_exception import EmployeeInfoException
from exceptions.resource_not_found import ResourceNotFound
from models.employee_info import EmployeeInfo
from util.temp_db import EmployeeDB as db
from repository.employee_info_repo import EmployeeInfoRepo


class EmployeeInfoTemp(EmployeeInfoRepo):
    def get_all_employees(self):
        employees = db.employees.values()
        return [EmployeeInfo in employees]

    def get_employee_info_by_id(self, employee_id):
        try:
            return db.employees[employee_id]
        except KeyError:
            raise ResourceNotFound(f"Employee with id: {employee_id} - Not found")

    def delete_employee(self, employee_id):
        del db.employees[employee_id]
