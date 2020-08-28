from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return "Hello World!"

@app.route("/second")
def second():
    return "This is a second page"

@app.route("/third/subthird")
def third():
    return "This is the third of subthird."

@app.route("/forth/<string:id>")
def forth(id):
    return f"Id of this page of {id}"

if __name__ == '__main__':
    app.run(debug = True)