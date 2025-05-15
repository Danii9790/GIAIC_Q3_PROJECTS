import streamlit as st
import hashlib
from cryptography.fernet import Fernet
import base64
import json
import os

# File to store encrypted data
DATA_FILE = "store.json"

# Generate or load encryption key
if 'fernet_key' not in st.session_state:
    key = os.getenv("FERNET_KEY", Fernet.generate_key().decode())
    st.session_state.fernet_key = key.encode()
    st.session_state.cipher = Fernet(st.session_state.fernet_key)

# Load/save functions
def load_data():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
    except Exception:
        return {}
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f,indent=4)

# Initialize data
if 'stored_data' not in st.session_state:
    st.session_state.stored_data = load_data()

if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0

if 'locked_out' not in st.session_state:
    st.session_state.locked_out = False

# Encryption functions
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text):
    try:
        encrypted = st.session_state.cipher.encrypt(text.encode())
        return base64.urlsafe_b64encode(encrypted).decode()
    except Exception as e:
        st.error(f"Encryption error: {str(e)}")
        return None

def decrypt_data(encrypted_text, passkey):
    try:
        hashed_passkey = hash_passkey(passkey)
        decoded = base64.urlsafe_b64decode(encrypted_text.encode())
        decrypted = st.session_state.cipher.decrypt(decoded).decode()
        
        # Verify passkey matches any entry with this encrypted text
        for entry_data in st.session_state.stored_data.values():
            if (entry_data["encrypted_text"] == encrypted_text and 
                entry_data["passkey"] == hashed_passkey):
                st.session_state.failed_attempts = 0
                return decrypted
        
        st.session_state.failed_attempts += 1
        if st.session_state.failed_attempts >= 3:
            st.session_state.locked_out = True
        return None
        
    except Exception as e:
        st.error(f"Decryption error: {str(e)}")
        st.session_state.failed_attempts += 1
        if st.session_state.failed_attempts >= 3:
            st.session_state.locked_out = True
        return None

# UI
st.title("🔒 Secure Data Encryption System")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("Secure Data Storage")
    st.write("Encrypt and decrypt data using passkeys")

elif choice == "Store Data":
    st.subheader("📥 Store Data")
    user_data = st.text_area("Data to encrypt:")
    passkey = st.text_input("Create passkey:", type="password")
    
    if st.button("Encrypt & Store"):
        if user_data and passkey:
            encrypted_text = encrypt_data(user_data)
            if encrypted_text:
                st.session_state.stored_data[encrypted_text] = {
                    "encrypted_text": encrypted_text,
                    "passkey": hash_passkey(passkey)
                }
                save_data(st.session_state.stored_data)
                st.success("Data encrypted!")
                st.code(encrypted_text)
        else:
            st.error("Both fields are required")

elif choice == "Retrieve Data":
    if st.session_state.locked_out:
        st.warning("🔒 Account locked - please login")
        st.stop()
        
    st.subheader("📤 Retrieve Data")
    encrypted_text = st.text_area("Paste encrypted data:")
    passkey = st.text_input("Enter passkey:", type="password")
    
    if st.button("Decrypt"):
        if encrypted_text and passkey:
            decrypted = decrypt_data(encrypted_text, passkey)
            if decrypted:
                st.success("Decrypted successfully!")
                st.text_area("Decrypted data:", decrypted, height=200)
            else:
                remaining = 3 - st.session_state.failed_attempts
                st.error(f"Invalid passkey! {remaining} attempts left")
        else:
            st.error("Both fields are required")

elif choice == "Login":
    st.subheader("🔑 Login Required")
    password = st.text_input("Admin password:", type="password")
    
    if st.button("Unlock"):
        if password == "admin123":
            st.session_state.failed_attempts = 0
            st.session_state.locked_out = False
            st.success("Account unlocked!")
        else:
            st.error("Incorrect password")