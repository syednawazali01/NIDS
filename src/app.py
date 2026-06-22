#  Network Intrusion Detection System — Streamlit Frontend
#  College Mini Project 🎓
#  Run with:  streamlit run src/app.py


import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
import random
import sys
from datetime import datetime
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from scapy.all import sniff, IP, TCP, UDP, ICMP
    SCAPY_AVAILABLE = True
except:
    SCAPY_AVAILABLE = False

# Updated paths for new structure
BASE_DIR = Path(__file__).parent.parent
MODELS_DIR = BASE_DIR / "models"
DATA_DIR = BASE_DIR / "data"

st.set_page_config(
    page_title="NIDS | Network Intrusion Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main { background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 100%); }
    .stApp { background: transparent; }
    .title-text { font-size: 2rem; font-weight: 700; color: #00d4ff; }
    .subtitle-text { font-size: 1rem; color: #a0a0b0; margin-bottom: 20px; }
    .metric-card { background: linear-gradient(145deg, #1e1e30, #252540); padding: 15px; border-radius: 12px; border: 1px solid #3a3a5c; text-align: center; }
    .feature-card { background: #1a1a2e; padding: 10px 15px; border-radius: 8px; border-left: 3px solid #00d4ff; margin: 8px 0; }
    .success-box { background: linear-gradient(145deg, #0d3320, #0f3d2a); padding: 20px; border-radius: 12px; border: 2px solid #00ff88; margin: 15px 0; }
    .danger-box { background: linear-gradient(145deg, #3d0f0f, #4d1515); padding: 20px; border-radius: 12px; border: 2px solid #ff4444; margin: 15px 0; }
    .section-header { color: #00d4ff; font-size: 1.3rem; font-weight: 600; margin: 20px 0 15px 0; padding-bottom: 8px; border-bottom: 1px solid #3a3a5c; }
    .sidebar-section { background: #1a1a2e; padding: 12px; border-radius: 8px; margin: 8px 0; }
    div[data-testid="stMetric"] { background: linear-gradient(145deg, #1e1e30, #252540); padding: 10px; border-radius: 8px; border: 1px solid #3a3a5c; }
    div[data-testid="stMetricLabel"] { color: #a0a0b0 !important; font-size: 0.8rem; }
    div[data-testid="stMetricValue"] { color: #00d4ff !important; font-size: 1.2rem; }
    .stButton > button { background: linear-gradient(145deg, #00d4ff, #0099cc) !important; color: #0f0f23 !important; font-weight: 600 !important; border: none !important; border-radius: 8px !important; }
    .stButton > button:hover { background: linear-gradient(145deg, #00ffaa, #00d4ff) !important; }
    .home-hero { background: linear-gradient(145deg, #1a1a2e, #252540); padding: 20px; border-radius: 12px; border: 1px solid #3a3a5c; text-align: center; }
    .progress-bar { background: #1e1e30; border-radius: 8px; height: 12px; overflow: hidden; }
    .progress-fill { background: linear-gradient(90deg, #00d4ff, #00ff88); height: 100%; border-radius: 8px; }
    .stat-box { background: #1a1a2e; padding: 10px 15px; border-radius: 8px; border-left: 3px solid #00d4ff; margin: 8px 0; }
    .stExpander { background: #1a1a2e; border-radius: 10px; border: 1px solid #3a3a5c; }
    .stRadio > div { gap: 15px; }
    .stRadio > div > label { background: #1e1e30; padding: 8px 16px; border-radius: 8px; border: 1px solid #3a3a5c; }
    .stRadio > div > label:has(input:checked) { background: #00d4ff; color: #0f0f23; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_models():
    model = joblib.load(str(MODELS_DIR / "best_model.joblib"))
    scaler = joblib.load(str(MODELS_DIR / "scaler.joblib"))
    encoders = joblib.load(str(MODELS_DIR / "encoders.joblib"))
    features = joblib.load(str(MODELS_DIR / "feature_names.joblib"))
    return model, scaler, encoders, features

model, scaler, encoders, FEATURES = load_models()

def preprocess(input_dict):
    df = pd.DataFrame([input_dict])
    for col, le in encoders.items():
        val = str(df[col][0])
        df[col] = le.transform([val]) if val in le.classes_ else 0
    df = df[FEATURES]
    return scaler.transform(df)

def predict(input_dict):
    X = preprocess(input_dict)
    pred = model.predict(X)[0]
    try:
        prob = model.predict_proba(X)[0]
        confidence = round(max(prob) * 100, 1)
    except:
        confidence = 0.0
    return pred, confidence

# Dashboard content continues here...
st.markdown('<p class="title-text">🛡️ NIDS - Network Intrusion Detection</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">College Mini Project 🎓</p>', unsafe_allow_html=True)

st.info("💡 This is a college mini project demonstrating ML-based network security")
