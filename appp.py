from flask import Flask, request, render_template
import pickle
import os
import speech_recognition as sr

# Initialize Flask app
app = Flask(__name__)

# Load saved models
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("nb_model.pkl", "rb") as f:
    nb_model = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

# Define label mapping
label_mapping = {
    0: "Mild/Moderate Depression or Emotional Struggle",
    1: "Severe Depression or Suicidal Ideation",
    2: "Mixed/Supportive or Ambiguous Emotional State"
}

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Predict route
@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return "⚠️ No file uploaded"

    file = request.files["file"]

    if file.filename == "":
        return "⚠️ No selected file"

    if file:
        # Save uploaded file temporarily
        filepath = os.path.join("uploads", file.filename)
        os.makedirs("uploads", exist_ok=True)
        file.save(filepath)

        # Convert audio to text
        recognizer = sr.Recognizer()
        try:
            with sr.AudioFile(filepath) as source:
                audio = recognizer.record(source)
                text = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "❌ Could not understand audio"
        except sr.RequestError as e:
            return f"❌ Could not request results; {e}"

        # Transform text
        sample_tfidf = vectorizer.transform([text])
        sample_pred = nb_model.predict(sample_tfidf)
        predicted_label = encoder.inverse_transform(sample_pred)[0]
        
        # Map numerical label to descriptive text
        descriptive_label = label_mapping.get(int(predicted_label), "Unknown Label")

        return render_template("index.html", transcript=text, prediction=descriptive_label)

if __name__ == "__main__":
    app.run(debug=True)