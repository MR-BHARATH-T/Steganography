import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# Function to open file dialog and select image
def select_image():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    return file_path

# Function to embed the message inside the image
def encrypt_message():
    # Select image file
    image_path = select_image()
    if not image_path:
        messagebox.showerror("Error", "No file selected. Please select an image.")
        return
    
    # Load image
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Unable to load the selected image.")
        return
    
    # Get message and passcode from the user
    message = simpledialog.askstring("Secret Message", "Enter the message to hide:")
    passcode = simpledialog.askstring("Passcode", "Enter a passcode for decryption:", show="*")
    
    if not message or not passcode:
        messagebox.showerror("Error", "Message or Passcode cannot be empty!")
        return
    
    # Encode message with passcode
    hidden_data = passcode + "|" + message + "\0"
    
    # Convert character to pixel values
    d = {chr(i): i for i in range(256)}
    
    n, m, z = 0, 0, 0
    height, width, _ = img.shape

    for char in hidden_data:
        img[n, m, z] = d[char]
        z = (z + 1) % 3  # Cycle through RGB
        if z == 0:
            m += 1
            if m == width:
                m = 0
                n += 1
                if n == height:
                    messagebox.showerror("Error", "Message too long for this image!")
                    return
    
    # Save encrypted image
    output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
    if output_path:
        cv2.imwrite(output_path, img)
        messagebox.showinfo("Success", f"Message successfully encrypted and saved as {output_path}")
    else:
        messagebox.showwarning("Warning", "Encryption cancelled. No file saved.")

# Create GUI window
root = tk.Tk()
root.withdraw()  # Hide the main window
encrypt_message()





# import streamlit as st
# import cv2
# import numpy as np

# # Set page title
# st.set_page_config(page_title="Encrypt Message", layout="centered")

# st.title("🔐 Encrypt Message into Image")

# uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

# message = st.text_area("Enter the secret message:")
# password = st.text_input("Enter a passcode:", type="password")

# if uploaded_file is not None and message and password:
#     # Read image
#     file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#     img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

#     # Encode message with passcode
#     hidden_data = password + "|" + message + "\0"

#     d = {chr(i): i for i in range(256)}

#     n, m, z = 0, 0, 0
#     height, width, _ = img.shape

#     for char in hidden_data:
#         img[n, m, z] = d[char]
#         z = (z + 1) % 3
#         if z == 0:
#             m += 1
#             if m == width:
#                 m = 0
#                 n += 1
#                 if n == height:
#                     st.error("Message too long for this image!")
#                     st.stop()

#     # Save encrypted image
#     output_filename = "encrypted_image.png"
#     cv2.imwrite(output_filename, img)
    
#     st.success("✅ Message successfully encrypted!")
#     with open(output_filename, "rb") as file:
#         st.download_button(label="⬇️ Download Encrypted Image", data=file, file_name="encrypted_image.png", mime="image/png")
