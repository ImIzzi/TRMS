from flask import jsonify, request

from exceptions.resource_not_found import ResourceNotFound
from models.form import Form
from repository.form_repo_impl import FormRepoImpl
from services.form_service import FormService

fr = FormRepoImpl()
fs = FormService(fr)


def run(app):

    @app.route("/login/<employee_id>/form", methods=["GET"])
    def get_all_forms_for_employee(employee_id):
        try:
            return fs.get_all_forms_for_employee(int(employee_id)).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/login/submit/form", methods=["POST"])
    def post_form():
        body = request.json

        form = Form(fname=body["fname"], lname=body["lname"], event_date=body["eventDate"],
                    event_time=body["eventTime"], location=body["location"], description=body["description"],
                    cost=body["cost"], grading_format=body["gradingFormat"], type_of_event=body["typeOfEvent"],
                    employee_id=body["employeeId"], final_grade=body["finalGrade"], work_just=body["workJust"])
        form = fs.submit_form(form)

        return form.json()

    @app.route("/login/supervisor/<employee_id>/form/update", methods=["PUT"])
    def put_form_dsup(employee_id):
        body = request.json
        form = Form(employee_id=employee_id, reject_form=body["rejectForm"], deny_reason=body["denyReason"],
                    dsup_approval=body["dsupApproval"])
        form = fs.update_form_dsup(form)

        return form.json()

    @app.route("/login/dhead/<employee_id>/form/update", methods=["PUT"])
    def put_form_dhead(employee_id):
        body = request.json
        form = Form(employee_id=employee_id, reject_form=body["rejectForm"], deny_reason=body["denyReason"],
                    dhead_approval=body["dheadApproval"])
        form = fs.update_form_dhead(form)

        return form.json()

    @app.route("/login/benco/<employee_id>/form/update", methods=["PUT"])
    def put_form_benco(employee_id):
        body = request.json
        form = Form(employee_id=employee_id, reject_form=body["rejectForm"], deny_reason=body["denyReason"],
                    benco_approval=body["bencoApproval"])
        form = fs.update_form_benco(form)

        return form.json()

    @app.route("/login/<employee_id>/form", methods=['DELETE'])
    def delete_form(employee_id):
        fs.delete_form(employee_id)
        return f"Deleted form related to : {employee_id}", 204

    @app.route("/login/<employee_id>/request", methods=["PUT"])
    def request_info(employee_id):
        pass

