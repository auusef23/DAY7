from flask import Flask , request

app = Flask(__name__)


@app.route("/weather")
def weather():
    city = request.args["city"]
    return f"Sunny in {city}"