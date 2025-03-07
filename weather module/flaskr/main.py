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





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")