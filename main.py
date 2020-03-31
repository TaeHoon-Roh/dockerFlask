from flask import Flask, make_response, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    values = request.values.get("body")
    print(values)
    if values == None:
        return render_template('index.html')
    else:
        return make_response(values)

@app.route('/createuser', methods=['GET', 'POST'])
def createUser():
    return render_template('createuser.html')

@app.route('/userinfo', methods=['POST'])
def test():
    value = request.values.to_dict()
    print(value)

    return make_response(value)

#run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=9001)
