from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def hello_world():
    dictionary = dict()
    dictionary['query'] = str(request.args['query'])
    return jsonify(dictionary)


if __name__ == '__main__':
    app.run()
