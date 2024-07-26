import common
import gradio as gr

# Create Gradio interface
gr_interface = gr.Interface(
    fn=common.get_response,
    inputs=gr.components.Textbox(lines=2, placeholder="Enter your question here"),
    outputs="text",
    examples=[
        ["What are the seven wonders?"],
        ["What does the Rhodes Statue look like?"],
        ["Tell me about the Mausoleum."],
    ],
)
gr_interface.launch()
