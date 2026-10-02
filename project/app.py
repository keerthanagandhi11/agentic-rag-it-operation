import sys
import os
import logging
import gradio as gr

sys.path.insert(0, os.path.dirname(__file__))

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

# Suppress OTel "Failed to detach context" warning caused by generator/context interaction.
# Tracing is unaffected.
# Known bug: https://github.com/open-telemetry/opentelemetry-python/issues/2606
class _SuppressOtelDetachWarning(logging.Filter):
    def filter(self, record):
        return "Failed to detach context" not in record.getMessage()

logging.getLogger("opentelemetry.context").addFilter(_SuppressOtelDetachWarning())

from ui.css import custom_css
from ui.gradio_app import create_gradio_ui

if __name__ == "__main__":
    print("\n🔨 Creating RAG Assistant...")
    demo = create_gradio_ui()
    print("\n🚀 Launching RAG Assistant...")
    dark_theme = gr.themes.Base(
        primary_hue="blue",
        secondary_hue="blue",
        neutral_hue="zinc",
    ).set(
        body_background_fill="#0f0f0f",
        body_text_color="#e5e5e5",
        background_fill_primary="#0f0f0f",
        background_fill_secondary="#1a1a1a",
        block_background_fill="#1a1a1a",
        block_label_background_fill="#1a1a1a",
        block_label_text_color="#e5e5e5",
        input_background_fill="#1a1a1a",
        input_background_fill_focus="#1a1a1a",
    )
    demo.launch(css=custom_css, theme=dark_theme)