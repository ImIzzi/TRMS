import requests
from flask import jsonify, request

from exceptions.resource_not_found import ResourceNotFound
from repository.employee_info_impl import EmployeeInfoRepoImpl
from services.employee_info_service import EmployeeInfoService
from models.employee_info import EmployeeInfo

er = EmployeeInfoRepoImpl()
eis = EmployeeInfoService(er)


def run(app):
    @app.route("/login/all_employees/info", methods=["GET"])
    def get_all_employees():
        return jsonify([employees.json() for employees in eis.get_all_employees()]), 200

    @app.route("/login/<employee_id>/info", methods=["GET"])
    def get_employee_info_id(employee_id):
        try:
            # return jsonify(eis.get_employee_info_by_id(int(employee_id))), 200
            return eis.get_employee_info_by_id(int(employee_id)).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/register/employee_info", methods=["POST"])
    def post_employee():
        body = request.json

        employee = EmployeeInfo(fname=body["fname"], lname=body["lname"], erole=body["erole"])
        employee = eis.create_employee(employee)

        return employee.json()

    @app.route("/login/<employee_id>/del", methods=["DELETE"])
    def delete_employee(employee_id):
        try:
            eis.delete_employee(employee_id)
            return '', 204
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404
























    # @app.route("/login/<employee_name>/info", methods=["GET"])
    # def get_employee_info_name(employee_name):
    #     try:
    #         return jsonify(eis.get_employee_info_by_name(employee_name)), 200
    #     except ValueError as e:
    #         return "Not a valid ID", 400
    #     except ResourceNotFound as r:
    #         return r.message, 404


