from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/rooms")
def rooms():
    return render_template("rooms.html")


@app.route("/book")
def book():
    return render_template("book.html")


@app.route("/bookings")
def bookings():
    return render_template("bookings.html")


if __name__ == "__main__":
    app.run(debug=True)