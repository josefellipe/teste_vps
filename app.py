from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

# Configurações do CORS
origins = ["*"]  # Ou você pode definir uma lista de origens permitidas aqui

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=JSONResponse)
async def custom_response():
    content = {"message": "Tá dando certo"}
    response = JSONResponse(content=content, status_code=200)
    return response

if __name__ == "__main__":
    uvicorn.run(
        app, host="0.0.0.0", port=8000
    )
