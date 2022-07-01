from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.noj5q89.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/mars", methods=["POST"])
def web_mars_post():
    response = request.values

    name = response.get('name') # request.values.get('name') or request.form.get('name')
    address = response.get('address')
    size = response.get('size')

    saveData = {
        'name': name,
        'address': address,
        'size': size
    }

    db.mars.insert_one(saveData)


    return jsonify({'msg': 'POST 연결 완료!'})


@app.route("/mars", methods=["GET"])
def web_mars_get():
    orderList = list(db.mars.find({},{'_id':False}))
    return jsonify({'orders': orderList})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

