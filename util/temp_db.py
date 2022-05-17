
from models.employee_info import EmployeeInfo
from models.form import Form


class EmployeeDB:
    employees = {
        1: EmployeeInfo(id=1, fname="Larry", lname="King", erole="department employee"),
        2: EmployeeInfo(id=2, fname="Jerry", lname="Jenkins", erole="department supervisor"),
        3: EmployeeInfo(id=3, fname="Billy", lname="Bob", erole="department head"),
        4: EmployeeInfo(id=4, fname="Mister", lname="Cord", erole="benco"),
    }


class FormDB:
    forms = {
        1: Form(id=1, fname="Larry", lname="King", event_date="03/23/3022", event_time="08:00AM", location="Texas",
                description="University Course", cost=7500.04, grading_format="txt", type_of_event="university course",
                employee_id=1, passing_cutoff="C", urgent=False, final_grade="B", work_just="Advance Knowledge",
                add_info=False, reject_form=False, deny_reason="", dsup_approval=True, dhead_approval=True,
                benco_approval=True),

        2: Form(id=1, fname="Jerry", lname="Jenkins", event_date="04/12/3022", event_time="09:00AM", location="Texas",
                description="College Course", cost=6200.15, grading_format="txt", type_of_event="college course",
                employee_id=2, passing_cutoff="C", urgent=False, final_grade="A", work_just="Benefit Work Role",
                add_info=False, reject_form=False, deny_reason="", dsup_approval=True, dhead_approval=True,
                benco_approval=True)
    }
