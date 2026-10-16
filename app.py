import streamlit as st
import os
import base64

st.set_page_config(page_title="Secret Vault for Sidra 🎂", page_icon="🐱", layout="centered")

# Helper to load Sidra's Bitmoji cleanly inside custom HTML
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

bitmoji_b64 = (
    get_base64_image("bitmoji.png")
    or get_base64_image("bitmoji.jpg")
    or get_base64_image("bitmoji.jpeg")
)

# Custom Cartoon CSS, Floating Stickers & Multicolor Theme
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Quicksand:wght@600;700&display=swap');

/* Animated Multicolor Cartoon Sky Background */
.stApp {
    background: linear-gradient(-45deg, #00a8ff, #ff6b8b, #feca57, #48dbfb, #a29bfe, #ff9ff3);
    background-size: 400% 400%;
    animation: gradientBG 7s ease infinite;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Cartoon Bubble Headers */
h1, h2, h3 {
    font-family: 'Fredoka One', cursive !important;
    color: #ffffff !important;
    text-shadow: 4px 4px 0px #ff4757, 7px 7px 0px #2f3542 !important;
    text-align: center;
    letter-spacing: 1px;
}

/* Giant Finale Title for Sidra */
.giant-bday-title {
    font-family: 'Fredoka One', cursive !important;
    font-size: 54px !important;
    color: #ffffff !important;
    text-shadow: 5px 5px 0px #ff4757, 9px 9px 0px #2f3542 !important;
    text-align: center;
    line-height: 1.2;
    margin: 25px 0 15px 0;
    animation: wiggleCake 1.5s infinite;
}

/* Floating Bitmoji & Level 24 Cake Showcase */
.bitmoji-wrapper {
    text-align: center;
    margin: 15px auto 25px auto;
    animation: bounceBitmoji 2.8s ease-in-out infinite;
}

.bitmoji-img {
    width: 210px;
    height: 210px;
    object-fit: cover;
    border-radius: 50%;
    border: 7px solid #ffffff;
    box-shadow: 0px 10px 0px #2f3542, 0px 0px 30px #feca57;
    background: #ffffff;
}

.cake-24-badge {
    display: inline-block;
    background: linear-gradient(45deg, #ff4757, #ff6b81);
    color: #ffffff;
    font-family: 'Fredoka One', cursive;
    font-size: 28px;
    padding: 10px 30px;
    border-radius: 50px;
    border: 5px solid #ffffff;
    box-shadow: 0px 8px 0px #2f3542;
    margin-top: -25px;
    position: relative;
    z-index: 5;
    text-shadow: 2px 2px 0px #2f3542;
    animation: wiggleCake 1.8s infinite;
}

@keyframes bounceBitmoji {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-14px); }
}

@keyframes wiggleCake {
    0%, 100% { transform: rotate(-2deg) scale(1); }
    50% { transform: rotate(2deg) scale(1.05); }
}

/* Bouncing 3D Cartoon Story Cards */
.cartoon-card {
    background: rgba(255, 255, 255, 0.96);
    border-radius: 28px;
    padding: 25px;
    margin: 25px 0;
    border: 5px solid #2f3542;
    box-shadow: 10px 10px 0px #2f3542;
    animation: floatCard 3.2s ease-in-out infinite;
}

.card-doraemon { border-color: #0097e6; box-shadow: 10px 10px 0px #0097e6; }
.card-tom { border-color: #ff4757; box-shadow: 10px 10px 0px #ff4757; animation-delay: 0.8s; }
.card-jerry { border-color: #ffa502; box-shadow: 10px 10px 0px #ffa502; animation-delay: 1.6s; }
.card-sidra { border-color: #8c7ae6; box-shadow: 10px 10px 0px #8c7ae6; animation-delay: 2.2s; }

@keyframes floatCard {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-9px) rotate(0.5deg); }
}

.card-title {
    font-family: 'Fredoka One', cursive;
    font-size: 26px;
    margin-bottom: 12px;
    text-align: center;
}

.card-text {
    font-family: 'Quicksand', sans-serif;
    font-size: 18px;
    color: #2f3542;
    line-height: 1.6;
    font-weight: 700;
}

/* Pure Cartoon Sticker Frame with Bouncing Animation */
.toon-card-box {
    background: #ffffff;
    border-radius: 24px;
    border: 5px solid #2f3542;
    box-shadow: 7px 7px 0px #2f3542;
    padding: 8px;
    margin-bottom: 15px;
    text-align: center;
    animation: popSticker 2.5s ease-in-out infinite;
}

.toon-pic {
    border-radius: 16px;
    width: 100%;
    height: 170px;
    object-fit: cover;
    background: #f1f2f6;
}

.toon-label {
    font-family: 'Fredoka One', cursive;
    font-size: 15px;
    color: #ff4757;
    margin-top: 6px;
}

@keyframes popSticker {
    0%, 100% { transform: scale(1) rotate(-1deg); }
    50% { transform: scale(1.04) rotate(1deg); }
}

/* Input Box Styling */
div[data-baseweb="input"] {
    border-radius: 20px !important;
    border: 4px solid #2f3542 !important;
    font-family: 'Quicksand', sans-serif !important;
    font-weight: 700 !important;
}

/* Mega Cartoon Button */
div.stButton > button {
    background: linear-gradient(45deg, #ff4757, #ffa502);
    color: white !important;
    font-family: 'Fredoka One', cursive !important;
    font-size: 23px !important;
    border-radius: 50px !important;
    border: 5px solid #ffffff !important;
    box-shadow: 0px 9px 0px #2f3542 !important;
    padding: 14px 30px !important;
    width: 100%;
    animation: wiggleCake 1.5s infinite;
}
</style>
""", unsafe_allow_html=True)

# 1. Main Header
st.markdown("<h1>✨ Secret Vault for Sidra ✨</h1>", unsafe_allow_html=True)

# 2. Sidra's Bitmoji + Glowing 24th Birthday Cake Badge
if bitmoji_b64:
    st.markdown(f"""
    <div class="bitmoji-wrapper">
        <img src="data:image/png;base64,{bitmoji_b64}" class="bitmoji-img"><br>
        <div class="cake-24-badge">🎂🕯️ 24 🕯️🎂</div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="bitmoji-wrapper">
        <div style="font-size: 95px;">👼🏻🎂</div>
        <div class="cake-24-badge">🎂🕯️ 24 🕯️🎂</div>
    </div>
    """, unsafe_allow_html=True)
    st.info("💡 Tip: Upload 'bitmoji.png' to your GitHub repository so Sidra's Snapchat Bitmoji appears right here!")

# 3. Preview Cartoon Row (Happy Doraemon, Good-Vibe Cute Jerry, Excited Pikachu)
g1, g2, g3 = st.columns(3)
with g1:
    st.markdown("""
    <div class="toon-card-box">
        <img src="https://media.giphy.com/media/noKPfoiakFXsk/giphy.gif" class="toon-pic">
        <div class="toon-label" style="color:#0097e6;">Happy Doraemon! 🔔</div>
    </div>
    """, unsafe_allow_html=True)
with g2:
    # Replaced fighting Tom & Jerry with happy, wholesome Jerry & Nibbles!
    st.markdown("""
    <div class="toon-card-box" style="animation-delay: 0.4s;">
        <img src="https://media.tenor.com/T4h5q6QMk00AAAAM/tom-and-jerry-flattered.gif" class="toon-pic">
        <div class="toon-label" style="color:#ffa502;">Happy Jerry! 🧀</div>
    </div>
    """, unsafe_allow_html=True)
with g3:
    st.markdown("""
    <div class="toon-card-box" style="animation-delay: 0.8s;">
        <img src="https://media.giphy.com/media/xuXzcHMkuwvf2/giphy.gif" class="toon-pic">
        <div class="toon-label" style="color:#ff4757;">
