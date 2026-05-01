import streamlit as st
import pandas as pd
import pickle
import os

# ============================================
# PAGE SETUP
# ============================================
st.set_page_config(page_title="EV-Safety System", page_icon="🚗", layout="wide")

# ============================================
# LOAD MODEL (Simple tarika - bina sklearn import)
# ============================================
@st.cache_resource
def load_model():
    # Check current directory
    st.write(f"Current directory: {os.getcwd()}")
    st.write(f"Files found: {os.listdir('.')}")
    
    # Try to load
    try:
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        st.success("✅ Model loaded!")
        return model
    except FileNotFoundError:
        st.error("❌ model.pkl not found in current directory!")
        st.write("Files in directory:", os.listdir('.'))
        return None
    except Exception as e:
        st.error(f"❌ Error: {e}")
        return None

model = load_model()
# ============================================
# TITLE
# ============================================
st.title("🚗 EV-Safety System")
st.markdown("### ⚡ AI-Powered Predictive Maintenance")
st.markdown("---")

# ============================================
# SIDEBAR
# ============================================
st.sidebar.header("⚙️ Charger Parameters")
voltage = st.sidebar.slider("⚡ Voltage (V)", 180, 260, 230)
temperature = st.sidebar.slider("🌡️ Temperature (°C)", 10, 90, 40)
session = st.sidebar.slider("⏱️ Session Duration (min)", 0, 180, 35)
error = st.sidebar.selectbox("⚠️ Error Code", [0, 1, 2])
days = st.sidebar.slider("🔧 Days Since Maintenance", 0, 365, 30)
threshold = st.sidebar.slider("🎯 Risk Threshold (%)", 5, 50, 15)

# ============================================
# PREDICT
# ============================================
if st.button("🔍 Analyze Charger Health", use_container_width=True):
    
    if model is not None:
        input_data = pd.DataFrame([[voltage, temperature, session, error, days]],
                                  columns=['voltage', 'temperature', 'session_duration',
                                           'error_code', 'days_since_maintenance'])
        
        probability = model.predict_proba(input_data)[0][1] * 100
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if probability > threshold:
                st.error("### ❌ FAILURE PREDICTED!")
            else:
                st.success("### ✅ CHARGER IS HEALTHY")
            st.metric("Failure Probability", f"{probability:.1f}%")
        
        with col2:
            if probability > 70:
                st.markdown("### 🔴 CRITICAL RISK")
                st.markdown("🚨 Immediate action required!")
            elif probability > 40:
                st.markdown("### 🟡 WARNING")
                st.markdown("⚠️ Schedule maintenance soon")
            elif probability > 10:
                st.markdown("### 🟠 LOW RISK")
                st.markdown("👀 Monitor closely")
            else:
                st.markdown("### 🟢 SAFE")
                st.markdown("✅ No action needed")
        
        st.markdown("---")
        st.progress(min(int(probability), 100) / 100)
        st.caption(f"Risk: {probability:.1f}% (Threshold: {threshold}%)")
    
    else:
        st.error("Model not loaded!")

else:
    st.info("👈 Adjust parameters and click **Analyze Charger Health**")

# Footer
st.markdown("---")
st.markdown("<div style='text-align:center;color:gray;'>🚗 EV-Safety System | AI-Powered Predictive Maintenance | Accuracy: 99.0%</div>", 
            unsafe_allow_html=True)
