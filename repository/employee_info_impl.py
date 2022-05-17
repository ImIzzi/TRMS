from exceptions.employee_info_exception import EmployeeInfoException
from exceptions.resource_not_found import ResourceNotFound
from models.employee_info import EmployeeInfo
from repository.employee_info_repo import EmployeeInfoRepo
from util.db_connection import connection


def build_employee(record):
    return EmployeeInfo(id=record[0], fname=record[1], lname=record[2], erole=record[3])


class EmployeeInfoRepoImpl(EmployeeInfoRepo):

    def get_all_employees(self):
        sql = "SELECT * FROM employee_info"
        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        employee_list = [build_employee(record) for record in records]

        return employee_list

    def get_employee_info_by_id(self, employee_id):
        sql = "SELECT * FROM employee_info WHERE id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])

        record = cursor.fetchone()

        if record:
            return build_employee(record)
        else:
            raise ResourceNotFound(f"Employee with id: {employee_id} - Not found")

    def create_employee(self, employee_info):
        sql = "INSERT INTO employee_info VALUES (default,%s,%s,%s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [employee_info.fname, employee_info.lname, employee_info.erole])

        connection.commit()
        record = cursor.fetchone()

        return build_employee(record)

    def delete_employee(self, employee_id):
        sql = "DELETE FROM employee_info WHERE id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        connection.commit()


def _test():
    er = EmployeeInfoRepoImpl()
    employee = er.get_employee_info_by_id(5)
    print(employee)

    print(er.get_all_employees())
    # print("---DELETE---")
    # er.delete_employee(6)   # This will delete any employee I choose to delete by their ID ()
    # print(er.get_all_employees())


if __name__ == '__main__':
    _test()
