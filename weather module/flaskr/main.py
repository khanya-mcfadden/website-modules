from flask import (
    Flask,
    request,
    jsonify,
    render_template,
)
import google.generativeai as genai


app = Flask(__name__)
app.secret_key = "1mads"



@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/weather_page")
# def weather_page():
#     return render_template("weather_page.html")


@app.route("/weather_data")
def get_weather_data():
    api_key = "0f98d01acd0e41818d8124023242111"
    location = request.args.get(
        "location", "horsham"
    )  # Get location from query params, default to horsham
    url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days=4&aqi=no"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the status is 4xx, 5xx
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch weather data", "details": str(e)})




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")