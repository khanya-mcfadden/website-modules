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




@app.route("/Ai_data", methods=["POST"])
def get_Ai():


    genai.configure(api_key="AIzaSyDC8TaqSgpDw2Emfkd7-1njplpLgd5dRxI")

    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": "Hello"},
            {
                "role": "model",
                "parts": "Great to meet you. What would you like to know?",
            },
        ]
    )

    # ai-question = request.form["ai-question"]

    data = request.get_json()
    question = data.get("question")

    response = chat.send_message(question)
    response_text = response.text

    # Function to check if the response is related to weather or health
    def is_relevant_response(response):
        animal_keywords = [
            "animal",
            "pet",
            "dog",  
            "cat",
            "bird",
            "fish",
            "reptile",
            "mammal",
            "insect",
            "wildlife",
            "zoo",
            "aquarium",
            "vet",
            "veterinarian",
            "animal shelter",
            "animal rescue",
            "animal welfare",
            "animal rights",
            "animal protection",
            "animal conservation",
            "animal behavior",
            "animal training",
            "animal care",
            "animal nutrition",
            "animal health",
            "animal diseases",
            "animal medicine",
            "animal surgery",
            "animal reproduction",
            "health",
            
        ]
        return any(keyword in response.lower() for keyword in animal_keywords)

    # Filter the response
    if is_relevant_response(response_text):
        # Check if the question specifies a longer response
        if "detailed" in question.lower() or "long" in question.lower():
            return jsonify(
                {
                    "response1": response_text,
                }
            )
        else:
            # Return a few short sentences
            short_response = " ".join(response_text.split(".")[:5]) + "."
            return jsonify(
                {
                    "response1": short_response,
                    "note": "As I am an AI, I can be wrong and you should always check trusted and well-known sources.",
                }
            )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")