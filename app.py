from flask import Flask
import uvicorn

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    uvicorn.run(host="0.0.0.0", port=5000)
