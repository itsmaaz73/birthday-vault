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

# Custom Cartoon CSS, Floating Animations & Multicolor Theme
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Quicksand:wght@600;700&display=swap');

/* Animated Multicolor Doraemon & Candy Sky Background */
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
    0%, 100% { transform: rotate(-3deg) scale(1); }
    50% { transform: rotate(3deg) scale(1.06); }
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

/* Cartoon Sticker GIF Frame */
.toon-gif {
    border-radius: 22px;
    border: 5px solid #ffffff;
    box-shadow: 6px 6px 0px #2f3542;
    width: 100%;
    height: 180px;
    object-fit: cover;
    margin-bottom: 12px;
    background: #ffffff;
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

# 3. Preview Cartoon Row (Tom & Jerry + Doraemon guarding the Vault)
g1, g2, g3 = st.columns(3)
with g1:
    st.markdown('<img src="https://media.giphy.com/media/b8RfbQFaOs1rO10ren/giphy.gif" class="toon-gif">', unsafe_allow_html=True)
with g2:
    st.markdown('<img src="https://media.giphy.com/media/noKPfoiakFXsk/giphy.gif" class="toon-gif">', unsafe_allow_html=True)
with g3:
    st.markdown('<img src="https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif" class="toon-gif">', unsafe_allow_html=True)

# 4. Passcode Lock Card
st.markdown("""
<div class="cartoon-card card-doraemon" style="text-align: center;">
    <div class="card-title" style="color: #0097e6;">🔔 Doraemon & Jerry's Secret Passcode 🔔</div>
    <div class="card-text">
        To unlock Sidra's <b>24th Birthday Toon World</b>, enter the exact date (Day & Month) a random Snapchat story right after Iftari & Maghrib turned into the best friendship ever!
    </div>
</div>
""", unsafe_allow_html=True)

password = st.text_input("✨ Type the secret date here (Format: 20 March) and press Enter:", "")

# 5. Unlocked Birthday World
if password.strip().lower() in ["20 march", "march 20", "20th march", "20 march "]:
    st.balloons()
    
    st.markdown("<h2>🎉 HAPPY 24th BIRTHDAY SIDRA! 🎉</h2>", unsafe_allow_html=True)
    
    # Row 1 of Tom & Jerry + Doraemon Party Animations
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<img src="https://media.giphy.com/media/y9QemIlaYYWdi/giphy.gif" class="toon-gif">', unsafe_allow_html=True)
    with c2:
        st.markdown('<img src="https://media.giphy.com/media/KdrWY4sOKhpyVvwWiZ/giphy.gif" class="toon-gif">', unsafe_allow_html=True)
    with c3:
        st.markdown('<img src="https://media.giphy.com/media/8rEiN2GsOdQTm/giphy.gif" class="toon-gif">', unsafe_allow_html=True)

    # Story Card 1: 20 March Ramadan Story
    st.markdown("""
    <div class="cartoon-card card-tom">
        <div class="card-title" style="color: #ff4757;">🌙 20th March: Better Than Doraemon's Anywhere Door!</div>
        <div class="card-text">
            It is honestly crazy to think that we have never met in person, yet I tell you literally everything about my personal life! All because you saw my Snapchat story and added me on <b>20th March in Ramadan</b>, right after Iftari and Maghrib prayer. Distance means nothing when a friendship is this real! 🌟
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Story Card 2: Tom & Jerry Referee for Wifey
    st.markdown("""
    <div class="cartoon-card card-jerry">
        <div class="card-title" style="color: #ffa502;">🐱🐭 Official Tom & Jerry Peacekeeper!</div>
        <div class="card-text">
            Whenever me and my wifey fight and get angry at each other like <b>Tom and Jerry</b>, you always step in, calm both of us down, and help us go back to normal! Thank you for always supporting my relationship and having my back through everything. 🕊️💖
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Row 2 of Cartoons
    d1, d2, d3 = st.columns(3)
    with d1:
        st.markdown('<img src="https://media.giphy.com/media/l4EoPk1lohVe4674I/giphy.gif" class="toon-gif">', unsafe_allow_html=True)
    with d2:
        st.markdown('<img src="https://media.giphy.com/media/11sBLVxNs7v6WA/giphy.gif" class="toon-gif">', unsafe_allow_html=True)
    with d3:
        st.markdown('<img src="https://media.giphy.com/media/GeimqsH0TLDt4tScGw/giphy.gif" class="toon-gif">', unsafe_allow_html=True)

    # Story Card 3: Level 24 Verdict
    st.markdown("""
    <div class="cartoon-card card-sidra">
        <div class="card-title" style="color: #8c7ae6;">👑 Welcome to Level 24, Bestie!</div>
        <div class="card-text">
            You are hands down the best person in friendship I have ever met. Sometimes I genuinely wonder how someone so pure-hearted and perfect like you even exists in this world! Wishing you the happiest <b>24th Birthday</b> filled with endless smiles, cartoons, peace, and success! 🎂🎁🌈
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Interactive Doraemon Pocket Surprise Button
    st.write("")
    if st.button("🔔 CLICK TO OPEN DORAEMON'S 24th BIRTHDAY POCKET! 🎁"):
        st.snow()
        st.balloons()
        st.markdown("<h2>✨ CHAPTER 24: OFFICIALLY THE GREATEST BEST FRIEND EVER! ✨</h2>", unsafe_allow_html=True)
        s1, s2 = st.columns(2)
        with s1:
            st.markdown('<img src="https://media.giphy.com/media/artj92V8o75VPL7AeQ/giphy.gif" class="toon-gif" style="height: 240px;">', unsafe_allow_html=True)
        with s2:
            st.markdown('<img src="https://media.giphy.com/media/feio2yIUMtdqWjRiaF/giphy.gif" class="toon-gif" style="height: 240px;">', unsafe_allow_html=True)

elif password != "":
    st.error("❌ Jerry says wrong passcode! Hint: Think back to Ramadan right after Iftari & Maghrib! (Format: 20 March) 🌙")
