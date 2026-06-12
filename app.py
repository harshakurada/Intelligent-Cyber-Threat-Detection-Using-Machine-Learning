import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="AI SOC Dashboard",
    page_icon="🚨",
    layout="wide"
)

# =========================
# LOAD FILES
# =========================

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")
feature_importance = joblib.load("feature_importance.pkl")

# =========================
# HEADER
# =========================

st.title("🚨 AI Driven Network Intrusion Detection & SOC Dashboard")

st.markdown("""
### Enterprise Security Operations Center

Machine Learning Based Intrusion Detection System
using NSL-KDD Dataset
""")

# =========================
# KPI CARDS
# =========================

col1,col2,col3,col4 = st.columns(4)

col1.metric("Model", "Random Forest")
col2.metric("Accuracy", "99.90%")
col3.metric("Features", len(columns))
col4.metric("Status", "ACTIVE")

st.divider()

# =========================
# SIDEBAR
# =========================

st.sidebar.header("Prediction Panel")

selected_features = feature_importance.head(10)["Feature"].tolist()

user_input = {}

for feature in selected_features:

    user_input[feature] = st.sidebar.number_input(
        feature,
        value=0.0
    )

# =========================
# SINGLE PREDICTION
# =========================

st.subheader("🔍 Real-Time Threat Detection")

if st.sidebar.button("Analyze Threat"):

    row = pd.DataFrame(
        np.zeros((1,len(columns))),
        columns=columns
    )

    for feature,value in user_input.items():
        row[feature] = value

    scaled = scaler.transform(row)

    pred = model.predict(scaled)[0]

    prob = model.predict_proba(scaled)[0][1]

    c1,c2 = st.columns(2)

    with c1:

        if pred == 1:
            st.error("⚠️ ATTACK DETECTED")
        else:
            st.success("✅ NORMAL TRAFFIC")

        st.metric(
            "Threat Probability",
            f"{prob*100:.2f}%"
        )

    with c2:

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=prob*100,
                title={"text":"Threat Score"}
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# =========================
# CSV ANALYZER
# =========================

st.divider()

st.subheader("📂 Bulk Traffic Analyzer")

uploaded_file = st.file_uploader(
    "Upload Network Traffic CSV",
    type=["csv"]
)

if uploaded_file is not None:

    test_df = pd.read_csv(uploaded_file)

    st.write("Preview")

    st.dataframe(
        test_df.head()
    )

    if st.button("Scan CSV"):

        try:

            test_df = test_df[columns]

            scaled = scaler.transform(test_df)

            preds = model.predict(scaled)

            test_df["Prediction"] = preds

            attacks = int(
                (preds==1).sum()
            )

            normals = int(
                (preds==0).sum()
            )

            c1,c2,c3 = st.columns(3)

            c1.metric(
                "Total Records",
                len(test_df)
            )

            c2.metric(
                "Attacks",
                attacks
            )

            c3.metric(
                "Normal",
                normals
            )

            fig = px.pie(
                names=["Normal","Attack"],
                values=[normals,attacks],
                title="Traffic Distribution"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.dataframe(
                test_df.head(20)
            )

        except Exception as e:
            st.error(str(e))

# =========================
# FEATURE IMPORTANCE
# =========================

st.divider()

st.subheader("📊 Top Features")

fig = px.bar(
    feature_importance.head(15),
    x="Importance",
    y="Feature",
    orientation="h"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# MODEL COMPARISON
# =========================

st.divider()

st.subheader("🤖 Model Comparison")

results = pd.DataFrame({

    "Model":[
        "Random Forest",
        "Decision Tree",
        "Gradient Boosting",
        "Logistic Regression"
    ],

    "Accuracy":[
        99.90,
        99.85,
        99.62,
        97.23
    ]
})

fig2 = px.bar(
    results,
    x="Model",
    y="Accuracy",
    text="Accuracy"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =========================
# FOOTER
# =========================

st.divider()

st.success(
    "AI Driven Network Intrusion Detection & SOC Dashboard"
)
