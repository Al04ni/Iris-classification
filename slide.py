import streamlit as st
from PIL import Image
import os
import time

# Title of the app
with st.container(border=True):
 st.markdown("*Image Slideshow with Uniform Size*")

 # Get the base directory
 base_dir = os.path.dirname(__file__)

 # List of image paths from different folders
 images = [
    os.path.join(base_dir, "images/pic1.jpg"),
    os.path.join(base_dir, "images/pic2.jpg"),
    os.path.join(base_dir, "images/pic3.jpg"),
    os.path.join(base_dir, "images/pic4.jpg"),
    os.path.join(base_dir, "images/pic5.jpg"),
    os.path.join(base_dir, "images/pic6.jpg")
 ]

 # Desired width and height for all images
 width, height = 400, 300

 # Initialize the slide index in session state
 if 'slide_index' not in st.session_state:
    st.session_state.slide_index = 0

 # Function to update the slide index
 def update_slide():
    st.session_state.slide_index = (st.session_state.slide_index + 1) % len(images)

 # Run the slideshow
 while True:
    # Load the current image and resize it
    img = Image.open(images[st.session_state.slide_index])
    img = img.resize((width, height))

    # Center the image using columns
    col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the column ratio to center the image
    with col2:
        st.image(img, use_column_width=True)

    # Wait for 2 seconds
    time.sleep(2)

    # Update the slide index
    update_slide()

    # Rerun the Streamlit script to update the image
    st.experimental_rerun()
