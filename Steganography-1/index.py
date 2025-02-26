import streamlit as st
import subprocess

# Set page title and icon
st.set_page_config(page_title="Steganography Tool", page_icon="🔐", layout="wide")

# Custom CSS for background styling and button alignment
st.markdown(
    """
    <style>
        /* Set Background Image */
        .stApp {
            background-image: url('https://media.istockphoto.com/id/1422766384/photo/cybersecurity-concept-user-privacy-security-and-encryption-secure-internet-access-future.jpg?s=1024x1024&w=is&k=20&c=h3_vpAyz1BOvJmvL-b1t1abXFDRJUnZZgIsxgrtOxbw=');
            background-size: cover;
            background-position: center;
        }
        
        /* Main Container */
        .main-container {
            background: rgba(0, 0, 0, 0.8);
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            color: white;
        }

        /* Title Styling */
        .title {
            font-size: 38px;
            font-weight: bold;
            color: #00FF00;
            text-align: center;
            margin-bottom: 10px;
        }

        /* Button Styling */
        .stButton>button {
            background-color: #000000;
            color: white;
            font-size: 20px;
            padding: 12px 24px;
            border-radius: 8px;
            margin-top: 10px;
            border: none;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #005f73;
        }

        /* Center the buttons */
        .button-container {
            display: flex;
            justify-content: center;
            gap: 30px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# UI Layout
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown('<p class="title">🔐 Steganography Encryption & Decryption Tool 🔓</p>', unsafe_allow_html=True)

st.write("### Hide & Extract Secret Messages from Images using Steganography")

# Create columns for buttons
col1, col2 = st.columns(2)

# Encrypt Button
with col1:
    if st.button("🔒 Encrypt Message"):
        subprocess.run(["python", "encrypt.py"])  # Runs encrypt.py

# Decrypt Button
with col2:
    if st.button("🔓 Decrypt Message"):
        subprocess.run(["python", "decrypt.py"])  # Runs decrypt.py

st.markdown('</div>', unsafe_allow_html=True)


# import streamlit as st
# import subprocess

# # Set page config
# st.set_page_config(page_title="Steganography Tool", layout="centered")

# # Background image styling
# page_bg = """
# <style>
# [data-testid="stAppViewContainer"] {
#     background-image: url("https://source.unsplash.com/1600x900/?technology,security");
#     background-size: cover;
# }
# </style>
# """
# st.markdown(page_bg, unsafe_allow_html=True)

# # Title
# st.markdown("<h1 style='text-align: center; color: white;'>Steganography Tool 🔒</h1>", unsafe_allow_html=True)

# # Encrypt & Decrypt Buttons
# col1, col2 = st.columns(2)

# with col1:
#     if st.button("🔐 Encrypt Message"):
#         subprocess.run(["streamlit", "run", "encrypt.py"])

# with col2:
#     if st.button("🔓 Decrypt Message"):
#         subprocess.run(["streamlit", "run", "decrypt.py"])

# st.markdown("<h5 style='text-align: center; color: white;'>Select an option to proceed</h5>", unsafe_allow_html=True)





# import streamlit as st
# import os
# import sys

# st.set_page_config(page_title="Steganography Tool", layout="centered")

# st.title("🔒 Steganography Tool")

# col1, col2 = st.columns(2)

# with col1:
#     if st.button("🔐 Encrypt Message"):
#         os.system(f"{sys.executable} -m streamlit run encrypt.py")

# with col2:
#     if st.button("🔓 Decrypt Message"):
#         os.system(f"{sys.executable} -m streamlit run decrypt.py")
