from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routers import temporadas, hoteles, usuarios

app = FastAPI()

origins = [
    "https://api-hotel-season.herokuapp.com/",
    "https://hotel-season.herokuapp.com/"
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(temporadas.router)
app.include_router(hoteles.router)
app.include_router(usuarios.router)

@app.get("/", tags = ["Principal"])
async def root():
    return {"Mensaje": "Bienvenido - HOTEL PRICE SYSTEM MANAGEMENT Api"}
