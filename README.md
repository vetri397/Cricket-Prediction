# 🏏 AI Cricket Player Performance Prediction System

An AI-powered web application that predicts a batter's expected runs in an IPL match using Machine Learning and historical IPL ball-by-ball data.

Built using **Python**, **Scikit-learn**, **Pandas**, and **Streamlit**.

---

## 📌 Project Overview

The AI Cricket Player Performance Prediction System analyzes a player's historical IPL performance and predicts the expected number of runs they may score.

The prediction is based on:

- Career Batting Average
- Recent Form (Last 5 Matches)
- Strike Rate
- Number of Fours
- Number of Sixes

The project also provides player statistics, recent performance trends, and batter vs bowler analysis through an interactive dashboard.

---

## 🚀 Features

- 🤖 Machine Learning-based run prediction
- 📊 Career statistics dashboard
- 📈 Recent form analysis
- 🎯 Batter vs Bowler analysis
- ⭐ AI performance rating
- 📋 Match summary
- 🏏 Interactive Streamlit web interface
- 📉 Performance visualization using charts

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Matplotlib
- Streamlit

### Machine Learning Algorithm
- Random Forest Regressor

### Dataset
- IPL Ball-by-Ball Dataset (Kaggle)

---

## 📂 Project Structure

```
CricketPlayerPrediction/
│
├── data/
│   ├── deliveries.csv
│   └── matches.csv
│
├── app.py
├── train_model.py
├── predict.py
├── feature_engineering.py
├── prepare_dataset.py
├── player_stats.py
├── recent_form.py
├── bowler_analysis.py
├── team_analysis.py
├── create_bowler_features.py
├── check_dataset.py
├── check_features.py
├── styles.py
├── charts.py
├── utils.py
├── features.csv
├── batter_vs_bowler.csv
├── player_match_stats.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Machine Learning Workflow

1. Load IPL datasets
2. Perform feature engineering
3. Generate player statistics
4. Calculate career average
5. Calculate last five match average
6. Train Random Forest Regressor
7. Evaluate using Mean Absolute Error (MAE)
8. Predict expected runs
9. Display results using Streamlit

---

## 📊 Features Used for Prediction

- Career Average
- Last 5 Match Average
- Strike Rate
- Number of Fours
- Number of Sixes

---

## 📈 Model Performance

**Algorithm:** Random Forest Regressor

**Evaluation Metric:** Mean Absolute Error (MAE)

**MAE:** **3.48 Runs**

---

## 📷 Application Dashboard

The dashboard includes:

- AI Prediction
- Career Statistics
- Recent Form
- Performance Charts
- Batter vs Bowler Analysis
- Match Summary
- AI Performance Rating

*(Add screenshots here after deployment.)*

Example:

```
screenshots/home.png
screenshots/prediction.png
screenshots/bowler_analysis.png
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/vetri397/Cricket-Prediction.git
```

Move into the project directory

```bash
cd Cricket-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📊 Dataset

The project uses the IPL Ball-by-Ball dataset containing:

- Match information
- Ball-by-ball deliveries
- Batting statistics
- Bowling statistics
- Match results

---

## 🎯 Future Improvements

- Deep Learning (LSTM) prediction model
- Venue-wise performance analysis
- Weather-based prediction
- Live IPL API integration
- Team winning probability prediction
- Fantasy Cricket player recommendation
- Interactive analytics dashboard
- Player comparison module

---

## 👨‍💻 Developed By

**Vetri**

**Department:** Artificial Intelligence & Data Science

---

## 📄 License

This project is developed for educational and learning purposes.

---

## ⭐ If you like this project

Please consider giving this repository a ⭐ on GitHub.
