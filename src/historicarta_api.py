from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data - replace with your actual data
historical_data = [
    {
        "id": 1,
        "Type": "Event",
        "Dates": "1776-07-04",
        "Description": "Declaration of Independence of the United States",
        "Nationality": "American",
        "Tags": ["Independence", "Revolution"]
    },
    {
        "id": 2,
        "Type": "Person",
        "Dates": "1564-04-23",
        "Description": "William Shakespeare was born.",
        "Nationality": "English",
        "Tags": ["Literature", "Playwright"]
    }
]

@app.route('/')
def index():
    return "Welcome to Historicarta API!"

@app.route('/events', methods=['GET', 'POST'])
def events():
    if request.method == 'GET':
        events = [data for data in historical_data if data["Type"] == "Event"]
        return jsonify(events)
    elif request.method == 'POST':
        new_event = request.json
        new_event["id"] = len(historical_data) + 1
        historical_data.append(new_event)
        return jsonify({"message": "Event added successfully", "event": new_event}), 201

@app.route('/persons', methods=['GET', 'POST'])
def persons():
    if request.method == 'GET':
        persons = [data for data in historical_data if data["Type"] == "Person"]
        return jsonify(persons)
    elif request.method == 'POST':
        new_person = request.json
        new_person["id"] = len(historical_data) + 1
        historical_data.append(new_person)
        return jsonify({"message": "Person added successfully", "person": new_person}), 201

if __name__ == '__main__':
    app.run(debug=True)

