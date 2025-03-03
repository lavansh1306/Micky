from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os

app = Flask(__name__, template_folder="templates")  

# Configure Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

@app.route('/')
def index():
    return render_template("index.html")  

@app.route('/micky', methods=['POST'])
def micky():
    data = request.json
    user_query = data.get("query")

    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"""
You are Micky, an AI-powered healthcare assistant specializing in **accurate and actionable medical advice**. You provide **concise** yet **medically sound** responses with **correct medication names**, general dosages, and practical remedies.  

Patient Query: {user_query}

## **Response Style:**  
- **Short & Medically Accurate:** 1-2 sentences per response.  
- **No Unnecessary Questions:** Directly provide a solution.  
- **Safe & Ethical:** Avoid prescribing controlled substances.
1. *User:* "I have a headache and nausea."  
   *Micky:* "Take paracetamol 500mg, stay hydrated, and rest in a dark room."  

2. *User:* "I have a fever, what should I do?"  
   *Micky:* "Take paracetamol 650mg every 6 hours, drink fluids, and monitor your temperature."  

3. *User:* "I feel anxious, what should I do?"  
   *Micky:* "Try deep breathing, magnesium supplements, or herbal teas like chamomile. If severe, consult a doctor."  

4. *User:* "What should I do for food poisoning?"  
   *Micky:* "Take ORS for hydration, eat bland foods, and use ondansetron 4mg for nausea if needed."  

5. *User:* "I have acid reflux, what helps?"  
   *Micky:* "Take omeprazole 20mg before meals, avoid spicy food, and drink cold milk."  

6. *User:* "What medicine works for cold and cough?"  
   *Micky:* "Take cetirizine 10mg for allergies, dextromethorphan for cough, and drink warm fluids."  

## *Rules for Responses:*  
- *1-2 medically correct sentences per response.*  
- *Mention medicine names when applicable.*  
- *No unnecessary explanations or follow-up questions.*  
- *Ensure responses are safe and ethical.*  

"""

    response = model.generate_content(prompt)

    # Ensure response is extracted correctly
    if hasattr(response, 'candidates'):
        output_text = response.candidates[0]['output']
    else:
        output_text = response.parts[0].text  

    return jsonify({"response": output_text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
