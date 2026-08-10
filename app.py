from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>ClarityFlow AI is LIVE!</h1><p>Your application is working.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
