# flaskapp/app.py
from flask import Flask, render_template, request, redirect, url_for
import os

# Update the template folder path
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "templates"))
app = Flask(__name__, template_folder=template_dir)

# List to store items (in a real app, you'd use a database)
items = []


@app.route("/")
def index():
    return render_template("index.html", items=items)


@app.route("/add_item", methods=["POST"])
def add_item():
    item = request.form.get("item")
    if item:
        items.append(item)
    return redirect(url_for("index"))


@app.route("/delete_item/<int:index>")
def delete_item(index):
    if 0 <= index < len(items):
        items.pop(index)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
