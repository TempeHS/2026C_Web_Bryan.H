from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    card_data = (
        ("Meet the skibidis", "Big library of skibidi", "Yessir!", "static/images/slider_1.png", "/Library.html"),
        ("Who are they?", "And I wonder", "Yessir!", "static/images/logo.png"),
        ("Meet the skibidis", "Big library of skibidi", "Yessir!", "static/images/logo.png"),
        ("Meet the skibidis", "Big library of skibidi", "Yessir!", "static/images/logo.png"),
        ("Meet the skibidis", "Big library of skibidi", "Yessir!", "static/images/logo.png")

    )

    return render_template("index.html", cards=card_data), 200


@app.route('/contact.html')
def contact():
    return render_template("contact.html"), 200


@app.route('/Library.html')
def Library():
    return render_template("Library.html"),

@app.route('/mango.html')
def mango():
    return render_template("mango.html")

if __name__ == '__main__':
    app.run(debug=True)
