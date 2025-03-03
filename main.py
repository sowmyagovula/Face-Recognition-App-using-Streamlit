import streamlit as st
import cv2
import face_recognition
import numpy as np
from PIL import Image

# Function to load and encode the face
def encode_face(image_file):
    image = Image.open(image_file)
    image = np.array(image)  # Convert to NumPy array
    face_encodings = face_recognition.face_encodings(image)
    
    if len(face_encodings) > 0:
        return face_encodings[0]  # Return first face encoding
    else:
        return None  # No face found

# Streamlit UI
st.title("Face Matching with Camera Capture or Image Upload")

# Capture or Upload Reference Image
st.subheader("Reference Image")
ref_img_option = st.radio("Choose an option to provide the reference image:", ("Capture with Camera", "Upload Image"))
if ref_img_option == "Capture with Camera":
    ref_img_file = st.camera_input("Take a reference image")
else:
    ref_img_file = st.file_uploader("Upload a reference image", type=["jpg", "jpeg", "png"])

# Capture or Upload Destination Image
st.subheader("Destination Image")
# dest_img_option = st.radio("Choose an option to provide the destination image:", ("Capture with Camera", "Upload Image"))
# if dest_img_option == "Capture with Camera":
dest_img_file = st.camera_input("Take a destination image")
# else:
#     dest_img_file = st.file_uploader("Upload a destination image", type=["jpg", "jpeg", "png"])

# Start Matching Button
if st.button("Start Matching"):
    if ref_img_file and dest_img_file:
        # Encode faces
        ref_encoding = encode_face(ref_img_file)
        dest_encoding = encode_face(dest_img_file)

        if ref_encoding is not None and dest_encoding is not None:
            # Compare faces
            match = face_recognition.compare_faces([ref_encoding], dest_encoding)
            distance = face_recognition.face_distance([ref_encoding], dest_encoding)[0]

            # Display images
            st.image([ref_img_file, dest_img_file], caption=["Reference Image", "Destination Image"], width=300)

            # Show match result
            if match[0]:
                st.success(f"✅ Face Matched! (Similarity Score: {round(1 - distance, 2)})")
            else:
                st.error(f"❌ Face Not Matched! (Difference Score: {round(distance, 2)})")
        else:
            st.warning("⚠ No face detected in one or both images. Please try again.")
    else:
        st.warning("⚠ Please provide both images before starting the match.")