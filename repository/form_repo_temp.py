from exceptions.resource_not_found import ResourceNotFound
from repository.form_repo import FormRepo
from models.form import Form
from util.temp_db import FormDB as db


class FormRepoTemp(FormRepo):

    def get_all_forms_for_employee(self, employee_id):
        try:
            return db.forms[employee_id]
        except KeyError:
            raise ResourceNotFound(f"Form belonging to Employee with the id of: {employee_id} - Not Found")

    def submit_form(self, form):
        pass

    def update_form_dsup(self, change):
        pass

    def update_form_dhead(self, change):
        pass

    def update_form_benco(self, change):
        pass

    def delete_form(self, employee_id):
        pass