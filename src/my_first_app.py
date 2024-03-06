"""Module that contains the Streamlit app."""
import streamlit as st
from app_utils import load_image, load_model, preprocess_image
from matplotlib import pyplot as plt
from torchvision.utils import draw_bounding_boxes


def main():
    """Main function of the app."""
    st.title("Image upload demo")

    model = load_model("yolov8s.pt")
    image = load_image()
    # image = Image.open("/home/skanelo/Desktop/dog_person.jpg")
    result = st.button("Run on image")
    if result and image:
        st.write("General Results...")

        original_image_tensor = preprocess_image(image)
        results = model.predict(original_image_tensor.unsqueeze(0), verbose=False)
        class_mapping = results[0].names
        predicted_classes = [
            class_mapping[int(label)] for label in results[0].boxes.cls
        ]
        predicted_confidences = results[0].boxes.conf

        predicted_boxes = results[0].boxes.xyxy

        img_with_bboxes = draw_bounding_boxes(
            (original_image_tensor * 255.0).byte(),
            predicted_boxes,
            colors="yellow",
            labels=predicted_classes,
        )

        fig = plt.figure(figsize=(12, 8))
        plt.imshow(img_with_bboxes.permute(1, 2, 0).numpy())
        plt.xticks([])
        plt.yticks([])

        st.pyplot(fig, use_container_width=True)

        st.header("Detected Objects")
        for i, (label, confidence) in enumerate(
            zip(predicted_classes, predicted_confidences)
        ):
            st.write(f"{i+1}. {label} ({confidence:.2f})")


if __name__ == "__main__":
    main()
