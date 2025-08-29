🎙️ Intelligent Mental Health Assessment

🧠 Predicting Depression Levels from Speech (Real-Time Web App)






📌 Overview

Depression is one of the leading mental health challenges worldwide, but many people avoid diagnosis due to stigma, lack of resources, or late detection.
This project provides an AI-powered intelligent mental health assessment tool that predicts depression severity from speech in real time.

🎤 User uploads an audio file (speech).

📝 The app converts speech → text using Google Speech Recognition.

🤖 Machine Learning (Naive Bayes + TF-IDF) classifies the text into depression levels.

🌐 Accessible via a Flask-based web application.

🚀 Features

✅ Real-time speech-to-text analysis
✅ Depression level classification:
✅ User-friendly Flask web interface
✅ Scalable & ready for future deployment
✅ End-to-end pipeline (Audio → Text → ML Prediction)

🏗️ Project Architecture
🎤 Audio Input (WAV/MP3)
        ⬇
📝 Speech-to-Text (SpeechRecognition API)
        ⬇
🔠 Text Preprocessing (TF-IDF Vectorizer)
        ⬇
🤖 ML Model (Multinomial Naive Bayes)
        ⬇
📊 Depression Level Prediction
        ⬇
🌐 Flask Web App (User Interface)

📂 Dataset

We trained our model using CSV speech text datasets with 3 labels:

0 → Mild/Moderate Depression

1 → Severe Depression

2 → Mixed/Supportive/Ambiguous

Example Samples:

Label 0: "I’ve been feeling a bit down lately, nothing too serious."

Label 1: "Life seems pointless. I don’t see a way out of this darkness."

Label 2: "It’s tough, but I have good support, trying to stay positive."

⚙️ Tech Stack

Backend: Flask

ML Model: Naive Bayes (TF-IDF features)

Speech Recognition: Google SpeechRecognition (Python API)

Frontend: HTML + CSS (Flask Templates)

Serialization: Pickle (for model/vectorizer storage)

Upload an audio file and get instant depression analysis.

📊 Results

LSTM Model: ~64% accuracy

Naive Bayes Model: ~68% accuracy (selected for final app)

👉 Naive Bayes gave better performance on limited dataset.

🌟 Future Enhancements

🎶 Add audio-based features (tone, pitch, prosody) for richer predictions

📈 Improve accuracy with larger, more diverse datasets

☁️ Deploy on cloud (AWS/GCP/Heroku) for real-world access

📱 Extend to mobile app integration

💡 Why This Project Matters?

Helps in early screening of depression

Non-invasive, quick, and stigma-free assessment

Supports mental health professionals in early intervention

Real-time, accessible, and scalable solution for the future

🙌 Acknowledgements

Dataset contributors

Python libraries: Flask, scikit-learn, SpeechRecognition

Inspiration: Tackling mental health with AI

🧑‍💻 Author

👤 Muhammed Anshid
🔗 AI Engineer | ML Enthusiast | Passionate about AI for Social Good
