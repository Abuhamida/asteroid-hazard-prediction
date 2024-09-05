import pickle
import gradio as gr
import pandas as pd

filename = 'Hazardous'
loaded_model = pickle.load(open(filename, 'rb'))


def predict_hazardous(absolute_magnitude, estimated_diameter_min, estimated_diameter_max, relative_velocity, miss_distance):
    """
    Predicts whether an asteroid is hazardous based on input features.
    """
    # Create a DataFrame with the input features
    input_data = pd.DataFrame({
        'absolute_magnitude': [absolute_magnitude],
        'estimated_diameter_min': [estimated_diameter_min],
        'estimated_diameter_max': [estimated_diameter_max],
        'relative_velocity': [relative_velocity],
        'miss_distance': [miss_distance]
    })

    # Make the prediction
    prediction = loaded_model.predict(input_data)[0]

    # Return the prediction
    return "Hazardous" if prediction == 1 else "Not Hazardous"

# Create the Gradio interface using the updated syntax
inputs = [
    gr.Number(label="Absolute Magnitude"),
    gr.Number(label="Estimated Diameter Min"),
    gr.Number(label="Estimated Diameter Max"),
    gr.Number(label="Relative Velocity"),
    gr.Number(label="Miss Distance"),
]

output = gr.Textbox(label="Prediction")

iface = gr.Interface(
    fn=predict_hazardous,
    inputs=inputs,
    outputs=output,
    title="Asteroid Hazard Prediction",
    description="Predict if an asteroid is hazardous based on its characteristics."
)

# Launch the interface
iface.launch(share=True)


