import streamlit as st
import re
import string
import random

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Uppercase and lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Special character check
    if re.search(r"[@#$%^&*!]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Strength Check
    if score == 4:
        return "✅ Strong Password!", score, feedback
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", score, feedback
    else:
        return "❌ Weak Password - Improve it using the suggestions above.", score, feedback

def generate_strong_password():
    length = 12 
    characters = string.ascii_letters + string.digits + "@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.set_page_config(page_icon="🔓", page_title="Password Strength Checker")
st.title("🔓 Password Strength Meter App")

password = st.text_input("Enter Your Password:", type="password")

if password:
    strength_msg, score, feedback = check_password_strength(password)
    st.markdown(f"**{strength_msg}**")

    if score < 4:
        for tip in feedback:
            st.markdown(f"- {tip}")

        # Suggest a strong password
        st.markdown("### ⚡ Suggested Strong Password:")
        st.code(generate_strong_password(), language="python")
