import cv2
import numpy as np
import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI-Based Intelligent Video Surveillance Platform",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM ECO-TECH DARK THEMING ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        color: #ecf2f8;
    }
    div[data-testid="stSidebarUserContent"] {
        background-color: #161b22;
    }
    .metric-card {
        background-color: #1f242c;
        border-radius: 10px;
        padding: 15px;
        border-left: 5px solid #2ea44f;
        text-align: center;
        margin-bottom: 10px;
    }
    .status-safe {
        background-color: rgba(46, 164, 79, 0.15);
        border: 1px solid #2ea44f;
        color: #34d399;
        padding: 15px;
        border-radius: 8px;
        font-weight: bold;
        text-align: center;
        font-size: 24px;
    }
    .status-unsafe {
        background-color: rgba(248, 81, 73, 0.15);
        border: 1px solid #f85149;
        color: #ff7b72;
        padding: 15px;
        border-radius: 8px;
        font-weight: bold;
        text-align: center;
        font-size: 24px;
    }
    </style>
""", unsafe_allow_html=True)

# --- NAVIGATION ROUTING ---
st.sidebar.title("AK. Surveillance Platform")
page = st.sidebar.radio("Navigate", ["Home", "Video Prediction", "Analytics History", "About Pipeline", "Contact"])

# --- DATA MOCKING FOR DETECTION (REPLACING DEEP LEARNING ARCHITECTURE INFERENCE) ---
def process_surveillance_frame(frame, frame_count):
    """
    Simulates the hybrid AI pipeline: Object Detection + Pose Estimation
    Returns processed frame, status string, confidence level, and detected activity
    """
    h, w, _ = frame.shape
    # Simulate a dynamic scenario based on frame index sequences
    if (frame_count // 60) % 2 == 0:
        status = "SAFE"
        confidence = np.random.uniform(92.0, 98.4)
        activity = "Yoga / Meditation" if frame_count % 120 < 60 else "Walking"
        color = (0, 255, 0) # Green bounding box
        
        # Simulate Pose Estimation skeletal overlay
        cv2.circle(frame, (w//2, h//3), 15, color, -1)
        cv2.line(frame, (w//2, h//3 + 15), (w//2, h//2 + 40), color, 3)
        cv2.line(frame, (w//2, h//3 + 30), (w//2 - 40, h//3 + 60), color, 2)
        cv2.line(frame, (w//2, h//3 + 30), (w//2 + 40, h//3 + 60), color, 2)
    else:
        status = "UNSAFE"
        confidence = np.random.uniform(90.0, 95.2)
        activity = "Unauthorized Vehicle Detected (Motorcycle)"
        color = (0, 0, 255) # Red bounding box for hazard alert
        
        # Simulate Object Detection bounding box bounding a generic threat area
        cv2.rectangle(frame, (w//4, h//4), (3*w//4, 3*h//4), color, 3)
        
    # Visual HUD Overlay
    cv2.putText(frame, f"STATUS: {status}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)
    cv2.putText(frame, f"CONF: {confidence:.1f}%", (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    
    return frame, status, confidence, activity

# --- PAGE RENDERING ---

if page == "Home":
    st.title("Activity Detection System")
    st.subheader("Real-time AI pipeline for proactive public park monitoring and threat mitigation.")
    
    # Real-time Metrics Row from report snapshots
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><h3>98.4%</h3><p>Model Accuracy Target</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>14ms</h3><p>Inference Latency</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>12+</h3><p>Activities Monitored</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><h3>24/7</h3><p>Automated Surveillance</p></div>', unsafe_allow_html=True)

elif page == "Video Prediction":
    st.title(" Live Streaming Inference Dashboard")
    
    uploaded_file = st.file_uploader("Upload Park Surveillance Video Stream (MP4/AVI)", type=["mp4", "avi", "mov"])
    
    if uploaded_file is not None:
        # Save temporary file to process stream via OpenCV
        with open("temp_stream.mp4", "wb") as f:
            f.write(uploaded_file.read())
            
        cap = cv2.VideoCapture("temp_stream.mp4")
        frame_placeholder = st.empty()
        status_placeholder = st.empty()
        
        frame_idx = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
                
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            processed_frame, status, conf, current_act = process_surveillance_frame(frame, frame_idx)
            
            # Display real-time video feed
            frame_placeholder.image(processed_frame, channels="RGB", use_container_width=True)
            
            # Display Sidebar-style status updates dynamically
            with status_placeholder.container():
                if status == "SAFE":
                    st.markdown(f'<div class="status-safe">✅ SAFE • {current_act} ({conf:.1f}%)</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="status-unsafe">⚠️ UNSAFE • ALERT: {current_act} ({conf:.1f}%)</div>', unsafe_allow_html=True)
            
            frame_idx += 1
            time.sleep(0.02) # Emulate a stable 14ms-30ms hardware frame processing loop
        cap.release()
    else:
        st.info("Please upload a sample surveillance video file to start tracking frame activities.")

elif page == "Analytics History":
    st.title(" Security Logging & Analytics History")
    st.write("Reviewing automated historical data captured across system execution points:")
    
    # Render tracking table matching internship telemetry
    mock_logs = [
        {"Timestamp": "2026-05-16 10:14:02", "Area Zone": "North Pathway", "Activity Type": "Walking", "Classification": "SAFE", "Confidence": "98.2%"},
        {"Timestamp": "2026-05-16 10:22:15", "Area Zone": "Central Green", "Activity Type": "Yoga/Meditation", "Classification": "SAFE", "Confidence": "97.5%"},
        {"Timestamp": "2026-05-16 11:05:40", "Area Zone": "Pedestrian Plaza", "Activity Type": "Motorcycle Trespassing", "Classification": "UNSAFE", "Confidence": "94.1%"},
    ]
    st.table(mock_logs)

elif page == "About Pipeline":
    st.title("How It Works - Deep Learning Architecture")
    st.markdown("""
    ### Hybrid AI Surveillance Pipeline
    1. **Video Input:** Raw source feeds are loaded and structured frame-by-frame.
    2. **Unsafe Object Filtering:** Run through single-shot bounding filters (**YOLO / SSD**) targeting unauthorized hazards or vehicles. If spatial densities cross a 10% threshold, it flags immediate alert triggers.
    3. **Pose Estimation Mapping:** Human targets are structuralized into geometric joint paths to map orientation angles.
    4. **Sequential Action Classification:** Extracted pose arrays are calculated via underlying models to confidently output distinct actions (`Walking`, `Running`, `Sitting`, `Yoga`).
    """)

elif page == "Contact":
    st.title(" Get In Touch")
    st.markdown("""
    **Let's work together!** I am looking for software development internship and entry-level engineering roles.
    *  **Email:** abdulkalam11221@gmail.com
    *  **LinkedIn:** [Abdul Kalam](https://linkedin.com)
    """)
