import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import os

from styles import load_css
from train_model import train_model

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="AI Cricket Player Performance Predictor",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(load_css(), unsafe_allow_html=True)

# =====================================================
# LOAD MODEL
# =====================================================

@st.cache_resource
def load_model():

    if not os.path.exists("cricket_predictor.pkl"):

        st.info("⚙️ Model not found. Training AI model... Please wait.")

        train_model()

        st.success("✅ Model trained successfully!")

    return joblib.load("cricket_predictor.pkl")


model = load_model()

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():
    deliveries = pd.read_csv("data/deliveries.csv")
    matches = pd.read_csv("data/matches.csv")
    features = pd.read_csv("features.csv")

    return deliveries, matches, features

deliveries, matches, features = load_data()

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🏏 AI Cricket Predictor")

st.sidebar.markdown("---")

st.sidebar.info("""
### Project Details

**Project**
AI Cricket Player Performance Prediction

**Algorithm**
Random Forest Regressor

**Dataset**
IPL Ball-by-Ball Dataset

**Machine Learning**
Scikit-Learn

**Evaluation**
MAE : 3.48 Runs
""")

st.sidebar.markdown("---")

st.sidebar.success("✅ Model Loaded Successfully")

st.sidebar.markdown("---")

st.sidebar.write("Developed By")
st.sidebar.write("**Vetri**")
st.sidebar.write("Artificial Intelligence & Data Science")

# =====================================================
# TITLE
# =====================================================

st.title("🏏 AI Cricket Player Performance Prediction Dashboard")

st.markdown("""
Predict a batter's expected score using Machine Learning trained on IPL historical data.
""")

st.divider()

# =====================================================
# PLAYER SELECTION
# =====================================================

players = sorted(features["batter"].unique())

teams = sorted(deliveries["bowling_team"].unique())

col1, col2 = st.columns(2)

with col1:
    player = st.selectbox(
        "👤 Select Batter",
        players
    )

with col2:
    opponent = st.selectbox(
        "🛡️ Select Opponent Team",
        teams
    )

predict_btn = st.button(
    "🚀 Predict Performance",
    use_container_width=True
)

# =====================================================
# AI PREDICTION
# =====================================================

