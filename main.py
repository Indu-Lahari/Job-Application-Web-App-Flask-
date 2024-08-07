from flask import Flask, render_template, request
# this library allows to interact with database using more high-level code, makes easier to manage database and data
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Parameters of Database
app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
# Instantiate Database with flask instance 'app' as argument
db = SQLAlchemy(app)


# To create a database we need database model , we create it by using class
class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    middle_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    mobile = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        middle_name = request.form["middle_name"]
        last_name = request.form["last_name "]
        email = request.form["email"]
        mobile = request.form["mobile"]
        date = request.form["date"]
        occupation = request.form["occupation"]
    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)