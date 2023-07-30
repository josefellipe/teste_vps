from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get("/", response_class=JSONResponse)
async def custom_response():
    content = {"message": "Tá dando certo"}
    response = JSONResponse(
        content=content, 
        status_code=200, 
        headers={"Access-Control-Allow-Origin": "*"}
    )
    return response


if __name__ == "__main__":
    uvicorn.run(
        host="89.117.33.83", 
        port=8000
        )
