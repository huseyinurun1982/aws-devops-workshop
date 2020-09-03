from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")

def head():    
    return render_template("index.html", huseyin = True)

@app.route("/for")
def for_example():
    names = ['Ahmet', 'Muhammed', 'Bulent', 'Neda', 'Ömer', 'Hüseyin']
    return render_template("deneme.html", isimler = names)

if __name__ == '__main__':
    app.run(debug = True)