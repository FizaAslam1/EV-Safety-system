import streamlit as st
import pandas as pd
import pickle
import sklearn          
import sklearn.ensemble  
# ============================================
# PAGE SETUP
# ============================================
st.set_page_config(page_title="EV-Safety System", page_icon="🚗", layout="wide")

# ============================================
# LOAD MODEL
# ============================================
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as f:
        return pickle.load(f)

model = load_model()

# ============================================
# TITLE
# ============================================
st.title("🚗 EV-Safety System")
st.markdown("### ⚡ AI-Powered Predictive Maintenance for EV Chargers")
st.markdown("---")

# ============================================
# SIDEBAR - INPUTS
# ============================================
st.sidebar.header("⚙️ Charger Parameters")
st.sidebar.markdown("---")

voltage = st.sidebar.slider("⚡ Voltage (V)", 180, 260, 230)
temperature = st.sidebar.slider("🌡️ Temperature (°C)", 10, 90, 40)
session = st.sidebar.slider("⏱️ Session Duration (min)", 0, 180, 35)
error = st.sidebar.selectbox("⚠️ Error Code", [0, 1, 2], 
                              format_func=lambda x: {0: "0 - No Error", 1: "1 - Minor", 2: "2 - Major"}[x])
days = st.sidebar.slider("🔧 Days Since Maintenance", 0, 365, 30)

st.sidebar.markdown("---")
threshold = st.sidebar.slider("🎯 Risk Threshold (%)", 5, 50, 15, 
                               help="Probability above this value = FAIL")

# ============================================
# PREDICT BUTTON
# ============================================
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_btn = st.button("🔍 Analyze Charger Health", use_container_width=True, type="primary")

# ============================================
# PREDICTION LOGIC
# ============================================
if predict_btn:
    # Create input dataframe
    input_data = pd.DataFrame([[voltage, temperature, session, error, days]],
                              columns=['voltage', 'temperature', 'session_duration', 
                                       'error_code', 'days_since_maintenance'])
    
    # Get probability
    probability = model.predict_proba(input_data)[0][1] * 100
    
    # Apply threshold
    if probability > threshold:
        prediction = 1
    else:
        prediction = 0
    
    st.markdown("---")
    
    # ============================================
    # RESULT COLUMNS
    # ============================================
    col1, col2 = st.columns(2)
    
    with col1:
        if prediction == 1:
            st.error("### ❌ FAILURE PREDICTED!")
        else:
            st.success("### ✅ CHARGER IS HEALTHY")
        
        st.metric(label="Failure Probability", value=f"{probability:.1f}%")
    
    with col2:
        # Risk Level
        if probability > 70:
            st.markdown("### 🔴 CRITICAL RISK")
            st.markdown("🚨 **Immediate action required!**")
        elif probability > 40:
            st.markdown("### 🟡 WARNING")
            st.markdown("⚠️ **Schedule maintenance soon**")
        elif probability > 10:
            st.markdown("### 🟠 LOW RISK")
            st.markdown("👀 **Monitor closely**")
        else:
            st.markdown("### 🟢 SAFE")
            st.markdown("✅ **No action needed**")
    
    # ============================================
    # PROGRESS BAR
    # ============================================
    st.markdown("---")
    st.markdown("### 📊 Risk Visualization")
    
    # Color based on probability
    if probability > 70:
        bar_color = "🔴"
    elif probability > 40:
        bar_color = "🟡"
    elif probability > 10:
        bar_color = "🟠"
    else:
        bar_color = "🟢"
    
    st.progress(min(int(probability), 100) / 100)
    st.caption(f"{bar_color} Failure Risk: {probability:.1f}% (Threshold: {threshold}%)")
    
    # ============================================
    # INPUT PARAMETERS SUMMARY
    # ============================================
    st.markdown("---")
    st.markdown("### 📋 Input Parameters")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("⚡ Voltage", f"{voltage}V")
    col2.metric("🌡️ Temperature", f"{temperature}°C")
    col3.metric("⏱️ Session", f"{session}min")
    col4.metric("⚠️ Error", error)
    col5.metric("🔧 Days Maint.", f"{days}d")

else:
    # Default view when no prediction
    st.info("👈 Adjust parameters in sidebar and click **Analyze Charger Health**")
    
    st.markdown("---")
    st.markdown("### 📊 Current Parameters")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("⚡ Voltage", f"{voltage}V")
    col2.metric("🌡️ Temperature", f"{temperature}°C")
    col3.metric("⏱️ Session", f"{session}min")
    col4.metric("⚠️ Error", error)
    col5.metric("🔧 Days Maint.", f"{days}d")

# ============================================
# FOOTER
# ============================================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>🚗 <b>EV-Safety System</b> | AI-Powered Predictive Maintenance</p>
    <p>Model: Random Forest | Accuracy: 99.0% | AUC-ROC: 0.9999</p>
</div>
""", unsafe_allow_html=True)
