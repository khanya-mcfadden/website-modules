@app.route("/")



app = Flask(__name__)
app.secret_key = "1mads"

@app.route("/Ai_data", methods=["POST"])
def get_Ai():
    import google.generativeai as genai
    from flask import request, jsonify

    genai.configure(api_key="AIzaSyCVadfEkISEXbfrKKWoXBgz2sCbFxMjLPY")

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

    data = request.get_json()
    question = data.get("question")

    response = chat.send_message(question)
    response_text = response.text

    # Function to check if the response is related to weather or health
    def is_relevant_response(response):
        animal_keywords = [
            "health",
            
        ]
        return any(keyword in response.lower() for keyword in animal_keywords)

    # Filter the response
    if is_relevant_response(response_text):
        return jsonify(
            {
                "response1": response_text,
            }
        )
    else:
        return jsonify(
            {
                "response1": "Sorry, I can only talk about weather or health.",
                "response2": "",
            }
        )