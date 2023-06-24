# app.py
import gradio as gr


def fahrenheit_to_celsius(fahrenheit):
    celsius = (int(fahrenheit) - 32) * 5 / 9
    return celsius


iface = gr.Interface(
    fn=fahrenheit_to_celsius,
    inputs="text",
    outputs="text",
    title="Fahrenheit to Celsius Converter",
    description="Converts temperature from Fahrenheit to Celsius",
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0")