if predict_btn:

    player_features = features[
        features["batter"] == player
    ]

    if player_features.empty:

        st.error("Player not found!")

        st.stop()

    latest = player_features.iloc[-1]

    career_avg = float(latest["Career_Avg"])
    last5_avg = float(latest["Last5_Avg"])
    strike_rate = float(latest["Strike Rate"])

    model_fours = int(latest["Fours"])
    model_sixes = int(latest["Sixes"])

    X = [[
        career_avg,
        last5_avg,
        strike_rate,
        model_fours,
        model_sixes
    ]]

    prediction = model.predict(X)[0]

    # =====================================================
    # CAREER STATS FROM DELIVERIES
    # =====================================================

    player_ball_data = deliveries[
        deliveries["batter"] == player
    ]

    career_runs = int(player_ball_data["batsman_runs"].sum())

    career_balls = len(player_ball_data)

    career_fours = int(
        (player_ball_data["batsman_runs"] == 4).sum()
    )

    career_sixes = int(
        (player_ball_data["batsman_runs"] == 6).sum()
    )

    dismissals = int(
        (player_ball_data["player_dismissed"] == player).sum()
    )

    if dismissals > 0:
        batting_average = round(
            career_runs / dismissals,
            2
        )
    else:
        batting_average = career_runs

    strike_rate_actual = round(
        (career_runs / career_balls) * 100,
        2
    )

    st.success("✅ Prediction Generated Successfully")
        # =====================================================
    # AI PREDICTION DASHBOARD
    # =====================================================

    st.divider()

    st.header("🤖 AI Prediction")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Career Average",
        f"{career_avg:.2f}"
    )

    col2.metric(
        "Last 5 Match Average",
        f"{last5_avg:.2f}"
    )

    col3.metric(
        "Predicted Runs",
        f"{round(prediction)}"
    )

    st.divider()

    col4, col5, col6 = st.columns(3)

    col4.metric(
        "Career Runs",
        career_runs
    )

    col5.metric(
        "Career Strike Rate",
        strike_rate_actual
    )

    col6.metric(
        "Batting Average",
        batting_average
    )

    st.divider()

    col7, col8, col9 = st.columns(3)

    col7.metric(
        "Career 4️⃣",
        career_fours
    )

    col8.metric(
        "Career 6️⃣",
        career_sixes
    )

    col9.metric(
        "Balls Faced",
        career_balls
    )

    # =====================================================
    # PERFORMANCE RATING
    # =====================================================

    if prediction >= 70:
        stars = "⭐⭐⭐⭐⭐"
        status = "Excellent 🔥"

    elif prediction >= 50:
        stars = "⭐⭐⭐⭐"
        status = "Very Good 💪"

    elif prediction >= 30:
        stars = "⭐⭐⭐"
        status = "Good 👍"

    elif prediction >= 15:
        stars = "⭐⭐"
        status = "Average"

    else:
        stars = "⭐"
        status = "Needs Improvement"

    st.divider()

    st.subheader("🏆 AI Performance Rating")

    left, right = st.columns([1, 2])

    with left:

        st.markdown(f"# {stars}")

    with right:

        st.success(f"Current Form : {status}")

        st.info(f"Expected Runs : {round(prediction)}")

        st.write(
            """
The prediction is based on:

- Career Average
- Recent Form
- Strike Rate
- Boundary Count
- Historical IPL Performance
"""
        )
            # =====================================================
    # RECENT FORM
    # =====================================================

    st.divider()

    st.header("📈 Recent Form Analysis")

    recent_matches = player_features.tail(5).copy()

    if not recent_matches.empty:

        recent_matches = recent_matches.reset_index(drop=True)
        recent_matches.index = recent_matches.index + 1

        st.subheader("Last 5 Innings")

        display_df = recent_matches[
            [
                "Runs",
                "Career_Avg",
                "Last5_Avg",
                "Strike Rate",
                "Fours",
                "Sixes"
            ]
        ]

        st.dataframe(display_df, use_container_width=True)

        st.subheader("Runs in Last 5 Matches")

        chart_df = pd.DataFrame({
            "Match": [1, 2, 3, 4, 5][:len(recent_matches)],
            "Runs": recent_matches["Runs"].values
        })

        st.line_chart(chart_df.set_index("Match"))

    # =====================================================
    # PLAYER PERFORMANCE CHART
    # =====================================================

    st.divider()

    st.header("📊 Player Performance Overview")

    fig, ax = plt.subplots(figsize=(8, 4))

    labels = [
        "Career Avg",
        "Last 5 Avg",
        "Strike Rate",
        "Predicted Runs"
    ]

    values = [
        career_avg,
        last5_avg,
        strike_rate_actual,
        round(prediction)
    ]

    ax.bar(labels, values)

    ax.set_ylabel("Value")
    ax.set_title(f"{player} Performance")

    st.pyplot(fig)

    # =====================================================
    # MATCH SUMMARY
    # =====================================================

    st.divider()

    st.subheader("📋 AI Match Summary")

    st.success(f"""
**Player:** {player}

**Opponent:** {opponent}

**Predicted Runs:** {round(prediction)}

**Current Form:** {status}

**Career Average:** {career_avg:.2f}

**Career Strike Rate:** {strike_rate_actual:.2f}
""")
        # =====================================================
    # BATTER VS BOWLER ANALYSIS
    # =====================================================

    st.divider()

    st.header(f"🎯 {player} vs Bowlers of {opponent}")

    opponent_match_ids = matches[
        (matches["team1"] == opponent) |
        (matches["team2"] == opponent)
    ]["id"]

    vs_team = deliveries[
        (deliveries["match_id"].isin(opponent_match_ids)) &
        (deliveries["batter"] == player)
    ]

    if vs_team.empty:

        st.warning(
            f"No historical data available for {player} against {opponent}."
        )

    else:

        bowler_stats = (
            vs_team.groupby("bowler")
            .agg(
                Runs=("batsman_runs", "sum"),
                Balls=("ball", "count"),
                Outs=("player_dismissed",
                      lambda x: (x == player).sum())
            )
            .reset_index()
        )

        bowler_stats["Strike Rate"] = (
            bowler_stats["Runs"] /
            bowler_stats["Balls"] * 100
        ).round(2)

        bowler_stats = bowler_stats.sort_values(
            "Runs",
            ascending=False
        )

        st.dataframe(
            bowler_stats,
            use_container_width=True
        )

        best_bowler = bowler_stats.sort_values(
            "Outs",
            ascending=False
        ).iloc[0]

        st.info(
            f"🎯 Most Successful Bowler against {player}: "
            f"**{best_bowler['bowler']}** "
            f"({int(best_bowler['Outs'])} dismissals)"
        )

    # =====================================================
    # DASHBOARD SUMMARY
    # =====================================================

    st.divider()

    st.header("📊 Dashboard Summary")

    summary1, summary2, summary3, summary4 = st.columns(4)

    summary1.metric(
        "Predicted Runs",
        round(prediction)
    )

    summary2.metric(
        "Career Runs",
        career_runs
    )

    summary3.metric(
        "Career 100s",
        int((player_features["Runs"] >= 100).sum())
    )

    summary4.metric(
        "Career 50s",
        int(
            (
                (player_features["Runs"] >= 50) &
                (player_features["Runs"] < 100)
            ).sum()
        )
    )

    st.divider()

    st.success("✅ Prediction completed successfully!")