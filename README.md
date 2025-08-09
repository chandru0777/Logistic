##  Drowsiness Detection Prediction System
A machine learning web application built with Logistic Regression and Flask that predicts whether a person is Drowsy or Alert based on factors such as study hours, sleep hours, previous scores, and distraction levels.

## Features
Predicts drowsiness risk using Logistic Regression

User-friendly web interface for data input

Responsive design with modern CSS styling

Lightweight Flask backend for fast performance

Works entirely locally or can be deployed online

## Dataset
The dataset (data.csv) contains 30 samples with the following columns:

## Column Name	Description
```
study_hours	Number of hours spent studying per day
sleep_hours	Average daily sleep hours
previous_score	Previous exam/test score (%)
distraction_level	Scale 1–10 (1 = focused, 10 = highly distracted)
status	Target variable — 1 (Alert) or 0 (Drowsy)
```
## Project Structure
```
 DrowsinessDetection
│── app.py                # Flask application
│── model.pkl             # Trained Logistic Regression model
│── data.csv              # Dataset with 30 samples
│── requirements.txt      # Dependencies
│
├──  templates
│   └── index.html        # Main HTML page
│
├──  static
│   └── style.css         # Styling for the app
│
└── README.md             # Project documentation
```
## Installation & Setup
## 1️ Clone the repository
```
git clone https://github.com/your-username/DrowsinessDetection.git
cd DrowsinessDetection
```

## 2 Install dependencies
```
pip install -r requirements.txt
```
## 4️ Run the Flask app
```
python app.py
```
## 5️ Access the app
Open your browser and go to:
```
http://127.0.0.1:5000
```
## Dependencies
Flask — Web framework

pandas — Data handling

scikit-learn — Machine learning

joblib — Model saving/loading

## Install all dependencies:
```
pip install flask pandas scikit-learn joblib
```
## Model Training
```
The Logistic Regression model is trained on data.csv and saved as model.pkl using joblib.
```
# Steps:

Load dataset

Split into training and testing sets

Train Logistic Regression model

Save trained model


## Screenshots
![alt text](<Screenshot 2025-08-09 113040.png>)
![alt text](<Screenshot 2025-08-09 113103.png>)
![alt text](<Screenshot 2025-08-09 113119.png>)