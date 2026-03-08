from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, Flask server is running!</h1>"

# Run the server
if __name__ == "__main__":
    # debug=True enables auto-reload on code changes
    app.run(host="0.0.0.0", port=5000, debug=True)