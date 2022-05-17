from abc import abstractmethod, ABC


class FormRepo(ABC):

    @abstractmethod
    def get_all_forms_for_employee(self, employee_id):
        pass

    @abstractmethod
    def submit_form(self, form):
        pass

    @abstractmethod
    def update_form_dsup(self, change):
        pass

    @abstractmethod
    def update_form_dhead(self, change):
        pass

    @abstractmethod
    def update_form_benco(self, change):
        pass

    @abstractmethod
    def delete_form(self, employee_id):
        pass
