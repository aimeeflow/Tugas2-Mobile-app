from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hi! This is Aimee trying to work on Mobile App Backend!"

@app.route('/api/products')
def products():
    data = [
        {"id": 1, "nama": "Aimee", "email": "aimee@mail.com"},
        {"id": 2, "nama": "Juni", "email": "juni@mail.com"},
        {"id": 3, "nama": "Nindy", "email": "nindy@mail.com"}
    ]
    return jsonify(data)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)

