from flask import Flask, render_template, request

app = Flask(__name__)


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


app.run(debug=True, port=5001)