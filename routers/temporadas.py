from typing import Optional
from fastapi import APIRouter, HTTPException
from db import db_nacionales, db_general
from fastapi.middleware.cors import CORSMiddleware

from time import mktime
from datetime import datetime

router = APIRouter

origins = [
    "https://santi-hpsm.herokuapp.com/",
    "http://localhost",
    "http://localhost:8080",
]

router.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@router.get("/Temporada/")
async def obtener_temporada(ciudad: Optional[str] = None):
    if ciudad:
        Temporada = []
        if ciudad in db_nacionales.db_temporada_alta:
            Temporada.routerend(db_nacionales.db_temporada_alta[ciudad]) 
        else:
            Temporada = {'Message: En la ciudad especificada no contamos con sucursal'}
    else:
        Temporada = db_nacionales.db_temporada_alta
    return  Temporada

@router.get("/Temporada/ciudadfecha/")
async def obtener_temporada_ciudad_fecha(ciudad: Optional[str] = None, fecha: Optional[str] = None):
    fecha = mktime(datetime.strptime(fecha, "%Y-%m-%d").timetuple())
    if ciudad:
        Temporada = []
        if ciudad in db_nacionales.db_temporada_alta:
            fecha_inicio = mktime(datetime.strptime(db_nacionales.db_temporada_alta[ciudad].fecha_inicio, "%Y-%m-%d").timetuple())
            fecha_fin = mktime(datetime.strptime(db_nacionales.db_temporada_alta[ciudad].fecha_fin, "%Y-%m-%d").timetuple())
            if fecha >= fecha_inicio and fecha <= fecha_fin:
                Temporada.routerend(db_nacionales.db_temporada_alta[ciudad])
            else: 
                Temporada = {'Message': 'Por la época especificada, la ciudad no se encuentra en temporada alta'}
        else:
            Temporada = {'Message': 'En la ciudad especificada no contamos con sucursal'}
    else:
        Temporada = db_nacionales.db_temporada_alta
    return  Temporada

@router.post("/Temporada/crear/")
async def crear_temporada(temporada: db_nacionales.temporada):
    creada_exitosamente = db_nacionales.crear_temporada(temporada)
    if creada_exitosamente:
        return {"mensaje": "Temporada creada correctamente"}
    else:
        raise HTTPException(status_code = 400,
                            detail="Evento ya existe")

@router.get("/Temporada/General")
async def obtener_FiestaG():
    TemporadaGeneral = db_general.obtener_temporada_general()
    return  TemporadaGeneral