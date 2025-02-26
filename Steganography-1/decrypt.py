import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# Function to open file dialog and select encrypted image
def select_image():
    file_path = filedialog.askopenfilename(title="Select Encrypted Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    return file_path

# Function to decrypt the hidden message from an image
def decrypt_message():
    # Select encrypted image file
    image_path = select_image()
    if not image_path:
        messagebox.showerror("Error", "No file selected. Please select an encrypted image.")
        return
    
    # Load image
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Unable to load the selected image.")
        return

    # Define character mappings
    c = {i: chr(i) for i in range(256)}

    # Extract the message from the image
    message = ""
    n, m, z = 0, 0, 0
    height, width, _ = img.shape

    while True:
        try:
            char = c[img[n, m, z]]

            # Stop extraction if null character is found
            if char == '\0':
                break

            message += char

            z = (z + 1) % 3
            if z == 0:
                m += 1
                if m == width:
                    m = 0
                    n += 1
                    if n == height:
                        break
        except:
            messagebox.showerror("Error", "Failed to extract the hidden message.")
            return

    # Ensure message format is correct
    if '|' not in message:
        messagebox.showerror("Error", "Invalid encrypted data format. Decryption failed.")
        return

    # Extract passcode and actual message
    stored_passcode, decrypted_message = message.split('|', 1)

    # Ask for passcode
    entered_passcode = simpledialog.askstring("Passcode", "Enter passcode for decryption:", show="*")

    # Verify passcode
    if entered_passcode == stored_passcode:
        messagebox.showinfo("Decryption Successful", f"Hidden Message:\n{decrypted_message}")
    else:
        messagebox.showerror("Access Denied", "Incorrect passcode!")

# Create GUI window
root = tk.Tk()
root.withdraw()  # Hide the main window
decrypt_message()





# import streamlit as st
# import cv2
# import numpy as np

# # Set page title
# st.set_page_config(page_title="Decrypt Message", layout="centered")

# st.title("🔓 Decrypt Message from Image")

# uploaded_file = st.file_uploader("Upload the encrypted image...", type=["png", "jpg", "jpeg"])

# if uploaded_file is not None:
#     # Read image
#     file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#     img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

#     # Define character mappings
#     c = {i: chr(i) for i in range(256)}

#     # Extract the message
#     message = ""
#     n, m, z = 0, 0, 0
#     height, width, _ = img.shape

#     while True:
#         try:
#             char = c[img[n, m, z]]
#             if char == '\0':
#                 break
#             message += char

#             z = (z + 1) % 3
#             if z == 0:
#                 m += 1
#                 if m == width:
#                     m = 0
#                     n += 1
#                     if n == height:
#                         break
#         except:
#             st.error("Failed to extract the hidden message.")
#             st.stop()

#     if '|' not in message:
#         st.error("Invalid encrypted data format. Decryption failed.")
#         st.stop()

#     # Extract passcode and actual message
#     stored_passcode, decrypted_message = message.split('|', 1)

#     # Ask for passcode
#     entered_passcode = st.text_input("Enter passcode for decryption:", type="password")

#     if st.button("🔓 Decrypt"):
#         if entered_passcode == stored_passcode:
#             st.success("✅ Decryption Successful!")
#             st.text_area("Hidden Message:", decrypted_message, height=150)
#         else:
#             st.error("❌ Incorrect passcode!")
