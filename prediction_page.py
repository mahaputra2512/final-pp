import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

def prediction_page():
    st.title("Cataract Prediction")
    interpreter = tf.lite.Interpreter(model_path='model.tflite')
    interpreter.allocate_tensors()


    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    uploaded_file = st.file_uploader("Choose an eye image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        image = image.resize((94, 55))
        image_array = np.array(image)
        image_array = image_array.astype(np.float32) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        interpreter.set_tensor(input_details[0]['index'], image_array)
        interpreter.invoke()
        prediction = interpreter.get_tensor(output_details[0]['index'])

        # Display prediction
        if prediction[0][0] > 0.5:
            st.success("No Cataract detected!")
        else:
            st.success("Cataract detected!")

if __name__ == "__main__":
    prediction_page()
