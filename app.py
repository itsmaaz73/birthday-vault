import streamlit as st
import time

st.set_page_config(page_title="Special Delivery", page_icon="🎁", layout="centered")

st.title("🔒 Private Birthday Vault")
st.write("To unlock this message, enter the exact date (Day and Month) a random Snapchat story after Iftari turned into the best friendship ever.")

password = st.text_input("Format: DD Month (e.g., 15 August)", "")

if password.strip().lower() in ["20 march", "march 20", "20th march", "20 march "]:
    st.balloons()
    st.success("Access Granted! Happy Birthday! 🎉")
    
    time.sleep(1)
    
    st.markdown("---")
    st.subheader("From Snapchat to Lifeline")
    st.write(
        "It is honestly crazy to think that we have never met in person, yet you know more about my life "
        "than almost anyone else. All because you saw my Snapchat story and added me on 20th March in Ramadan, "
        "right after Iftari and Maghrib prayer."
    )
    
    st.subheader("Official Relationship Referee")
    st.write(
        "Thank you for always having my back, and especially for being the ultimate peacekeeper between me and my wifey. "
        "Whenever we are angry or fighting, you somehow step in, calm both of us down, and get us back to normal. "
        "I genuinely don't know how you have the patience for my chaos, but I'm grateful you do."
    )
    
    st.subheader("The Verdict")
    st.info(
        "You are hands down the best friend I have ever had. Sometimes I genuinely wonder how someone as solid and "
        "pure-hearted as you even exists in this world. Have the best birthday—you deserve all the peace, happiness, "
        "and success in the world this year."
    )
    
elif password != "":
    st.error("Wrong date! Hint: Think back to Ramadan right after Maghrib.")
