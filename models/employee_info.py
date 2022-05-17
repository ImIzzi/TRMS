

class EmployeeInfo:

    def __init__(self, fname="", lname="", id=0, erole=""):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.erole = erole

    def __repr__(self):
        return str({
            "fname": self.fname,
            "lname": self.lname,
            "id": self.id,
            "erole": self.erole
        })

    def json(self):
        return {
            "fname": self.fname,
            "lname": self.lname,
            "id": self.id,
            "erole": self.erole
        }

    @staticmethod
    def json_parse(json):
        employee = EmployeeInfo()
        employee.fname = json["fname"]
        employee.lname = json["lname"]
        employee.id = json["id"]
        employee.erole = json["erole"]
        return employee

    def __eq__(self, other):
        if not other:
            return False

        if not isinstance(other, EmployeeInfo):
            return False

        for value1, value2 in zip(vars(self).values(), vars(other).values()):
            if value1 != value2:
                return False

        return True


def _test():
    employee1 = EmployeeInfo()
    employee2 = EmployeeInfo()

    print(employee1 == employee2)

    employee1 = EmployeeInfo(fname="Izzi", lname="Last", erole="department employee")
    employee2 = EmployeeInfo(fname="Izzi", lname="Last", erole="department employee")

    print(employee1 == employee2)


if __name__ == '__main__':
    _test()
