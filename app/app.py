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
    text_to_search = request.values.get('search_text')
    regex_query = { "name" : {"$regex" : text_to_search} }
    check_db = mongo.db.coll.find(regex_query)
    print (check_db)
    x   = []
    for i in check_db:
        x.append(i["name"])

    return render_template('index.html', table=x)

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)

