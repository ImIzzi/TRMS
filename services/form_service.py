from repository.form_repo import FormRepo


class FormService:

    def __init__(self, form_repo: FormRepo):
        self.form_repo = form_repo

    def get_all_forms_for_employee(self, employee_id):
        return self.form_repo.get_all_forms_for_employee(employee_id)

    def submit_form(self, form):
        return self.form_repo.submit_form(form)

    def update_form_dsup(self, change):
        return self.form_repo.update_form_dsup(change)

    def update_form_dhead(self, change):
        return self.form_repo.update_form_dhead(change)

    def update_form_benco(self, change):
        return self.form_repo.update_form_benco(change)

    def delete_form(self, employee_id):
        return self.form_repo.delete_form(employee_id)
