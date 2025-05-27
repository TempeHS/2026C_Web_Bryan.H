from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    card_data = (
        ("Meet the skibidis", "Big library of skibidi", "Yessir!", "static/images/slider_1.png"),
        ("Who are they?", "Big library of skibidi", "Yessir!", "static/images/logo.png"),
        ("Meet the skibidis", "Big library of skibidi", "Yessir!", "static/images/logo.png"),
        ("Meet the skibidis", "Big library of skibidi", "Yessir!", "static/images/logo.png"),
        ("Meet the skibidis", "Big library of skibidi", "Yessir!", "static/images/logo.png")

    )

    return render_template("index.html", cards=card_data), 200

if __name__ == '__main__':
    app.run(debug=True)
