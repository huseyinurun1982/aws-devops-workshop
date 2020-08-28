from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", num1 = 25, num2 = 50)

@app.route("/second")
def second():
    return render_template("yeni.html", hazirlayan = "Hüseyin")

if __name__ == "__main__":
    app.run(debug = True)