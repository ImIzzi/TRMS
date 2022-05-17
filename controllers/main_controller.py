from controllers import form_controller as fc
from controllers import employee_info_controller as ec
from controllers import login_controller as lc


def run(app):
    fc.run(app)
    ec.run(app)
    lc.run(app)
