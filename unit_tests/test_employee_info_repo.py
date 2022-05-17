import unittest

from models.employee_info import EmployeeInfo
from repository.employee_info_impl import EmployeeInfoRepoImpl

er = EmployeeInfoRepoImpl()


class TestEmployeeInfoRepo(unittest.TestCase):

    added_employee = EmployeeInfo()

    def test_get_employee_success(self):
        employee_info = er.get_employee_info_by_id(5)
        self.assertEqual(employee_info, EmployeeInfo(fname="Izzi", lname="Saucy", id=5, erole="department employee"))

    def test_create_employee_success(self):
        TestEmployeeInfoRepo.added_employee = er.create_employee(self.added_employee)

        self.assertEqual(self.added_employee, EmployeeInfo(fname="", lname="", id=self.added_employee.id, erole=""))

        self.assertIsNotNone(er.get_employee_info_by_id(self.added_employee.id))
        print(self.added_employee)

    @classmethod
    def tearDownClass(cls):
        if cls.added_employee.id:
            er.delete_employee(cls.added_employee.id)


if __name__ == '__main__':
    unittest.main()