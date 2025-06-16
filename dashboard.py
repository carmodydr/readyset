import streamlit as st
import requests
import pandas as pd

# --- PAGE SETUP ---
st.set_page_config(page_title="ReadySet - Disaster Prep Dashboard", layout="wide")
st.title("🏠 ReadySet: Personalized Disaster Prep Dashboard")
st.markdown("Get a personalized emergency plan based on your location and household.")

# --- USER INPUT FORM ---
st.sidebar.header("Household Profile")
with st.sidebar.form("user_profile"):
    zip_code = st.text_input("Zip Code", max_chars=5)
    adults = st.number_input("Number of Adults", min_value=1, max_value=10, value=2)
    kids = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
    pets = st.selectbox("Any Pets?", ["No", "Yes"])
    housing = st.selectbox("Housing Type", ["House", "Apartment", "Mobile Home"])
    car_access = st.selectbox("Access to a Vehicle?", ["Yes", "No"])
    submitted = st.form_submit_button("Generate Plan")

# --- PLACEHOLDER OUTPUT ---
if submitted:
    st.subheader("📍 Local Hazard Summary")
    st.markdown(f"**Location:** {zip_code}")

    # Simulated API response (to be replaced with real data pipeline)
    hazard_summary = {
        "Flood Risk": "Moderate",
        "Power Outage History": "Frequent (avg. 2 outages/year)",
        "Heat Risk": "High",
        "Wildfire Risk": "Low",
    }

    df_summary = pd.DataFrame(list(hazard_summary.items()), columns=["Hazard", "Level"])
    st.table(df_summary)

    st.subheader("✅ Recommended Preparedness Actions")
    st.markdown("Generating your customized checklist...")

    # Placeholder checklist generation
    checklist = [
        "Store 14 gallons of water (1 gallon/person/day for 1 week)",
        "Keep battery banks charged",
        "Create go-bags for each household member",
        "Plan alternate communication methods",
        "Maintain a full gas tank during hurricane season",
    ]

    for item in checklist:
        st.checkbox(item, value=False)

    st.markdown("---")
    st.markdown("*This is an MVP prototype. Data shown is placeholder only.*")

