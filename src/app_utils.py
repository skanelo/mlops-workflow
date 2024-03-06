"""Module containing utility functions for the Streamlit app."""

import io

import streamlit as st
import torch
from PIL import Image
from torchvision import transforms
from ultralytics import YOLO


def load_image():
    """Load an image from a file and return it as a PIL image."""
    uploaded_file = st.file_uploader(label="Pick an image to test")
    if uploaded_file:
        image_data = uploaded_file.getvalue()
        image = Image.open(io.BytesIO(image_data))
        st.image(image)
        return image
    else:
        return None


@st.cache_resource
def load_model(model_size: str):
    """Load the YOLO model."""
    model = YOLO(model_size)
    return model


def detect(model, image):
    """Detect objects in the image and display the results."""
    pass


def preprocess_image(image: Image.Image) -> torch.Tensor:
    """Preprocess the image for the model."""
    transform = transforms.Compose(
        [
            transforms.Resize((448, 640)),
            transforms.ToTensor(),
        ]
    )
    return transform(image)
