from flask import Flask, jsonify, make_response, request, abort
from hivery.models import companies, people, PersonSerializer, CommonFriendSerializer, get_person, FoodSerializer

app = Flask(__name__)


@app.route('/<company>', methods=['GET'])
def get_employees(company):
    """
    Given a company, return all their employees.
    """
    company_obj = next((c for c in companies if
                        company.lower() in [c['company'].lower(), str(c['index'])]
                        ), {})
    if not company_obj:
        abort(make_response(jsonify(message="Company not found"), 404))

    employees = [p for p in people if p['company_id'] == company_obj['index']]
    return jsonify(PersonSerializer(employees, many=True).data)


@app.route('/friend', methods=['GET'])
def get_common_friend():
    """
    Given 2 people, provide their information (Name, Age, Address, phone)
    and the list of their friends in common which have brown eyes and are still alive.
    """
    person_1_id, person_2_id = request.args.get('person').split(',')

    person_1 = get_person(person_1_id)
    person_2 = get_person(person_2_id)

    if not person_1 or not person_2:
        abort(make_response(jsonify(message="Employee not found"), 404))

    friend_indexs = set([i['index'] for i in person_1['friends']]).intersection(
        [i['index'] for i in person_2['friends']])

    result = CommonFriendSerializer({
        "person_1": person_1,
        "person_2": person_2,
        "friends": [get_person(index, 'index') for index in friend_indexs]
    })

    return jsonify(result.data)


@app.route('/food/<_id>', methods=['GET'])
def get_food(_id):
    """
    Given 1 people, provide a list of fruits and vegetables they like.
     This endpoint must respect this interface for the output:
    {"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}
    """
    person = get_person(_id)

    if not person:
        abort(make_response(jsonify(message="Employee not found"), 404))

    return jsonify(FoodSerializer(person).data)


if __name__ == '__main__':
    app.run()
