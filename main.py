from datetime import datetime
from flask import Flask, render_template, request, flash
# this library allows to interact with database using more high-level code, makes easier to manage database and data
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)

# Parameters of Database
app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

# Declare MAIL_SERVER
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "your_gmail"
app.config["MAIL_PASSWORD"] = "your_app_password"

# Instantiate Database with flask instance 'app' as argument
db = SQLAlchemy(app)

mail = Mail(app)


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
        last_name = request.form["last_name"]
        email = request.form["email"]
        mobile = request.form["mobile"]
        date = request.form["date"]
        date_object = datetime.strptime(date, "%Y-%m-%d")
        occupation = request.form["occupation"]

        form = Form(first_name=first_name, middle_name=middle_name,
                    last_name=last_name, email=email,
                    mobile=mobile, date=date_object, occupation=occupation)
        db.session.add(form)
        db.session.commit()

        message_body = f"Thank you for your submission, {first_name}." \
                       f"Here are your data:\n{first_name}\n{last_name}\n{date}\n"
        message = Message(subject="New Form submission",
                          sender=app.config["MAIL_USERNAME"],
                          recipients=[email],
                          body=message_body)
        mail.send(message)

        flash(f"{first_name}, Your form was submitted successfully!", "success")
    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)