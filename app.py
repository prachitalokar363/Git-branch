from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "updated Flask sample application on azure hghapp service updated version-6"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="1.2.3.4", port=port, debug=False)
