import time
import streamlit as st

# Page Title aur Layout
st.set_page_config(page_title="Animated Python App", page_icon="🚀", layout="centered")

# Custom Styling (CSS effect)
st.markdown(
    """
    <style>
    .main-title {
        color: #FF4B4B;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
    }
    .rocket-text {
        font-size: 80px;
        text-align: center;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    "<h1 class='main-title'>🎬 Python Web Animation Demo</h1>",
    unsafe_allow_html=True,
)
st.write(
    "### Button daba kar animation start karein aur progress dekhein!"
)

# Interactive Animation trigger button
if st.button("🚀 Launch Rocket Animation"):

    # 1. Countdown Animation
    st.write("---")
    countdown_spot = st.empty()
    for i in range(3, 0, -1):
        countdown_spot.markdown(f"## ⏳ Launching in: **{i}**")
        time.sleep(1)

    countdown_spot.success("🎉 **Liftoff!**")

    # 2. Moving Rocket Frame Animation
    sky_frame = st.empty()
    space_layers = [
        "🌍 -------------------- 🚀 (Ground)",
        "☁️ -------- 🚀 --------- (Clouds)",
        "✨ ---- 🚀 ------------- (Atmosphere)",
        "🌌 🚀 ------------------ (Deep Space)",
    ]

    for frame in space_layers:
        sky_frame.markdown(f"### {frame}")
        time.sleep(0.8)

    # 3. Progress Bar Animation
    st.write("### 🔋 Fuel Burning Progress:")
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.02)
        progress_bar.progress(percent_complete + 1)

    # Celebration Effect!
    st.balloons()
    st.success("Mission Successful! Rocket space me pahunch gaya! 🌠")