from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello, World!!!"}

if __name__ == "__main__":
    uvicorn.run(
        host="89.117.33.83", 
        port=8000
        )
