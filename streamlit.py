import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Function to load the EfficientNet model
@st.cache_resource
def load_efficientnet_model():
    model = load_model('efficientnet_model.h5')
    return model

# Function to preprocess the uploaded image
def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image)
    image = image / 255.0  # Rescale the image
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Class labels (Replace these with your actual class names)
class_names = ['Aipan Art', 'Assamese Miniature Painting', 'Basholi Painting',
               'Bhil Painting', 'Chamba Rumal', 'Cheriyal Scroll Painting',
               'Dokra Art', 'Gond Painting', 'Kalamkari Painting',
               'Kalighat Painting', 'Kangra Painting', 'Kerala Mural Painting',
               'Kondapalli Bommallu', 'Kutch Lippan Art', 'Leather Puppet Art',
               'Madhubani Painting', 'Mandala Art', 'Mandana Art', 'Mata Ni Pachedi',
               'Meenakari Painting', 'Mughal Paintings', 'Mysore Ganjifa Art', 'Pattachitra Painting',
               'Patua Painting', 'Pichwai Painting', 'Rajasthani Miniature Painting', 'Rogan Art from Kutch',
               'Sohrai Art', 'Tikuli Art', 'Warli Folk Painting']

# Class information
class_info = {
    'Aipan Art': 'Aipan Art originated from Uttarakhand, India.',
    'Assamese Miniature Painting': 'Assamese Miniature Painting is an art form from the state of Assam, India.',
    'Basholi Painting': 'Basholi Painting is a style of miniature painting from the Jammu region of Jammu and Kashmir, India.',
    'Bhil Painting': 'Bhil Painting is a traditional art form practiced by the Bhil tribe in Madhya Pradesh, India.',
    'Chamba Rumal': 'Chamba Rumal is a style of embroidered cloth originating from Chamba district in Himachal Pradesh, India.',
    'Cheriyal Scroll Painting': 'Cheriyal Scroll Painting is a traditional art form from Telangana, India, depicting narratives on long scrolls.',
    'Dokra Art': 'Dokra Art is a non-ferrous metal casting art form practiced in West Bengal, India.',
    'Gond Painting': 'Gond Painting is a traditional art form of the Gond tribe from Madhya Pradesh, India.',
    'Kalamkari Painting': 'Kalamkari Painting is a traditional style of hand-painted or block-printed cotton textile from Andhra Pradesh and Telangana, India.',
    'Kalighat Painting': 'Kalighat Painting is a style of Indian painting that originated in the Kalighat temple area in West Bengal, India.',
    'Kangra Painting': 'Kangra Painting is a style of miniature painting that originated in the Kangra district of Himachal Pradesh, India.',
    'Kerala Mural Painting': 'Kerala Mural Painting is a traditional mural art form from the state of Kerala, India.',
    'Kondapalli Bommallu': 'Kondapalli Bommallu are traditional toys and dolls made from wood in the Kondapalli village of Andhra Pradesh, India.',
    'Kutch Lippan Art': 'Kutch Lippan Art is a traditional art form of decorating mud walls and floors with intricate patterns, practiced in the Kutch region of Gujarat, India.',
    'Leather Puppet Art': 'Leather Puppet Art is a traditional form of puppetry using leather puppets, practiced in Andhra Pradesh, India.',
    'Madhubani Painting': 'Madhubani Painting is a style of Indian painting practiced in the Madhubani district of Bihar, India.',
    'Mandala Art': 'Mandala Art is a spiritual and ritual art form involving the creation of intricate circular designs, with origins in various Indian traditions.',
    'Mandana Art': 'Mandana Art is a traditional art form of decorating floors and walls with intricate designs, practiced in Rajasthan, India.',
    'Mata Ni Pachedi': 'Mata Ni Pachedi is a traditional art form involving narrative paintings depicting Hindu goddesses, originating from Gujarat, India.',
    'Meenakari Painting': 'Meenakari Painting is a traditional art form of enameling and decorating metal surfaces, practiced in Rajasthan, India.',
    'Mughal Paintings': 'Mughal Paintings are a style of miniature painting that flourished during the Mughal Empire in the Indian subcontinent.',
    'Mysore Ganjifa Art': 'Mysore Ganjifa Art is a traditional art form of hand-painted playing cards, originating from the city of Mysore in Karnataka, India.',
    'Pattachitra Painting': 'Pattachitra Painting is a traditional cloth-based scroll painting from the states of Odisha and West Bengal, India.',
    'Patua Painting': 'Patua Painting is a traditional art form of scroll painting practiced by the Patua community in West Bengal, India.',
    'Pichwai Painting': 'Pichwai Painting is a traditional style of textile painting depicting Hindu deities, originating from Rajasthan, India.',
    'Rajasthani Miniature Painting': 'Rajasthani Miniature Painting is a style of miniature painting that originated and flourished in the state of Rajasthan, India.',
    'Rogan Art from Kutch': 'Rogan Art is a traditional art form of decorating fabrics with intricate patterns using a mix of castor oil and natural pigments, practiced in the Kutch region of Gujarat, India.',
    'Sohrai Art': 'Sohrai Art is a traditional art form of wall painting practiced by the Sohrai tribal community in Jharkhand, India.',
    'Tikuli Art': 'Tikuli Art is a traditional art form of creating intricate designs and patterns using natural colors on walls and floors, practiced in Bihar, India.',
    'Warli Folk Painting': 'Warli Folk Painting is a traditional art form of the Warli tribe depicting scenes from daily life, originating from Maharashtra, India.'
}

# Streamlit UI
st.title("Automated Recognition of Indian Folk Art")
st.write("Upload an image of folk art, and the model will predict its category.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load and preprocess the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    model = load_efficientnet_model()
    processed_image = preprocess_image(image)

    # Make prediction
    predictions = model.predict(processed_image)
    predicted_class = np.argmax(predictions[0])
    accuracy = np.max(predictions[0])

    # Get art style/origin information
    predicted_class_name = class_names[predicted_class]
    art_info = class_info.get(predicted_class_name, "No information available for this class.")

    # Display results
    st.write(f"Predicted Class: {predicted_class_name}")
    st.write(f"Confidence: {accuracy:.2f}")
    st.write(f"Art Style/Origin: {art_info}")




#streamlit run d:/arifa/Isha.py --server.enableXsrfProtection false