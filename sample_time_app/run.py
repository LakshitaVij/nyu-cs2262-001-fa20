from flask import Flask
from datetime import datetime

app = Flask(__name__)

# Home route (optional)
@app.route('/')
def home():
    return "Welcome to the sample Flask app!"

# /time route to return the current time
@app.route('/time')
def time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Current time is: {current_time}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
