import flask
from flask import Flask, render_template, url_for
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
with open("static/img/images_extensions", "rt", encoding="utf-8") as f:
    images_extensions = f.read().removesuffix("\n").split(",")
added_images = len(images_extensions)

@app.route("/galery", methods=["GET", "POST"])
def info():
    global added_images
    if flask.request.method == "GET":
        return render_template("carousel.html", flask=flask, added_images=added_images, extensions=images_extensions)
    else:
        if (name := flask.request.files.get("file").filename) is not None:
            with open(f"static/img/{added_images}.{(extension := name.split(".")[-1])}", "w") as f:
                pass
            flask.request.files["file"].save(dst=f"static/img/{added_images}.{(extension := name.split(".")[-1])}")
            added_images += 1
            images_extensions.append(extension)
        return ""


if __name__ == "__main__":
    app.run("127.0.0.1", 8080)
    with open("static/img/images_extensions", "wt", encoding="utf-8") as f:
        f.write(",".join(images_extensions))