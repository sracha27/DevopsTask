from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from scipy.constants import convert_temperature
import numpy
import math
app = Flask(__name__)
api = Api(app)

STUDENTS = {
    'student1': {"InputNumericalValue": '84.2' ,"InputUnitofMeasure": "Fahrenheit","TargetUnitofMeasure": "Rankine","StudentResponse": '543.94'},
    'student2': {"InputNumericalValue": '317.33' ,"InputUnitofMeasure": "Kelvin","TargetUnitofMeasure": "Fahrenheit","StudentResponse": '111.554'},
    'student3': {"InputNumericalValue": '6.5' ,"InputUnitofMeasure": "Fahrenheit","TargetUnitofMeasure": "Rankine","StudentResponse": 'dog'},
    'student4': {"InputNumericalValue": '136.1' ,"InputUnitofMeasure": "dogcow","TargetUnitofMeasure": "Celsius","StudentResponse": '45.32 '}
}

def abort_if_student_doesnt_exist(student_id):
    if student_id not in STUDENTS:
        abort(404, message="STUDENT {} doesn't exist".format(student_id))

parser = reqparse.RequestParser()
parser.add_argument('InputNumericalValue')
parser.add_argument('InputUnitofMeasure')
parser.add_argument('TargetUnitofMeasure')
parser.add_argument('StudentResponse')

# STUDENT
#   show a single student item and lets you delete them
class STUDENT(Resource):
    def get(self, student_id):
        abort_if_student_doesnt_exist(student_id)
        if (STUDENTS[student_id]['InputUnitofMeasure'] not in ('Fahrenheit','Rankine','Kelvin','Celsius') or STUDENTS[student_id]['TargetUnitofMeasure'] not in ('Fahrenheit','Rankine','Kelvin','Celsius')):
            result = {'result':'invalid','InputUnitofMeasure':STUDENTS[student_id]['InputUnitofMeasure'],'TargetUnitofMeasure':STUDENTS[student_id]['TargetUnitofMeasure']}
            return result
        elif (STUDENTS[student_id]['StudentResponse'].isnumeric() or len(STUDENTS[student_id]['StudentResponse'].split('.')[1]) > 2):
            result = {'result':'incorrect','StudentResponse':STUDENTS[student_id]['StudentResponse'], 'StudentResponseFloatSize':len(STUDENTS[student_id]['StudentResponse'].split('.')[1])}
            return result


        result = {'result':'correct'}
        student_num  = numpy.fromstring(STUDENTS[student_id]['StudentResponse'], dtype=int, sep=' ' )
        input_num =  numpy.fromstring(STUDENTS[student_id]['InputNumericalValue'], dtype=int, sep=' ' )
        output_num = convert_temperature(input_num,STUDENTS[student_id]['InputUnitofMeasure'].lower(),STUDENTS[student_id]['TargetUnitofMeasure'].lower())
        if math.floor(student_num) == math.floor(output_num):
            result = {'result':'correct','StudentInput': numpy.array_str(student_num), 'ScientificOutput': numpy.array_str(output_num)}
            return result
        else:
            print(output_num,flush=True)
            result = {'result':'wrong','StudentInput': numpy.array_str(student_num), 'ScientificOutput': numpy.array_str(output_num)}
            return result

    def delete(self, student_id):
        abort_if_student_doesnt_exist(student_id)
        del STUDENTS[student_id]
        return '', 204

    def put(self, student_id):
        args = parser.parse_args()
        student = {'InputNumericalValue': args['InputNumericalValue'],'InputUnitofMeasure': args['InputUnitofMeasure'],'TargetUnitofMeasure': args['TargetUnitofMeasure'],'StudentResponse': args['StudentResponse']}
        STUDENTS[student_id] = student
        return student, 201


# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class STUDENTList(Resource):
    def get(self):
        return STUDENTS

    def post(self):
        args = parser.parse_args()
        student_id = 'student%d' % (len(STUDENTS) + 1)
        STUDENTS[student_id] = {'student': args['student']}
        return STUDENTS[student_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(STUDENTList, '/students')
api.add_resource(STUDENT, '/students/<string:student_id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
