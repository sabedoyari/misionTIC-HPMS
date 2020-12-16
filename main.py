from typing import Optional
from fastapi import FastAPI, HTTPException
from db import db_nacionales, db_general
from fastapi.middleware.cors import CORSMiddleware

from time import mktime
from datetime import datetime

app = FastAPI()

origins = [
    "https://santi-hpsm.herokuapp.com/",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/Temporada/ciudadfecha/")
async def obtener_temporada_ciudad_fecha(ciudad: Optional[str] = None, fecha: Optional[str] = None):
    fecha = mktime(datetime.strptime(fecha, "%d-%m-%Y").timetuple())
    if ciudad:
        Temporada = []
        if ciudad in db_nacionales.db_temporada_alta:
            fecha_inicio = mktime(datetime.strptime(db_nacionales.db_temporada_alta[ciudad].fecha_inicio, "%d-%m-%Y").timetuple())
            fecha_fin = mktime(datetime.strptime(db_nacionales.db_temporada_alta[ciudad].fecha_inicio, "%d-%m-%Y").timetuple())
            if fecha >= fecha_inicio and fecha <= fecha_fin:
                Temporada.append(db_nacionales.db_temporada_alta[ciudad])
            else: 
                Temporada = {'Message': 'Por la época especificada, la ciudad no se encuentra en temporada alta'}
        else:
            Temporada = {'Message': 'En la ciudad especificada no contamos con sucursal'}
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
