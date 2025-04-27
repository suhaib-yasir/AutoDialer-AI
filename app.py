from flask import Flask
from main import main
from call_handler import find_contact, simulate_call
from tts_feedback import speak

app = Flask(__name__)

@app.route("/start")
def start():
    message = main(use_adb=False)  # Use web-based method by default
    return message

@app.route("/emergency")
def call_emergency():
    contact = find_contact("emergency")
    message = simulate_call(contact, use_adb=False)
    speak(message)
    return message

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)