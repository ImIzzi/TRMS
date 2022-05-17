import unittest
from unittest.mock import MagicMock

from models.employee_info import EmployeeInfo
from repository.employee_info_impl import EmployeeInfoRepoImpl
from services.employee_info_service import EmployeeInfoService


class TestEmployeeInfoService(unittest.TestCase):
    er = EmployeeInfoRepoImpl()
    es = EmployeeInfoService(er)

    def test_get_employee_by_id(self):
        self.es.get_all_employees = MagicMock(return_value=[
            EmployeeInfo(fname="Larry", lname="King", id=1, erole="department employee"),
            EmployeeInfo(fname="Billy", lname="Bob", id=3, erole="department head"),
            EmployeeInfo(fname="Mister", lname="Cord", id=4, erole="benco")
        ])

        refined_employees = self.es.get_employee_info_by_id(4)
        print(refined_employees)

        self.assertEqual(refined_employees, EmployeeInfo(fname="Mister", lname="Cord", id=4, erole="benco"))


if __name__ == '__main__':
    unittest.main()