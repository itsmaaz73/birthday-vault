import streamlit as st
import time

st.set_page_config(page_title="Cartoon Birthday World! 🎈", page_icon="🦄", layout="centered")

# Injecting Custom Cartoon CSS & Multicolor Animations
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Quicksand:wght@600;700&display=swap');

/* Animated Multicolor Candy Background */
.stApp {
    background: linear-gradient(-45deg, #ff6b8b, #ff8e53, #feca57, #48dbfb, #ff9ff3, #a29bfe);
    background-size: 400% 400%;
    animation: gradientBG 8s ease infinite;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Cartoon Fonts */
h1, h2, h3 {
    font-family: 'Fredoka One', cursive !important;
    color: #ffffff !important;
    text-shadow: 3px 3px 0px #ff4757, 5px 5px 0px #2f3542 !important;
    text-align: center;
}

p, label, .stMarkdown {
    font-family: 'Quicksand', sans-serif !important;
    font-size: 18px !important;
}

/* Bouncing & Floating Cartoon Cards */
.cartoon-card {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 25px;
    padding: 25px;
    margin: 25px 0;
    border: 5px solid #2f3542;
    box-shadow: 10px 10px 0px #2f3542;
    animation: floatCard 3s ease-in-out infinite;
    color: #2f3542 !important;
}

.card-pink { border-color: #ff4757; box-shadow: 10px 10px 0px #ff4757; }
.card-blue { border-color: #1e90ff; box-shadow: 10px 10px 0px #1e90ff; animation-delay: 1s; }
.card-purple { border-color: #9c88ff; box-shadow: 10px 10px 0px #9c88ff; animation-delay: 2s; }

@keyframes floatCard {
    0% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-10px) rotate(0.5deg); }
    100% { transform: translateY(0px) rotate(0deg); }
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

/* Wiggling Cartoon Button */
div.stButton > button {
    background: linear-gradient(45deg, #ff4757, #ffa502);
    color: white !important;
    font-family: 'Fredoka One', cursive !important;
    font-size: 22px !important;
    border-radius: 50px !important;
    border: 4px solid #ffffff !important;
    box-shadow: 0px 8px 0px #b33939 !important;
    padding: 12px 30px !important;
    width: 100%;
    transition: all 0.2s !important;
    animation: pulseBtn 1.5s infinite;
}

div.stButton > button:hover {
    transform: scale(1.05);
}

@keyframes pulseBtn {
    0% { transform: scale(1); }
    50% { transform: scale(1.03); }
    100% { transform: scale(1); }
}
</style>
""", unsafe_allow_html=True)

# Top Cartoon Banner
st.markdown("<h1>🎪 Magical Birthday Toon Vault 🎪</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://media.giphy.com/media/l4KibWpBGWchSqCRy/giphy.gif", use_container_width=True)

st.markdown("""
<div class="cartoon-card card-pink" style="text-align: center;">
    <div class="card-title" style="color: #ff4757;">🔐 Secret Cartoon Passcode</div>
    <div class="card-text">
        To unlock this magical world, enter the exact date (Day & Month) a random Snapchat story right after Iftari & Maghrib turned into the best friendship ever!
    </div>
</div>
""", unsafe_allow_html=True)

password = st.text_input("✨ Type the secret date here (Format: 20 March) and press Enter:", "")

if password.strip().lower() in ["20 march", "march 20", "20th march", "20 march "]:
    st.balloons()
    
    # Confetti & Celebration Header
    st.markdown("<h2>🎉 BOOM! ACCESS GRANTED! HAPPY BIRTHDAY! 🎉</h2>", unsafe_allow_html=True)
    
    # Row of Dancing Cartoons
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image("https://media.giphy.com/media/11sBLVxNs7v6WA/giphy.gif", use_container_width=True)
    with c2:
        st.image("https://media.giphy.com/media/feio2yIUMtdqWjRiaF/giphy.gif", use_container_width=True)
    with c3:
        st.image("https://media.giphy.com/media/blSTtZehjAZ8I/giphy.gif", use_container_width=True)

    # Card 1: The Story
    st.markdown("""
    <div class="cartoon-card card-pink">
        <div class="card-title" style="color: #ff4757;">🌙 From a Ramadan Snap to Besties!</div>
        <div class="card-text">
            It is honestly crazy to think that we have never met in person, yet you know more about my personal life than almost anyone else! All because you saw my Snapchat story and added me on <b>20th March in Ramadan</b>, right after Iftari and Maghrib prayer. Best notification ever! 🌟
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Card 2: Wifey Referee
    st.markdown("""
    <div class="cartoon-card card-blue">
        <div class="card-title" style="color: #1e90ff;">🦸‍♀️ Official Relationship Superhero</div>
        <div class="card-text">
            Thank you for always supporting me, and especially for being the ultimate peacekeeper between me and my wifey! Whenever we fight and get angry at each other, you step in like a cartoon superhero, calm both of us down, and make everything normal again. 🕊️💖
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Card 3: The Best Person Ever
    st.markdown("""
    <div class="cartoon-card card-purple">
        <div class="card-title" style="color: #8c7ae6;">👑 One in a Billion!</div>
        <div class="card-text">
            You are hands down the best person in friendship I have ever met. Sometimes I genuinely sit and wonder how someone so pure-hearted and perfect like you even exists in this world! Have the happiest, most colorful birthday ever! 🎂🎁🌈
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Interactive Cartoon Surprise Button
    st.write("")
    if st.button("🎁 CLICK HERE FOR MEGA BIRTHDAY MAGIC! 🎁"):
        st.snow()
        st.balloons()
        st.markdown("<h2>✨ YOU ARE OFFICIALLY THE COOLEST BEST FRIEND ON EARTH! ✨</h2>", unsafe_allow_html=True)
        st.image("https://media.giphy.com/media/artj92V8o75VPL7AeQ/giphy.gif", use_container_width=True)

elif password != "":
    st.error("❌ Oops! Wrong passcode! Hint: Think back to Ramadan right after Iftari & Maghrib! 🌙")
