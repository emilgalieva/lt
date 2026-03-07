import flask
from flask import Flask

app = Flask(__name__)


@app.route("/carousel")
def info():
    return f"""
        <!DOCTYPE html>
        <html lang="ru">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                
                <link rel="stylesheet" href="{flask.url_for("static", filename="css/default.css")}">
                <title>Пейзажи марса</title>
            </head>
            <body>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" 
                 integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" 
                 crossorigin="anonymous"></script>
                <h1>Пейзажи марса</h1>
                <div id="carouselWithControls" class="carousel slide" data-bs-ride="carousel">
                    <div class="carousel-inner">
                        <div style="text-align: center;" class="carousel-item active" data-bs-interval="2000">
                            <img src="{flask.url_for("static", filename="img/1.jpg").removeprefix("/")}"
                             width="400" height="400">
                        </div>
                        <div style="text-align: center;" class="carousel-item" data-bs-interval="2000">
                            <img src="{flask.url_for("static", filename="img/2.jpg").removeprefix("/")}"
                             width="400" height="400">
                        </div>
                        <div style="text-align: center;" class="carousel-item" data-bs-interval="2000">
                            <img src="{flask.url_for("static", filename="img/3.jpg").removeprefix("/")}"
                             width="400" height="400">
                        </div>
                    </div>
                </div>
            </body>
        </html>
    """


if __name__ == "__main__":
    app.run("127.0.0.1", 8080)
