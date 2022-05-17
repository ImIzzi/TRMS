class Form:

    def __init__(self, id=0, fname="", lname="", event_date="", event_time="", location="", description="", cost=0,
                 grading_format="", type_of_event="", employee_id=0, passing_cutoff='C', urgent="No", final_grade="",
                 work_just="", add_info="", reject_form="No", deny_reason='', dsup_approval="No", dhead_approval="No",
                 benco_approval="No"):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.event_date = event_date
        self.event_time = event_time
        self.location = location
        self.description = description
        self.cost = cost
        self.grading_format = grading_format
        self.type_of_event = type_of_event
        self.employee_id = employee_id
        self.passing_cutoff = passing_cutoff
        self.urgent = urgent
        self.final_grade = final_grade
        self.work_just = work_just
        self.add_info = add_info
        self.reject_form = reject_form
        self.deny_reason = deny_reason
        self.dsup_approval = dsup_approval
        self.dhead_approval = dhead_approval
        self.benco_approval = benco_approval

    def __repr__(self):
        return str({
            "id": self.id,
            "fname": self.fname,
            "lname": self.lname,
            "event_date": self.event_date,
            "event_time": self.event_time,
            "location": self.location,
            "description": self.description,
            "cost": self.cost,
            "grading_format": self.grading_format,
            "type_of_event": self.type_of_event,
            "employee_id": self.employee_id,
            "passing_cutoff": self.passing_cutoff,
            "urgent": self.urgent,
            "final_grade": self.final_grade,
            "work_just": self.work_just,
            "add_info": self.add_info,
            "reject_form": self.reject_form,
            "deny_reason": self.deny_reason,
            "dsup_approval": self.dsup_approval,
            "dhead_approval": self.dhead_approval,
            "benco_approval": self.benco_approval
        })

    def json(self):
        return {
            "id": self.id,
            "fname": self.fname,
            "lname": self.lname,
            "eventDate": self.event_date,
            "eventTime": self.event_time,
            "location": self.location,
            "description": self.description,
            "cost": self.cost,
            "gradingFormat": self.grading_format,
            "typeOfEvent": self.type_of_event,
            "employeeId": self.employee_id,
            "passingCutoff": self.passing_cutoff,
            "urgent": self.urgent,
            "finalGrade": self.final_grade,
            "workJust": self.work_just,
            "addInfo": self.add_info,
            "rejectForm": self.reject_form,
            "denyReason": self.deny_reason,
            "dsupApproval": self.dsup_approval,
            "dheadApproval": self.dhead_approval,
            "bencoApproval": self.benco_approval
        }


    # @staticmethod
    # def json_parse(json):
    #     form = Form()
    #     form.id = json["id"]
    #     form.fname = json["fname"]
    #     form.lname = json["lname"]
    #     form.event_date = json["eventDate"]
    #     form.event_time = json["eventTime"]
    #     form.location = json["location"]
    #     form.description = json["description"]
    #     form.cost = json["cost"]
    #     form.grading_format = json["gradingFormat"] if "gradingFormat" in json else "Exam"
    #     form.type_of_event = json["typeOfEvent"]
    #     form.employee_id = json["employeeId"] if "employeeId" in json else 0
    #     form.passing_cutoff = json["passingCutoff"] if "passingCutoff" in json else "C"
    #     form.urgent = json["urgent"] if "urgent" in json else False
    #     form.final_grade = json["finalGrade"] if "finalGrade" in json else "A"
    #     form.work_just = json["workJust"]
    #     form.add_info = json["addInfo"] if "addInfo" in json else False
    #     form.reject_form = json["rejectForm"] if "rejectForm" in json else False
    #     form.deny_reason = json["denyReason"] if "denyReason" in json else ""
    #     form.dsup_approval = json["dsupApproval"] if "dsupApproval" in json else False
    #     form.dhead_approval = json["dheadApproval"] if "dheadApproval" in json else False
    #     form.benco_approval = json["bencoApproval"] if "bencoApproval" in json else False
    #     return form


