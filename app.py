import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image, ImageOps

# Set page configuration
st.set_page_config(
    page_title="Kidney Stone Detection",
    page_icon="🔍",
    layout="centered"
)

# Title and Description
st.title("Kidney Stone Detection using CNN+LSTM")
st.write("""
Upload a CT scan (axial/transverse view only supported) image of the kidney to detect the presence of kidney stones.
""")

# Load the model
@st.cache_resource  # Caches the model after the first load
def load_trained_model():
    model = load_model('kidney_stone_detector_final.keras')
    return model

model = load_trained_model()

# Display example images
st.subheader("Example Images for Testing")
col1, col2 = st.columns(2)
with col1:
    st.image("images/Normal- (1).jpg", caption="Normal Kidney", use_container_width=True)
with col2:
    st.image("images/Stone- (1).jpg", caption="Kidney with Stone", use_container_width=True)

# File uploader
uploaded_file = st.file_uploader("Choose a CT scan (axial/transverse view only supported) image...", type=["jpg", "jpeg", "png"])

def preprocess_image(image):
    # Convert the image to RGB if necessary
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Resize the image to 128x128
    image = image.resize((128, 128))

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Normalize the image
    image_array = image_array / 255.0

    # Handle grayscale images
    if image_array.shape[-1] == 1:
        image_array = np.stack((image_array,) * 3, axis=-1)

    # Expand dimensions to match model input
    image_array = np.expand_dims(image_array, axis=0)

    return image_array

if uploaded_file is not None:
    # Read the image file
    image = Image.open(uploaded_file)

    # Display the uploaded image
    st.image(image, caption='Uploaded Image', use_container_width=True)

    # Preprocess the image
    preprocessed_image = preprocess_image(image)

    # Make prediction
    prediction = model.predict(preprocessed_image)
    probability = prediction[0][0]
    result = "Kidney Stone Detected" if probability > 0.5 else "No Kidney Stone Detected"

    # Display the prediction
    st.write(f"## Prediction: {result}")
    st.write(f"### Probability: {probability:.2f}")

    # Provide interpretation
    if probability > 0.5:
        st.warning("The model predicts that there is a kidney stone present.")
    else:
        st.success("The model predicts that there is no kidney stone present.")
else:
    st.info("Please upload an image file to get a prediction.")
