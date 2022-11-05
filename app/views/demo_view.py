from flask import Blueprint, request, render_template, abort
from flask import jsonify


class DemoViews:

    def __init__(self):
        self.student_record = {"101": {"Name": "MallaReddy", "Graduation": "BTech", "Branch": "MEC", "Year": 2017,
                            "gardes": {"Degree": 72, "Inter": 98, "ssc": 93}},
                    "106": {"Name": "Lakshmi", "Graduation": "BSC", "Branch": "CS", "Year": 2018,
                            "gardes": {"Degree": 84, "Inter": 75, "ssc": 90}},
                    "169": {"Name": "Navya", "Graduation": "BSC", "Branch": "CS", "Year": 2020,
                            "gardes": {"Degree": 86, "Inter": 97, "ssc": 97}}}

        self.demo_page_views = Blueprint('demo_page', __name__)

        @self.demo_page_views.route('/', methods=["GET"])
        def __home_page():
            return jsonify({"A": 65})

        @self.demo_page_views.route('/students', methods=["GET"])
        def __get_all_students():
            return self.get_all_students()

        @self.demo_page_views.route('/students/<int:studentID>', methods=["GET"])
        def __get_student_by_id(studentID):
            return self.get_student_by_id(studentID)

    def get_all_students(self):
        return jsonify(self.student_record)

    def get_student_by_id(self, studentID):
        args = request.args
        print(args)
        data = self.student_record.get(str(studentID))
        if data:
            return jsonify(data)
        else:
            return jsonify({"status_code": 500, "errorText": f"The record was not presnet with id {studentID}"})


