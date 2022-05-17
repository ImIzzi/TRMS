from exceptions.resource_not_found import ResourceNotFound
from repository.form_repo import FormRepo
from models.form import Form
from util.db_connection import connection


def build_form(record):
    if record:
        return Form(id=record[0], fname=record[1], lname=record[2], event_date=record[3], event_time=record[4],
                    location=record[5], description=record[6], cost=float(record[7]), grading_format=record[8],
                    type_of_event=record[9], employee_id=record[10], passing_cutoff=record[11], urgent=record[12],
                    final_grade=record[13], work_just=record[14], add_info=record[15], reject_form=record[16],
                    deny_reason=record[17], dsup_approval=record[18], dhead_approval=record[19],
                    benco_approval=record[20])
    else:
        return None


class FormRepoImpl(FormRepo):
    def get_all_forms_for_employee(self, employee_id):
        sql = "SELECT * FROM form WHERE employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        connection.commit()
        record = cursor.fetchone()

        if record:
            return build_form(record)
        else:
            raise ResourceNotFound(f"Form belonging to Employee with the id of: {employee_id} - Not Found")

    def submit_form(self, form):
        sql = "INSERT INTO form VALUES (default, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, default, default, %s, %s, " \
              "default, default, default, default, default, default) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [form.fname, form.lname, form.event_date, form.event_time, form.location, form.description,
                             form.cost, form.grading_format, form.type_of_event, form.employee_id, form.final_grade,
                             form.work_just])
        connection.commit()
        record = cursor.fetchone()

        return build_form(record)

    def update_form_dsup(self, change):
        sql = f"UPDATE form SET reject_form = %s, dsup_approval = %s, deny_reason = %s WHERE employee_id = %s " \
              f"RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [change.reject_form, change.dsup_approval, change.deny_reason, change.employee_id])

        connection.commit()
        record = cursor.fetchone()

        return build_form(record)

    def update_form_dhead(self, change):
        sql = "UPDATE form SET reject_form = %s, dhead_approval = %s, deny_reason = %s WHERE employee_id = %s " \
              "RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [change.reject_form, change.dhead_approval, change.deny_reason, change.employee_id])

        connection.commit()
        record = cursor.fetchone()

        return build_form(record)

    def update_form_benco(self, change):
        sql = "UPDATE form SET reject_form = %s, benco_approval = %s, deny_reason = %s WHERE employee_id = %s " \
              "RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [change.reject_form, change.benco_approval, change.deny_reason, change.employee_id])

        connection.commit()
        record = cursor.fetchone()

        return build_form(record)

    def delete_form(self, employee_id):
        sql = "DELETE FROM form WHERE employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        connection.commit()
