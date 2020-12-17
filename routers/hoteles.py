from typing import Optional
from fastapi import APIRouter, HTTPException
from db import db_hoteles

from time import mktime
from datetime import datetime

router = APIRouter(
    tags = ["Hoteles"],
    prefix = "/Hoteles"
)

@router.get("/")
async def obtener_hoteles(nombre_hotel: Optional[str] = None):

    if nombre_hotel:
        hoteles = []
        if nombre_hotel in db_hoteles.db_hoteles.keys():
            hoteles.append(db_hoteles.db_hoteles[nombre_hotel])
        else:
            hoteles = {'Message': 'El hotel especificado no está registrado en el aplicativo'}
    else:
        hoteles = db_hoteles.db_hoteles

    return hoteles

@router.post("/Crear")
async def crear_hotel(hotel: db_hoteles.hotel):

    if hotel.nombre_hotel in db_hoteles.db_hoteles:
        raise HTTPException(status_code = 400,
                            detail = "El hotel ya está creado")
    else:
        db_hoteles.db_hoteles[hotel.nombre_hotel] = hotel
        return {'message': f'Se ha creado correctamente el hotel {hotel.nombre_hotel}'}

@router.post("/Sucursales/Crear")
async def crear_sucursal(sucursal: db_hoteles.sucursal):

    if sucursal.nombre_hotel:
        if not sucursal.nombre_hotel in db_hoteles.db_hoteles.keys():
            raise HTTPException(status_code = 400,
                            detail = "El hotel no está registrado en nuestro aplicativo. Proceda a crearlo.")
        elif sucursal.ciudad in db_hoteles.db_hoteles[sucursal.nombre_hotel].sucursales:
            raise HTTPException(status_code = 400,
                            detail = "El hotel ya cuenta con sucursal en esa ciudad.")
        else:
            db_hoteles.db_sucursales[sucursal.ciudad] = sucursal
            db_hoteles.db_hoteles[sucursal.nombre_hotel].sucursales.append(sucursal.ciudad)
            price = (sucursal.other_costs/sucursal.num_hab + sucursal.room_costs) * (1 + sucursal.utility)

            return {'Message': f'Se ha creado una sucursal en la ciudad de {sucursal.ciudad}'
                            f' para el hotel {sucursal.nombre_hotel}. '
                            f'El precio recomendable por habitación es: {price}'}
    else:
        raise HTTPException(status_code = 400,
                            detail = "Debe especificar el nombre del hotel al que le añadirá la sucursal")    
    
@router.get("Sucursales/Consultar")
async def consultar_sucursales(nombre_hotel: Optional[str] = None, ciudad: Optional[str] = None):
    
    if nombre_hotel or ciudad:

        if ciudad in db_hoteles.db_sucursales.keys():
            if db_hoteles.db_sucursales[ciudad].nombre_hotel == nombre_hotel:
                return db_hoteles.db_sucursales[ciudad]
            else:
                raise HTTPException(status_code = 400,
                            detail = "En la ciudad detalla, no existen sucursales de ese hotel")
        else:
            raise HTTPException(status_code = 400,
                            detail = "En la ciudad detalla no hay hoteles registrados en el aplicativo")
    else:    
        return db_hoteles.db_sucursales

