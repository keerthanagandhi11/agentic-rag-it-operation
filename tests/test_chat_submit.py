import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "project"))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from ui.gradio_app import create_gradio_ui


def test_chat_submit_events_are_registered():
    demo = create_gradio_ui()
    dependencies = demo.config["dependencies"]

    submit_events = [
        dep for dep in dependencies
        if dep.get("targets") and dep["targets"][0][1] == "submit"
    ]
    send_clicks = [
        dep for dep in dependencies
        if dep.get("targets")
        and dep["targets"][0][1] == "click"
        and dep.get("api_name") == "chat_handler_1"
    ]

    assert submit_events, "The chat textbox submit event is missing."
    assert send_clicks, "The Send button click handler is missing."
