import streamlit as st
import numpy as np
from PIL import Image
import os
import time
import pickle

st.set_page_config(
    page_title="Iris Species",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="auto",
)

# Load the saved model
@st.cache_resource  # Caches the model to avoid reloading every time
def load_model():
    try:
        with open('notebook/model.pkl', 'rb') as file:
          model = pickle.load(file)
        st.success('Model loaded successfully')
        return model
        
    except Exception as e:
       st.error(f'Error loading the model:{str(e)}')
       return None

# Load the model
model = load_model()
if model is None:
   st.stop()

# Function to get and transform user input
def get_user_input(petal_length, petal_width):
     input_list = [petal_length, petal_width]
     input_array = np.array(input_list)

     input_2d = input_array.reshape(1, -1)
     return input_2d
def main():
 #head
 st.title('Predicting Iris Flower Species: A Seamless Experience')
 #introduction
 st.markdown('*This project brings the elegance of nature and the power of technology together, offering a sophisticated solution to identify different iris flower species with remarkable accuracy.By leveraging the renowned Iris dataset, this project provides an intuitive and interactive platform that makes predicting iris species accessible and engaging for everyone.*')
 #video about the iris
 st.video('assets/iris_flowers.mp4')

 st.markdown('''
*With a user-friendly interface developed using Jupyter Notebook and Streamlit, this project allows users to effortlessly enter flower measurements and receive instant predictions. 
The streamlined process ensures that even those with little to no background in data science can appreciate and utilize the power of machine learning.
This project is a perfect demonstration of how technology can simplify complex tasks, making it easier for educators, hobbyists, and professionals alike to explore the beauty of iris species classification.*''')
 #model form
 with st.form('my_model'):
    st.subheader("The Iris Flower Measurements")
    
    # Input fields for flower measurements
    petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
    petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)
    
    # Submit button inside the form
    submitted = st.form_submit_button("Predict Species")
    st.markdown("---")
    # If the form is submitted
    if submitted:
      if petal_length <= 0 or petal_width <=0:
         st.warning('Please enter valid measurements')
      else: 
         input_data = get_user_input(petal_length, petal_width)
    
    try:
       
       # Make prediction using the loaded model
       prediction = model.predict(input_data)
    
       # Map prediction to species name (assuming 0 = Iris-setosa, 1 = Iris-versicolor, etc.)
       species_mapping = {0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'}
       predicted_species = species_mapping.get(prediction[0], 'Unknown')
    
       # Display the prediction
       st.success(f"The predicted species is: {predicted_species}")
       st.write(f"Petal Length: {petal_length} cm")
       st.write(f"Petal Width: {petal_width} cm")
    except Exception as e:
       st.error(f"Error making prediction: {str(e)}")
    

   #discalimer 
 with st.expander('More :)'):
         st.caption('''The Iris Classification project is more than just a technical exercise—it's a testament to the power of simplicity and innovation. 
 By making advanced technology accessible through an easy-to-use platform, this project empowers users to explore and understand the natural world in a new way. 
 Whether used for educational purposes or simply to satisfy curiosity, this project leaves a lasting impact, showcasing the future of user-friendly technological solutions.''')
 #model stuffs




if __name__ == '__main__': 
    main()

 #######################################################
 #slide section
 #######################################################
 
with st.container(border=True):
     st.markdown("*Image Slideshow of Iris fowers species: Iris Satosa, Iris versicolor and Iris Virginica.*")
     # Get the base directory
     base_dir = os.path.dirname(__file__)
     # List of image paths from different folders 
     images = [
         os.path.join(base_dir, "assets/pic1.jpg"),
         os.path.join(base_dir, "assets/pic2.jpg"),
         os.path.join(base_dir, "assets/pic3.jpg"),
         os.path.join(base_dir, "notebook/images/Softmax_regression_decision_boundaries.png"),
         os.path.join(base_dir, "assets/pic4.jpg"),
         os.path.join(base_dir, "assets/pic5.jpg"),
         os.path.join(base_dir, "assets/pic6.jpg")
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

      # Center the image using columns
      col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the column ratio to center the image
      with col2:
        st.image(img, use_container_width=True)

      # Wait for 2 seconds
      time.sleep(2)
      st.markdown(
        """
        <hr style="border: none; border-top: 1px solid #ccc; margin: 20px 0;">
        <p style="text-align: center; font-size: 14px;">
        <span>Developed with ❤️ from Kigali, Rwanda.</span>
        </p>
        """,
        unsafe_allow_html=True,
        )
      # Update the slide index
      update_slide()

      # Rerun the Streamlit script to update the image
      st.rerun()



