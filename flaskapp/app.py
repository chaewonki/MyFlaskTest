from flask import Flask, render_template, request, redirect, url_for
import os

# Update the template folder path to point to the 'flaskapp/templates' directory
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "templates"))
app = Flask(__name__, template_folder=template_dir)

# List to store items (in a real app, you'd use a database)
items = []

@app.route("/")
def index():
    return render_template("index.html", items=items)

@app.route("/add_item", methods=["POST"])
def test_add_item(client):
    # Test adding an item via POST request
    response = client.post('/add_item', data={'item': 'Test Item'})
    
    # Assert that the response is a redirect (302)
    assert response.status_code == 302
    
    # Follow the redirect to the index page (this is where you expect the item to appear)
    response = client.get('/')  # This follows the redirect and accesses the index page
    
    # Assert that the added item appears in the rendered template
    assert b"Test Item" in response.data  # The item should now be in the index view


@app.route("/delete_item/<int:index>")
def delete_item(index):
    if 0 <= index < len(items):
        items.pop(index)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
