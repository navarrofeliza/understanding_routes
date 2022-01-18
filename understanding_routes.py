from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/hi/<name>!') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hi, " + name"!"

@app.route('/dojo')
def dojo():
    return "Dojo"


@app.route('/hello/<string:hello>/<int:num>')
def hello(hello,num):
    return f"{Hello * num}"

@app.route('/hello/<string:bye>/<int:num>')
def hello(bye,num):
    return f"{bye * num}"

@app.route('/hello/<string:dog>/<int:num>')
def hello(dog,num):
    return f"{dog * num}"


if __name__=="__main__":
    app.run(debug=True)