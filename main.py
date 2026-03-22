import json

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/member")
def info():
    with open("templates/.json", "rt", encoding="utf-8") as f:
        data = json.load(f)
    return render_template("carousel.html", len=len, data=data)

if __name__ == "__main__":
    app.run("127.0.0.1", 8080)