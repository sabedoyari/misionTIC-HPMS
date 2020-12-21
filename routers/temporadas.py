from typing import Optional
from fastapi import APIRouter, HTTPException
from db import db_nacionales, db_general

from time import mktime
from datetime import datetime

router = APIRouter(
    tags = ["Temporadas"],
    prefix = "/Temporada"
)

@router.get("/")
async def obtener_temporada(ciudad: Optional[str] = None):

    """
    Buscar las temporadas registradas asociadas a las fiestas nacionales.

    Al enviar el parámetro ciudad, buscará si en la ciudad especificada
    el hotel cuenta con sucursales.
    
    Si no se envía el parámetro, se devuelve el
    listado completo.
    """

    if ciudad:
        Temporada = []
        if ciudad in db_nacionales.db_temporada:
            Temporada.append(db_nacionales.db_temporada[ciudad]) 
        else:
            Temporada = {'Message: En la ciudad especificada no contamos con sucursal'}
    else:
        Temporada = db_nacionales.db_temporada
    return  Temporada

@router.get("/CiudadFecha/")
async def obtener_temporada_ciudad_fecha(ciudad: Optional[str] = None, fecha: Optional[str] = None):
    fecha = mktime(datetime.strptime(fecha, "%Y-%m-%d").timetuple())
    if ciudad:
        Temporada = []
        if ciudad in db_nacionales.db_temporada:
            fecha_inicio = mktime(datetime.strptime(db_nacionales.db_temporada[ciudad].fecha_inicio, "%Y-%m-%d").timetuple())
            fecha_fin = mktime(datetime.strptime(db_nacionales.db_temporada[ciudad].fecha_fin, "%Y-%m-%d").timetuple())
            if fecha >= fecha_inicio and fecha <= fecha_fin:
                Temporada.append(db_nacionales.db_temporada[ciudad])
            else: 
                Temporada = {'Message': 'Por la época especificada, la ciudad no se encuentra en temporada alta'}
        else:
            Temporada = {'Message': 'En la ciudad especificada no se ha registrado una sucursal.'}
    else:
        Temporada = db_nacionales.db_temporada
    return  Temporada

@router.post("/Crear/")
async def crear_temporada(temporada: db_nacionales.temporada):
    creada_exitosamente = db_nacionales.crear_temporada(temporada)
    if creada_exitosamente:
        return {"mensaje": "Temporada creada correctamente"}
    else:
        raise HTTPException(status_code = 400,
                            detail="Evento ya existe")

@router.get("/General")
async def obtener_temporada_general():
    TemporadaGeneral = db_general.obtener_temporada_general()
    return  TemporadaGeneral