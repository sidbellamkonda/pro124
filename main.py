from flask import Flask, jsonify, request
app = Flask(__name__)
list1 = [
    {
        "id" : 1,
        "name" : u"Siddharth",
        "contact" : u"12343232",
        "done" : False
    },
    {
        "id" : 2,
        "name" : u"Bob",
        "contact" : u"01982374",
        "done" : False
    }
]
@app.route("/get-data")
def get_contact():
    return jsonify({
        "data" : list1
    })
@app.route("/add-data", methods = ["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "Please provide the data"
        },400)
    contact = {
        "id" : list1[-1]["id"]+1,
        "name": request.json["name"],
        "contact" : request.json.get("contact", ""),
        "done": False
    }
    list1.append(contact)
    return jsonify({
        "status": "success",
        "message": "Contact added successfully"
    })
app.run(debug = True)