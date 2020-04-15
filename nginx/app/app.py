import os
from flask import Flask, request, jsonify, render_template, redirect
from flask_pymongo import PyMongo

application = Flask(__name__)

application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']


mongo = PyMongo(application)
db = mongo.db

coll = db.userData #Select the collection name

@application.route('/')
def my_form():
    return render_template('index.html')

@application.route('/', methods=['POST'])
def insertData():
    text = request.values.get('text')
    data = {"name":text}
    mongo.db.coll.insert(data)
    return redirect("/")

@application.route("/search", methods = ['GET'])
def search():
    text_to_search = request.values.get('text')
    results = getResult(text_to_search)
    # read all data
    docs = coll.find()
    data = []
    for i in docs:
        data.append(i)

    return render_template('searchlist.html', results = results, data = data)

def getResult(input):
    data = input
    check_db = coll.find({"name":data})
    return check_db

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)

