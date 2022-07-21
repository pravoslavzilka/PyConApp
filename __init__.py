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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")