from flask import Flask, jsonify, request
from src.app.config import Config
from models import db, Employee
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/team/get_employees', methods=['GET'])
def get_employees():
    url = app.config['EXTERNAL_SYSTEM_URL']
    auth = HTTPBasicAuth(app.config['EXTERNAL_SYSTEM_LOGIN'], app.config['EXTERNAL_SYSTEM_PASSWORD'])
    headers = {'Content-Type': 'application/json'}
    data = {
        "Request_id": "e1477272-88d1-4acc-8e03-7008cdedc81e",
        "ClubId": app.config['CLUB_ID'],
        "Method": "GetSpecialistList",
        "Parameters": {
            "ServiceId": ""
        }
    }
    response = requests.post(url, auth=auth, headers=headers, data=json.dumps(data))
    employees_data = response.json()

    employees = []
    for emp in employees_data.get('Specialists', []):
        employee = Employee(
            id=emp.get('Id', ''),
            name=emp.get('Name', ''),
            last_name=emp.get('LastName', ''),
            phone=emp.get('Phone', ''),
            image_url=emp.get('ImageUrl', '')
        )
        employees.append(employee)

    return jsonify([{
        'id': emp.id,
        'name': emp.name,
        'last_name': emp.last_name,
        'phone': emp.phone,
        'image_url': emp.image_url
    } for emp in employees])

if __name__ == '__main__':
    app.run(debug=True)
