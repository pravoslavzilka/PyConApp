from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def splash_screen():
        return render_template("login_screen.html")


@app.route("/get-login-info", methods=["POST"])
def login_proceed():
    # email = request.form["email-address"]
    # password = request.form["password"]

    return render_template("continue_login.html")


@app.route("/menu")
def online_main_page():
    return render_template("online_splash_page.html")


@app.route("/navigation")
def offline_main_page():
    return render_template("offline_splash_page.html")


@app.route("/map")
def map_page():
    return render_template("map_page.html")


@app.route("/workshops")
def workshop_page():
    return render_template("workshops_page.html")


@app.route("/lectures")
def lecture_page():
    return render_template("lectures_page.html")


@app.route("/forum")
def forum_page():
    return render_template("forum_page.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")