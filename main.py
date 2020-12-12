from typing import Optional
from fastapi import FastAPI, HTTPException
from db import db_nacionales, db_general

app = FastAPI()

@app.get("/")
async def root():
    return {"Mensaje": "Bienvenido - HOTEL PRICE SYSTEM MANAGEMENT Api"}

@app.get("/Temporada/")
async def obtener_temporada(ciudad: Optional[str] = None):
    if ciudad:
        Temporada = []
        if ciudad in db_nacionales.db_temporada_alta:
            Temporada.append(db_nacionales.db_temporada_alta[ciudad]) 
        else:
            Temporada = {'Message: En la ciudad especificada no contamos con sucursal'}
    else:
        Temporada = db_nacionales.db_temporada_alta
    return  Temporada

@app.post("/Temporada/crear/")
async def crear_temporada(temporada: db_nacionales.temporada):
    creada_exitosamente = db_nacionales.crear_temporada(temporada)
    if creada_exitosamente:
        return {"mensaje": "Temporada creada correctamente"}
    else:
        raise HTTPException(status_code = 400,
                            detail="Evento ya existe")

@app.get("/TemporadaGeneral/")
async def obtener_FiestaG():
    TemporadaGeneral = db_general.obtener_temporada_general()
    return  TemporadaGeneral
