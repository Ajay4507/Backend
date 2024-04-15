from flask import Flask, jsonify
from flask_babel import Babel, gettext
import json
from datetime import datetime

# postgres://flask_deployment_yfcx_user:EYOTjNelK1jPBkiyHIyPMCor7MAl7dzI@dpg-coefafol5elc738767h0-a.oregon-postgres.render.com/flask_deployment_yfcx


app = Flask(__name__)
babel = Babel(app)

class Organization:
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('Name')
        self.type = data.get('OrganizationType')
        self.created_by = data.get('CreatedBy')
        self.creation_date = self.format_date(data.get('CreationDate'))
        self.updated_on = self.format_date(data.get('UpdatedOn'))
        self.updated_by = data.get('UpdatedBy')

    def get_not_filled_fields(self):
        not_filled_fields = []
        if not self.id:
            not_filled_fields.append('id')
        if not self.name:
            not_filled_fields.append('Name')
        if not self.type:
            not_filled_fields.append('OrganizationType')
        if not self.created_by:
            not_filled_fields.append('CreatedBy')
        if not self.creation_date:
            not_filled_fields.append('CreationDate')
        if not self.updated_on:
            not_filled_fields.append('UpdatedOn')
        if not self.updated_by:
            not_filled_fields.append('UpdatedBy')
        return not_filled_fields

    def is_valid(self):
        return all([self.id, self.name, self.type, self.created_by, self.creation_date, self.updated_on, self.updated_by])

    def format_date(self, date_str):
        return datetime.strptime(date_str, "%m/%d/%Y").strftime("%Y-%m-%d") if date_str else None

@app.route('/')
def index():
    return gettext("Welcome to the Flask App.")

@app.route('/load_data')
def load_data():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)

        for item in data:
            organization = Organization(item)
            if not organization.is_valid():
                not_filled_fields = organization.get_not_filled_fields()
                error_message = gettext("Organization with ID {id} is missing required fields: {fields}").format(id=organization.id, fields=', '.join(not_filled_fields))
                return jsonify({'error': {'category': 'Value Error', 'type': 'data_validation_error', 'message': error_message}}), 400

        return gettext("Data loaded successfully.")
    except Exception as e:
        error_message = gettext("An error occurred: {error}").format(error=str(e))
        return jsonify({'error': {'category': 'Runtime Error', 'type': 'internal_error', 'message': error_message}}), 500

if __name__ == '__main__':
    app.run(debug=True)
