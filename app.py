
#  Network Intrusion Detection System — Streamlit Frontend
#  Run with:  streamlit run app.py


import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
import random
from datetime import datetime

try:
    from scapy.all import sniff, IP, TCP, UDP, ICMP
    SCAPY_AVAILABLE = True
except:
    SCAPY_AVAILABLE = False

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
    div[data-testid="stVerticalBlock"] { gap: 15px; }
    .block-container { padding-top: 1rem; padding-bottom: 1rem; }
    .stSlider { padding: 0 10px; }
    .stTextInput > div > div { background: #1e1e30; border: 1px solid #3a3a5c; }
    .stSelectbox > div > div { background: #1e1e30; border: 1px solid #3a3a5c; }
    .stNumberInput > div > div { background: #1e1e30; border: 1px solid #3a3a5c; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_models():
    model = joblib.load("models/best_model.joblib")
    scaler = joblib.load("models/scaler.joblib")
    encoders = joblib.load("models/encoders.joblib")
    features = joblib.load("models/feature_names.joblib")
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

NORMAL_SAMPLE = {
    "duration": 0, "protocol_type": "tcp", "service": "http", "flag": "SF",
    "src_bytes": 215, "dst_bytes": 45076, "land": 0, "wrong_fragment": 0,
    "urgent": 0, "hot": 0, "num_failed_logins": 0, "logged_in": 1,
    "num_compromised": 0, "root_shell": 0, "su_attempted": 0, "num_root": 0,
    "num_file_creations": 0, "num_shells": 0, "num_access_files": 0,
    "num_outbound_cmds": 0, "is_host_login": 0, "is_guest_login": 0,
    "count": 2, "srv_count": 2, "serror_rate": 0.0, "srv_serror_rate": 0.0,
    "rerror_rate": 0.0, "srv_rerror_rate": 0.0, "same_srv_rate": 1.0,
    "diff_srv_rate": 0.0, "srv_diff_host_rate": 0.0, "dst_host_count": 255,
    "dst_host_srv_count": 255, "dst_host_same_srv_rate": 1.0,
    "dst_host_diff_srv_rate": 0.0, "dst_host_same_src_port_rate": 0.0,
    "dst_host_srv_diff_host_rate": 0.0, "dst_host_serror_rate": 0.0,
    "dst_host_srv_serror_rate": 0.0, "dst_host_rerror_rate": 0.0,
    "dst_host_srv_rerror_rate": 0.0,
}

ATTACK_SAMPLE = {
    "duration": 0, "protocol_type": "tcp", "service": "http", "flag": "S0",
    "src_bytes": 0, "dst_bytes": 0, "land": 0, "wrong_fragment": 0,
    "urgent": 0, "hot": 0, "num_failed_logins": 0, "logged_in": 0,
    "num_compromised": 0, "root_shell": 0, "su_attempted": 0, "num_root": 0,
    "num_file_creations": 0, "num_shells": 0, "num_access_files": 0,
    "num_outbound_cmds": 0, "is_host_login": 0, "is_guest_login": 0,
    "count": 511, "srv_count": 511, "serror_rate": 1.0, "srv_serror_rate": 1.0,
    "rerror_rate": 0.0, "srv_rerror_rate": 0.0, "same_srv_rate": 1.0,
    "diff_srv_rate": 0.0, "srv_diff_host_rate": 0.0, "dst_host_count": 255,
    "dst_host_srv_count": 255, "dst_host_same_srv_rate": 1.0,
    "dst_host_diff_srv_rate": 0.0, "dst_host_same_src_port_rate": 1.0,
    "dst_host_srv_diff_host_rate": 0.0, "dst_host_serror_rate": 1.0,
    "dst_host_srv_serror_rate": 1.0, "dst_host_rerror_rate": 0.0,
    "dst_host_srv_rerror_rate": 0.0,
}

def is_npcap_installed():
    """Check if Npcap or WinPcap is installed on Windows."""
    import platform
    if platform.system() != "Windows":
        return True  # Linux/Mac handle pcap differently
    import winreg
    keys_to_check = [
        r"SOFTWARE\Npcap",
        r"SOFTWARE\WinPcap",
    ]
    for key in keys_to_check:
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key):
                return True
        except FileNotFoundError:
            continue
    return False

def get_network_interfaces():
    if not SCAPY_AVAILABLE:
        return []
    try:
        import platform
        if platform.system() == "Windows":
            # Use scapy's Windows-specific interface lister
            try:
                from scapy.arch.windows import get_windows_if_list
                ifaces = get_windows_if_list()
                names = [i.get("name", i.get("description", "")) for i in ifaces if i.get("name")]
                if names:
                    return names
            except Exception:
                pass
            # Fallback: scapy ifaces dict
            try:
                from scapy.interfaces import IFACES
                names = [str(v.name) for v in IFACES.data.values() if hasattr(v, 'name') and v.name]
                if names:
                    return names
            except Exception:
                pass
            return []  # empty = admin required
        else:
            from scapy.interfaces import get_if_list
            interfaces = get_if_list()
            return interfaces if interfaces else []
    except:
        return []

def packet_to_features(pkt):
    if not pkt.haslayer(IP):
        return None
    src, dst = pkt[IP].src, pkt[IP].dst
    if pkt.haslayer(TCP):
        proto, sport, dport, flags = "tcp", pkt[TCP].sport, pkt[TCP].dport, str(pkt[TCP].flags)
    elif pkt.haslayer(UDP):
        proto, sport, dport, flags = "udp", pkt[UDP].sport, pkt[UDP].dport, "SF"
    elif pkt.haslayer(ICMP):
        proto, sport, dport, flags = "icmp", 0, 0, "SF"
    else:
        proto, sport, dport, flags = "tcp", 0, 0, "SF"
    
    service_map = {80: "http", 443: "http", 22: "ssh", 21: "ftp", 25: "smtp", 53: "domain", 3306: "mysql", 5432: "postgres", 8080: "http"}
    service = service_map.get(dport, "other")
    
    logged_in = 1 if dport in [22, 23, 21, 25, 80, 443] else 0
    flag_map = {"S": "S0", "SA": "S0", "R": "REJ", "RA": "REJ", "F": "SF", "FPRS": "SF", "FPR": "SF", "SHR": "SH"}
    flag = flag_map.get(flags, "SF")
    serror_rate = 1.0 if "S" in flags and "A" not in flags else 0.0
    
    return {
        "duration": 0, "protocol_type": proto, "service": service, "flag": flag,
        "src_bytes": len(pkt), "dst_bytes": 0, "land": 1 if src == dst else 0,
        "wrong_fragment": 0, "urgent": 0, "hot": 0, "num_failed_logins": 0,
        "logged_in": logged_in, "num_compromised": 0, "root_shell": 0, "su_attempted": 0,
        "num_root": 0, "num_file_creations": 0, "num_shells": 0, "num_access_files": 0,
        "num_outbound_cmds": 0, "is_host_login": 0, "is_guest_login": 0, "count": 1,
        "srv_count": 1, "serror_rate": serror_rate, "srv_serror_rate": serror_rate,
        "rerror_rate": 0.0, "srv_rerror_rate": 0.0, "same_srv_rate": 0.8,
        "diff_srv_rate": 0.2, "srv_diff_host_rate": 0.0, "dst_host_count": 1,
        "dst_host_srv_count": 1, "dst_host_same_srv_rate": 0.8, "dst_host_diff_srv_rate": 0.2,
        "dst_host_same_src_port_rate": 0.5, "dst_host_srv_diff_host_rate": 0.0,
        "dst_host_serror_rate": serror_rate, "dst_host_srv_serror_rate": serror_rate,
        "dst_host_rerror_rate": 0.0, "dst_host_srv_rerror_rate": 0.0,
    }

page = st.session_state.get("page", "Dashboard")

with st.sidebar:
    st.markdown("### 🛡️ NIDS")
    st.markdown("---")
    
    pages = [
        ("🏠", "Dashboard"),
        ("🔍", "Detection"),
        ("⚡", "Simulation"),
        ("📂", "Batch"),
        ("ℹ️", "About"),
    ]
    
    for icon, key in pages:
        label = {"Dashboard": "Home", "Detection": "Manual", "Simulation": "Live", "Batch": "Batch", "About": "Info"}.get(key, key)
        if st.button(f"{icon} {label}", use_container_width=True, type="secondary" if page != key else "primary"):
            st.session_state["page"] = key
            page = key
            st.rerun()
    
    st.markdown("---")
    st.caption(f"🕐 {datetime.now().strftime('%H:%M')}")
    st.caption("Model: Random Forest")

if page == "Dashboard":
    st.markdown('<p class="title-text">🛡️ Network Intrusion Detection</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text">Real-time AI-powered network security monitoring</p>', unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Dataset", "NSL-KDD")
    with c2: st.metric("Model", "Random Forest")
    with c3: st.metric("Accuracy", "~79%")
    with c4: st.metric("Features", "41")
    
    st.markdown("### 🚀 Quick Actions")
    action_cols = st.columns(3)
    with action_cols[0]:
        if st.button("🔍 Manual Detection", use_container_width=True):
            st.session_state["page"] = "Detection"
            st.rerun()
    with action_cols[1]:
        if st.button("⚡ Live Analysis", use_container_width=True):
            st.session_state["page"] = "Simulation"
            st.rerun()
    with action_cols[2]:
        if st.button("📂 Batch Upload", use_container_width=True):
            st.session_state["page"] = "Batch"
            st.rerun()
    
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.markdown("### 📊 Model Comparison")
        models = [("Random Forest ⭐", 79.2), ("MLP Neural Net", 78.1), ("SVM", 76.5)]
        for name, acc in models:
            st.markdown(f"""
            <div class="stat-box">
                <span style="color: #a0a0b0;">{name}</span>
                <span style="color: #00d4ff; float: right;">{acc}%</span>
                <div class="progress-bar" style="margin-top: 5px;">
                    <div class="progress-fill" style="width: {acc}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col_right:
        st.markdown("### 🛡️ Status")
        st.markdown("""
        <div class="home-hero">
            <p style="color: #00ff88; margin: 0;">● Online</p>
            <p style="color: #a0a0b0; font-size: 0.8rem;">Monitoring active</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "Detection":
    st.markdown('<p class="section-header">🔍 Manual Traffic Detection</p>', unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        fill_normal = st.button("📋 Normal Sample", use_container_width=True)
    with col_b:
        fill_attack = st.button("⚠️ Attack Sample", use_container_width=True)
    
    defaults = ATTACK_SAMPLE.copy() if fill_attack else NORMAL_SAMPLE.copy()
    
    with st.expander("📡 Connection Info", expanded=True):
        c1, c2, c3, c4 = st.columns(4)
        with c1: duration = c1.number_input("Duration", value=int(defaults["duration"]), min_value=0)
        with c2: protocol_type = c2.selectbox("Protocol", ["tcp", "udp", "icmp"], index=["tcp", "udp", "icmp"].index(defaults["protocol_type"]))
        with c3: service = c3.text_input("Service", value=defaults["service"])
        with c4: flag = c4.selectbox("Flag", ["SF", "S0", "REJ", "RSTO", "SH", "S1", "S2", "S3", "RSTOS0", "RSTR", "OTH"], index=["SF", "S0", "REJ", "RSTO", "SH", "S1", "S2", "S3", "RSTOS0", "RSTR", "OTH"].index(defaults["flag"]))
    
    with st.expander("📊 Data Transfer"):
        c1, c2, c3, c4 = st.columns(4)
        with c1: src_bytes = c1.number_input("Source Bytes", value=int(defaults["src_bytes"]), min_value=0)
        with c2: dst_bytes = c2.number_input("Dest Bytes", value=int(defaults["dst_bytes"]), min_value=0)
        with c3: wrong_fragment = c3.number_input("Wrong Fragments", value=int(defaults["wrong_fragment"]), min_value=0)
        with c4: urgent = c4.number_input("Urgent", value=int(defaults["urgent"]), min_value=0)
    
    with st.expander("🔐 Authentication"):
        c1, c2, c3, c4 = st.columns(4)
        with c1: logged_in = c1.selectbox("Logged In", [0, 1], index=int(defaults["logged_in"]))
        with c2: num_failed_logins = c2.number_input("Failed Logins", value=int(defaults["num_failed_logins"]), min_value=0)
        with c3: is_guest_login = c3.selectbox("Guest", [0, 1], index=int(defaults["is_guest_login"]))
        with c4: root_shell = c4.selectbox("Root Shell", [0, 1], index=int(defaults["root_shell"]))
    
    with st.expander("📈 Traffic Rates"):
        c1, c2, c3, c4 = st.columns(4)
        with c1: count = c1.number_input("Count", value=int(defaults["count"]), min_value=0)
        with c2: srv_count = c2.number_input("Srv Count", value=int(defaults["srv_count"]), min_value=0)
        with c3: serror_rate = c3.slider("SYN Error", 0.0, 1.0, float(defaults["serror_rate"]), 0.01)
        with c4: rerror_rate = c4.slider("REJ Error", 0.0, 1.0, float(defaults["rerror_rate"]), 0.01)
        
        c1, c2, c3, c4 = st.columns(4)
        with c1: same_srv_rate = c1.slider("Same Srv", 0.0, 1.0, float(defaults["same_srv_rate"]), 0.01)
        with c2: diff_srv_rate = c2.slider("Diff Srv", 0.0, 1.0, float(defaults["diff_srv_rate"]), 0.01)
        with c3: dst_host_count = c3.number_input("Dst Host", value=int(defaults["dst_host_count"]), min_value=0, max_value=255)
        with c4: dst_host_serror_rate = c4.slider("DstHost Err", 0.0, 1.0, float(defaults["dst_host_serror_rate"]), 0.01)
    
    input_data = NORMAL_SAMPLE.copy()
    input_data.update({
        "duration": duration, "protocol_type": protocol_type, "service": service, "flag": flag,
        "src_bytes": src_bytes, "dst_bytes": dst_bytes, "wrong_fragment": wrong_fragment,
        "urgent": urgent, "logged_in": logged_in, "num_failed_logins": num_failed_logins,
        "is_guest_login": is_guest_login, "root_shell": root_shell, "count": count,
        "srv_count": srv_count, "serror_rate": serror_rate, "rerror_rate": rerror_rate,
        "same_srv_rate": same_srv_rate, "diff_srv_rate": diff_srv_rate,
        "dst_host_count": dst_host_count, "dst_host_serror_rate": dst_host_serror_rate,
    })
    
    st.markdown("---")
    if st.button("🔍 Analyze Traffic", type="primary", use_container_width=True):
        pred, confidence = predict(input_data)
        
        if pred == 1:
            st.markdown(f"""
            <div class="danger-box">
                <h3 style="color: #ff4444; margin: 0;">🚨 ATTACK DETECTED</h3>
                <p style="color: #ff8888;">Confidence: {confidence}%</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="success-box">
                <h3 style="color: #00ff88; margin: 0;">✅ NORMAL TRAFFIC</h3>
                <p style="color: #88ffaa;">Confidence: {confidence}%</p>
            </div>
            """, unsafe_allow_html=True)

elif page == "Simulation":
    st.markdown('<p class="section-header">⚡ Live Traffic Analysis</p>', unsafe_allow_html=True)
    
    capture_mode = st.radio("Mode:", ["🎲 Simulated", "🌐 Real Capture"], horizontal=True)
    
    if capture_mode == "🎲 Simulated":
        st.info("Generate random network traffic for testing")
        
        c1, c2 = st.columns(2)
        with c1: num_packets = c1.slider("Packets", 5, 50, 20)
        with c2: attack_ratio = c2.slider("Attack %", 0, 100, 30)
        
        if st.button("▶️ Start", type="primary", use_container_width=True):
            log_placeholder = st.empty()
            stats_placeholder = st.empty()
            
            attack_count = normal_count = 0
            log_lines = []
            
            for i in range(num_packets):
                is_attack = random.random() < (attack_ratio / 100)
                base = ATTACK_SAMPLE.copy() if is_attack else NORMAL_SAMPLE.copy()
                base["src_bytes"] = max(0, int(base["src_bytes"] + random.randint(-50, 50)))
                base["serror_rate"] = min(1.0, max(0.0, base["serror_rate"] + random.uniform(-0.05, 0.05)))
                
                pred, conf = predict(base)
                
                if pred == 1:
                    attack_count += 1
                    icon, status = "🔴", "ATTACK"
                else:
                    normal_count += 1
                    icon, status = "🟢", "NORMAL"
                
                log_lines.append(f"#{i+1:02d}  {icon}  {status}  {conf}%")
                log_placeholder.code("\n".join(log_lines[-12:]), language="text")
                time.sleep(0.08)
            
            with stats_placeholder:
                col_s1, col_s2, col_s3 = st.columns(3)
                with col_s1: st.metric("Total", num_packets)
                with col_s2: st.metric("🟢 Normal", normal_count)
                with col_s3: st.metric("🔴 Attack", attack_count)
    
    else:
        st.markdown("### 🌐 Real Network Capture")
        
        if not SCAPY_AVAILABLE:
            st.warning("Scapy not installed. Run: pip install scapy")
        elif not is_npcap_installed():
            st.markdown("""
            <div style="background: linear-gradient(145deg, #3d0f0f, #4d1515); padding: 20px; border-radius: 12px; border: 2px solid #ff4444; margin: 15px 0;">
                <h3 style="color: #ff4444; margin: 0 0 10px 0;">🚨 Npcap Driver Not Found</h3>
                <p style="color: #ffaaaa; margin: 0 0 10px 0;">Live packet capture on Windows requires the <b>Npcap</b> driver to be installed.</p>
                <p style="color: #a0a0b0; margin: 0;">📥 Download from: <b>https://npcap.com/#download</b><br>
                ✅ During install, check: <b>"Install Npcap in WinPcap API-compatible Mode"</b><br>
                🔄 Then restart VS Code and run the app again.</p>
            </div>
            """, unsafe_allow_html=True)
            st.info("💡 You can still use **Simulated Mode** on the left — it works without Npcap and is great for demos!")
        else:
            interfaces = get_network_interfaces()
            if not interfaces:
                st.markdown("""
                <div style="background: linear-gradient(145deg, #2a1a00, #3d2800); padding: 20px; border-radius: 12px; border: 2px solid #ffaa00; margin: 15px 0;">
                    <h3 style="color: #ffaa00; margin: 0 0 10px 0;">⚠️ Administrator Privileges Required</h3>
                    <p style="color: #ffcc77; margin: 0 0 10px 0;">Npcap is installed but Scapy cannot list network interfaces without <b>Administrator</b> rights.</p>
                    <p style="color: #a0a0b0; margin: 0;">
                    🔑 <b>To fix:</b><br>
                    1. Close VS Code completely<br>
                    2. Right-click the VS Code icon → <b>"Run as Administrator"</b><br>
                    3. Open this project folder and run the app again
                    </p>
                </div>
                """, unsafe_allow_html=True)
                st.info("💡 Or use **Simulated Mode** — it looks identical and works perfectly for a presentation demo!")
            else:
                st.info("Capture live packets from your network interface")
                
                col_net1, col_net2 = st.columns(2)
                with col_net1:
                    selected_iface = st.selectbox("Interface", interfaces)
                with col_net2:
                    capture_count = st.number_input("Packets", 5, 50, 15)
            
            if st.button("🔴 Start Capture", type="primary", use_container_width=True):
                try:
                    log_placeholder = st.empty()
                    stats_placeholder = st.empty()
                    
                    attack_count = normal_count = 0
                    log_lines = []
                    
                    for i in range(capture_count):
                        captured = sniff(iface=selected_iface, count=1, timeout=3)
                        
                        if captured:
                            pkt = captured[0]
                            features = packet_to_features(pkt)
                            
                            if features:
                                pred, conf = predict(features)
                                
                                if pred == 1:
                                    attack_count += 1
                                    icon, status = "🔴", "ATTACK"
                                else:
                                    normal_count += 1
                                    icon, status = "🟢", "NORMAL"
                                
                                src = pkt[IP].src if pkt.haslayer(IP) else "N/A"
                                dst = pkt[IP].dst if pkt.haslayer(IP) else "N/A"
                                proto = pkt.sprintf("%IP.proto%") if pkt.haslayer(IP) else "N/A"
                                
                                log_lines.append(f"#{i+1:02d} {src} → {dst} ({proto}) {icon} {status} {conf}%")
                                log_placeholder.code("\n".join(log_lines[-12:]), language="text")
                    
                    if attack_count + normal_count > 0:
                        with stats_placeholder:
                            col_s1, col_s2, col_s3 = st.columns(3)
                            with col_s1: st.metric("Captured", attack_count + normal_count)
                            with col_s2: st.metric("🟢 Normal", normal_count)
                            with col_s3: st.metric("🔴 Attack", attack_count)
                        st.success(f"Captured {attack_count + normal_count} packets from {selected_iface}")
                    else:
                        st.warning("No packets captured. Check network activity.")
                        
                except PermissionError:
                    st.error("Permission denied: Please run VS Code/Command Prompt as Administrator")
                except Exception as e:
                    st.error(f"Error: {e}")

elif page == "Batch":
    st.markdown('<p class="section-header">📂 Batch Analysis</p>', unsafe_allow_html=True)
    st.markdown("Upload CSV file for bulk traffic analysis")
    
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    
    if uploaded:
        df_upload = pd.read_csv(uploaded)
        
        col1, col2 = st.columns(2)
        with col1: st.metric("Records", len(df_upload))
        with col2: st.metric("Features", len(df_upload.columns))
        
        st.dataframe(df_upload.head(5), use_container_width=True)
        st.markdown("---")
        
        if st.button("🚀 Run Analysis", type="primary", use_container_width=True):
            actual_labels = None
            for col in ["label", "class", "target"]:
                if col in df_upload.columns:
                    actual_labels = df_upload[col].copy()
                    df_upload = df_upload.drop(col, axis=1)
                    break
            
            predictions, confidences = [], []
            progress = st.progress(0)
            
            for i, row in df_upload.iterrows():
                row_dict = row.to_dict()
                for feat in FEATURES:
                    if feat not in row_dict:
                        row_dict[feat] = NORMAL_SAMPLE.get(feat, 0)
                try:
                    pred, conf = predict(row_dict)
                    predictions.append("Attack" if pred == 1 else "Normal")
                    confidences.append(conf)
                except:
                    predictions.append("Error")
                    confidences.append(0.0)
                progress.progress((i+1)/len(df_upload))
            
            result_df = df_upload.copy()
            result_df.insert(0, "Prediction", predictions)
            result_df.insert(1, "Confidence", confidences)
            
            attack_count = predictions.count("Attack")
            normal_count = predictions.count("Normal")
            
            col_r1, col_r2, col_r3 = st.columns(3)
            with col_r1: st.metric("Total", len(predictions))
            with col_r2: st.metric("Normal", normal_count)
            with col_r3: st.metric("Attack", attack_count)
            
            if actual_labels is not None:
                actual_binary = actual_labels.apply(lambda x: 1 if str(x).strip().lower() not in ["normal", "0"] else 0).values
                pred_binary = [1 if p == "Attack" else 0 for p in predictions]
                accuracy = round(sum(a == p for a, p in zip(actual_binary, pred_binary)) / len(predictions) * 100, 2)
                st.success(f"Accuracy: {accuracy}%")
            
            csv = result_df.to_csv(index=False)
            st.download_button("💾 Download", csv, "results.csv", "text/csv")

elif page == "About":
    st.markdown('<p class="section-header">ℹ️ Project Information</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎓 Overview")
        st.markdown("""
        <div class="feature-card">
            <p style="color: #a0a0b0;">Network Intrusion Detection System using Machine Learning.
            Classifies network traffic as <b>Normal</b> or <b>Attack</b>.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📊 Dataset")
        st.markdown("""
        <div class="feature-card">
            <p style="color: #a0a0b0;"><b>NSL-KDD</b><br>41 features | Binary classification</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🤖 Models")
        st.markdown("""
        <div class="feature-card">
            <p style="color: #a0a0b0;">
            1. <b>Random Forest</b> ⭐ 79.2%<br>
            2. <b>MLP Neural Net</b> 78.1%<br>
            3. <b>SVM</b> 76.5%
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🚨 Attack Types")
        st.markdown("""
        <div class="feature-card">
            <p style="color: #a0a0b0;">
            <b>🌊 DoS</b> - neptune, smurf<br>
            <b>🔎 Probe</b> - ipsweep, portsweep<br>
            <b>🔑 R2L</b> - guess_passwd<br>
            <b>⬆️ U2R</b> - buffer_overflow
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🛠️ Tech Stack")
        st.markdown("""
        <div class="feature-card">
            <p style="color: #a0a0b0;">
            Python | Scikit-learn<br>
            Streamlit | Scapy<br>
            Pandas | NumPy
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align: center; color: #666;'>🛡️ NIDS | Academic Project 2026</div>", unsafe_allow_html=True)