from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get data from form
        eye_blink_rate = float(request.form["eye_blink_rate"])
        steering_variation = float(request.form["steering_variation"])
        hours_driven = float(request.form["hours_driven"])
        heart_rate = float(request.form["heart_rate"])
        caffeine_intake = float(request.form["caffeine_intake"])

        # Prepare input
        features = np.array([[eye_blink_rate, steering_variation, hours_driven, heart_rate, caffeine_intake]])

        # Prediction
        prediction = model.predict(features)[0]

        if prediction == 1:
            result = "Drowsy Driver – Please take a break!"
        else:
            result = "Alert Driver – Keep driving safely."

        return render_template("index.html", prediction=result)

    except Exception as e:
        return render_template("index.html", prediction="Error: " + str(e))

if __name__ == "__main__":
    app.run(debug=True)
