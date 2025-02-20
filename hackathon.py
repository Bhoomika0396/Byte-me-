pip install flask
from flask import Flask, request, jsonify

app = Flask(__name__)

class MediGuideChatbot:
    def __init__(self):
        self.symptom_database = {
            "fever": "Monitor your temperature. If it exceeds 102°F or persists for more than 3 days, consult a doctor.",
            "cough": "A mild cough may indicate a cold, but if it persists for more than 2 weeks, seek medical advice.",
            "chest pain": "This could be serious. Seek immediate medical attention.",
            "shortness of breath": "This might indicate a respiratory issue. Call emergency services if severe.",
            "headache": "Mild headaches are common, but if severe or with vision problems, consult a physician.",
            "nausea": "If accompanied by vomiting or dehydration, seek medical care.",
            "fatigue": "Ensure you get enough rest. Persistent fatigue could indicate an underlying condition.",
            "sore throat": "Gargle with warm salt water and stay hydrated. If it lasts more than a week, consult a doctor.",
            "runny nose": "Likely a cold or allergies. Use antihistamines if needed.",
            "muscle pain": "Rest and stay hydrated. If severe or persistent, see a doctor.",
            "dizziness": "If frequent or severe, it could indicate an inner ear issue or low blood pressure. Seek medical attention.",
            "diarrhea": "Stay hydrated. If it lasts more than 3 days or contains blood, consult a doctor.",
            "vomiting": "Hydrate well. Seek medical care if persistent or accompanied by severe pain.",
            "rash": "Could be an allergic reaction or infection. If spreading or painful, consult a doctor.",
            "joint pain": "Apply ice or heat. If swelling or stiffness persists, consult a physician.",
        }

    def get_symptom_advice(self, symptom):
        symptom = symptom.lower()
        return self.symptom_database.get(symptom, "I'm not certain about that symptom. Please consult a healthcare provider for accurate guidance.")

    def risk_assessment(self, symptoms):
        high_risk_symptoms = ["chest pain", "shortness of breath", "vomiting", "severe dizziness"]
        moderate_risk_symptoms = ["fever", "cough", "headache", "nausea", "fatigue", "muscle pain", "joint pain", "diarrhea"]

        risk_level = "Low Risk"
        for symptom in symptoms:
            if symptom.lower() in high_risk_symptoms:
                risk_level = "High Risk"
                break
            elif symptom.lower() in moderate_risk_symptoms:
                risk_level = "Moderate Risk"

        return risk_level

# Instantiate the chatbot
chatbot = MediGuideChatbot()

@app.route('/check_symptoms', methods=['POST'])
def check_symptoms():
    data = request.get_json()
    symptoms = data.get("symptoms", [])

    if not symptoms or not isinstance(symptoms, list):
        return jsonify({"error": "Please provide a list of symptoms."}), 400

    results = {}
    for symptom in symptoms:
        results[symptom] = chatbot.get_symptom_advice(symptom)

    risk = chatbot.risk_assessment(symptoms)

    return jsonify({
        "advice": results,
        "risk_level": risk,
        "message": "Seek immediate medical attention." if risk == "High Risk" else 
                   "Monitor symptoms closely and consult a doctor if they persist or worsen." if risk == "Moderate Risk" else 
                   "Your symptoms seem mild, but stay mindful and take care!"
    })

if __name__ == '__main__':
    app.run(debug=True)
python mediguide_api.py
curl -X POST http://127.0.0.1:5000/check_symptoms -H "Content-Type: application/json" -d '{"symptoms": ["fever", "cough", "chest pain"]}'
import requests

url = "http://127.0.0.1:5000/check_symptoms"
data = {"symptoms": ["fever", "cough", "chest pain"]}

response = requests.post(url, json=data)
print(response.json())
{
    "advice": {
        "fever": "Monitor your temperature. If it exceeds 102°F or persists for more than 3 days, consult a doctor.",
        "cough": "A mild cough may indicate a cold, but if it persists for more than 2 weeks, seek medical advice.",
        "chest pain": "This could be serious. Seek immediate medical attention."
    },
    "risk_level": "High Risk",
    "message": "Seek immediate medical attention."
}



#HTML CODE

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MediGuide Chatbot</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="chat-container">
        <h2>MediGuide Chatbot</h2>
        <div id="chat-box">
            <p class="bot-message">Hi, I'm MediGuide! What symptoms are you experiencing?</p>
        </div>
        <input type="text" id="user-input" placeholder="Enter symptoms separated by commas...">
        <button onclick="processSymptoms()">Check Symptoms</button>
    </div>

    <script src="script.js"></script>
</body>
</html>



#CSS

body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.chat-container {
    width: 400px;
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
}

h2 {
    color: #2c3e50;
}

#chat-box {
    height: 200px;
    overflow-y: auto;
    border: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 10px;
    background: #f9f9f9;
    border-radius: 5px;
    text-align: left;
}

.bot-message {
    background: #dff0d8;
    padding: 8px;
    border-radius: 5px;
    margin: 5px 0;
}

.user-message {
    background: #d9edf7;
    padding: 8px;
    border-radius: 5px;
    margin: 5px 0;
    text-align: right;
}

input {
    width: 80%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    background: #27ae60;
    color: white;
    border: none;
    padding: 8px 15px;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 10px;
}

button:hover {
    background: #219150;
}


