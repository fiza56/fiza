import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model
# Example of loading a pre-trained model 
model = load_model('path_to_trained_model.h5')
def generate_digit_images(digit):
    # Here you may want to predict or randomly generate images from the specified digit
    images = [ ]
    for _ in range (5):
        # generate or predict an image of the specified digit 
        images.append(np.random.rand(28, 28))
    return images
def main():
       st.title("Handwritten Digit Image Generator")
       digit = st.number_input("Choose a digit to generate (0-9)", 0, 9)
       
       if st.button("Generate"):
           images = generate_digit_images(digit)
           for i, img in enumerate(images):
               plt.imshow(img, cmap='gray')
               plt.axis('off')
               st.pyplot(plt)

if __name__ == "__main__": 
       main()
   