import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="AI SOC Dashboard",
    page_icon="🚨",
    layout="wide"
)

# ------------------------
# LOAD FILES
# ------------------------

@st.cache_resource
def load_assets():
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    columns = joblib.load("columns.pkl")
    feature_importance = joblib.load("feature_importance.pkl")

    return model, scaler, columns, feature_importance

model, scaler, columns, feature_importance = load_assets()

# ------------------------
# SESSION STATE
# ------------------------

if "history" not in st.session_state:
    st.session_state.history = []

# ------------------------
# HEADER
# ------------------------

st.title("🚨 AI-Driven Security Operations Center")

st.markdown("""
### Network Intrusion Detection System

**Model:** Random Forest  
**Accuracy:** 99.90%  
**Dataset:** NSL-KDD
""")

# ------------------------
# KPI CARDS
# ------------------------

c1,c2,c3,c4 = st.columns(4)

c1.metric("Model", "Random Forest")
c2.metric("Accuracy", "99.90%")
c3.metric("Features", len(columns))
c4.metric("Status", "ACTIVE")

st.divider()

# ------------------------
# TABS
# ------------------------

tab1, tab2, tab3 = st.tabs(
    [
        "Threat Detection",
        "Analytics",
        "SOC Monitor"
    ]
)

# ==================================================
# TAB 1
# ==================================================

with tab1:

    st.subheader("Quick Threat Scan")

    col1,col2 = st.columns(2)

    src_bytes = col1.number_input(
        "Source Bytes",
        min_value=0.0,
        value=100.0
    )

    dst_bytes = col2.number_input(
        "Destination Bytes",
        min_value=0.0,
        value=200.0
    )

    if st.button("Analyze Threat"):

        row = pd.DataFrame(
            np.zeros((1,len(columns))),
            columns=columns
        )

        if "src_bytes" in row.columns:
            row["src_bytes"] = src_bytes

        if "dst_bytes" in row.columns:
            row["dst_bytes"] = dst_bytes

        scaled = scaler.transform(row)

        pred = model.predict(scaled)[0]

        prob = model.predict_proba(scaled)[0][1]

        if prob < 0.30:
            severity = "LOW"

        elif prob < 0.70:
            severity = "MEDIUM"

        else:
            severity = "HIGH"

        c1,c2 = st.columns(2)

        with c1:

            if pred == 1:
                st.error("⚠️ ATTACK DETECTED")
            else:
                st.success("✅ NORMAL TRAFFIC")

            st.metric(
                "Threat Score",
                f"{prob*100:.2f}%"
            )

            st.metric(
                "Severity",
                severity
            )

        with c2:

            gauge = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=prob*100,
                    title={"text":"Threat Level"}
                )
            )

            st.plotly_chart(
                gauge,
                use_container_width=True
            )

        st.session_state.history.append({

            "Time":
                datetime.now().strftime(
                    "%H:%M:%S"
                ),

            "Threat Score":
                round(prob*100,2),

            "Result":
                "Attack" if pred==1 else "Normal"
        })

# ==================================================
# TAB 2
# ==================================================

with tab2:

    st.subheader("Model Comparison")

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

    fig = px.bar(

        results,

        x="Model",

        y="Accuracy",

        text="Accuracy",

        title="ML Model Performance"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader(
        "Feature Importance"
    )

    fig2 = px.bar(

        feature_importance.head(15),

        x="Importance",

        y="Feature",

        orientation="h",

        title="Top 15 Important Features"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# ==================================================
# TAB 3
# ==================================================

with tab3:

    st.subheader(
        "SOC Alert Feed"
    )

    if len(
        st.session_state.history
    ) == 0:

        st.info(
            "No alerts generated yet."
        )

    else:

        history_df = pd.DataFrame(
            st.session_state.history
        )

        st.dataframe(
            history_df,
            use_container_width=True
        )

        pie = px.pie(

            history_df,

            names="Result",

            title="Attack Distribution"
        )

        st.plotly_chart(
            pie,
            use_container_width=True
        )

        trend = px.line(

            history_df,

            x="Time",

            y="Threat Score",

            markers=True,

            title="Threat Trend"
        )

        st.plotly_chart(
            trend,
            use_container_width=True
        )

st.divider()

st.success(
    "AI-Driven Network Intrusion Detection & SOC Dashboard"
)
