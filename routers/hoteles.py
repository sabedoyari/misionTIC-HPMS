from datetime import date, datetime
from time import mktime
from typing import Optional
from fastapi import APIRouter, HTTPException
from pydantic.main import BaseModel
from db import db_hoteles, db_nacionales

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

# Para sucursales se aplica el supuesto de que en temporada alta el precio es 150%, media 125% y baja 100%.

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

class consulta_sucursal(BaseModel):
    nombre_hotel: Optional[str] = None
    ciudad: Optional[str] = None
    fecha_inicio: Optional[str] = None
    fecha_fin: Optional[str] = None

@router.post("/Sucursales/Consultar")
async def consultar_sucursales(consulta: consulta_sucursal):
    
    nombre_hotel = consulta.nombre_hotel
    ciudad = consulta.ciudad
    fecha_inicio = consulta.fecha_inicio
    fecha_fin = consulta.fecha_fin

    if nombre_hotel or ciudad or fecha_inicio or fecha_fin:
        
        if ciudad in db_hoteles.db_sucursales.keys():
            if db_hoteles.db_sucursales[ciudad].nombre_hotel == nombre_hotel:
                sucursal = db_hoteles.db_sucursales[ciudad]
                price = (sucursal.other_costs/sucursal.num_hab + sucursal.room_costs) * (1 + sucursal.utility)
                ts_fecha_inicio = mktime(datetime.strptime(fecha_inicio, "%Y-%m-%d").timetuple())
                ts_fecha_fin = mktime(datetime.strptime(fecha_fin, "%Y-%m-%d").timetuple())
                duracion = (ts_fecha_fin - ts_fecha_inicio)/(3600*24)

                tasa_tipo_temp = 1
                temporada_ciudad = db_nacionales.db_temporada[ciudad]
                ts_fecha_inicio_hotel = mktime(datetime.strptime(temporada_ciudad.fecha_inicio, "%Y-%m-%d").timetuple())
                ts_fecha_fin_hotel = mktime(datetime.strptime(temporada_ciudad.fecha_fin, "%Y-%m-%d").timetuple())

                if ts_fecha_inicio <= ts_fecha_inicio_hotel:
                    if ts_fecha_fin <= ts_fecha_inicio_hotel:
                        price *= tasa_tipo_temp
                        return {'Mensaje': f'Para la fecha especificada, recomendable aplicar tarifa de temporada baja.\n'
                                           f'Precio de la habitación por noche: {price}\n\n'
                                           f'Para {duracion:.0f} días, el precio total de la estadía es: {duracion*price}'}
                    elif ts_fecha_fin > ts_fecha_inicio_hotel and ts_fecha_fin <= ts_fecha_fin_hotel:
                        duracion_baja = (ts_fecha_inicio_hotel-ts_fecha_inicio)/(3600*24)
                        duracion_alta = (ts_fecha_fin-ts_fecha_inicio_hotel)/(3600*24)
                        return {'Mensaje': f'Para la fecha especificada, se deben aplicar varias tarifas: \n'
                                           f'Precio de la habitación por noche en temporada baja: {price}\n'
                                           f'Para {duracion_baja:.0f} días en temporada baja, el precio por esos días es: {duracion_baja*price}'
                                           f'Precio de la habitación por noche en temporada alta: {1.5*price}\n'
                                           f'Para {duracion_alta:.0f} días en temporada alta, el precio por esos días es: {duracion_alta*1.5*price}\n\n'
                                           f'Precio total de la estadía para {duracion:.0f} días: {(duracion_baja + 1.5*duracion_alta)*price}'}
                    elif ts_fecha_fin > ts_fecha_inicio_hotel and ts_fecha_fin > ts_fecha_fin_hotel:
                        duracion_baja = (ts_fecha_inicio_hotel-ts_fecha_inicio)/(3600*24) + (ts_fecha_fin-ts_fecha_fin_hotel)/(3600*24) 
                        duracion_alta = (ts_fecha_fin_hotel-ts_fecha_inicio_hotel)/(3600*24)
                        return {'Mensaje': f'Para la fecha especificada, se deben aplicar varias tarifas: \n'
                                           f'Precio de la habitación por noche en temporada baja: {price}\n'
                                           f'Para {duracion_baja:.0f} días en temporada baja, el precio por esos días es: {duracion_baja*price}'
                                           f'Precio de la habitación por noche en temporada alta: {1.5*price}\n'
                                           f'Para {duracion_alta:.0f} días en temporada alta, el precio por esos días es: {duracion_alta*1.5*price}\n\n'
                                           f'Precio total de la estadía para {duracion:.0f} días: {(duracion_baja + 1.5*duracion_alta)*price}'}
                elif ts_fecha_inicio > ts_fecha_inicio_hotel and ts_fecha_inicio <= ts_fecha_fin_hotel:
                    if ts_fecha_fin <= ts_fecha_fin_hotel:
                        return {'Mensaje': f'Para la fecha especificada, recomendable aplicar tarifa de temporada alta.\n'
                                           f'Precio de la habitación por noche: {price}\n\n'
                                           f'Para {duracion:.0f} días, el precio total de la estadía es: {duracion*price}'}
                    elif ts_fecha_fin > ts_fecha_fin_hotel:
                        duracion_baja = (ts_fecha_fin-ts_fecha_fin_hotel)/(3600*24)
                        duracion_alta = (ts_fecha_fin_hotel-ts_fecha_inicio)/(3600*24)
                        return {'Mensaje': f'Para la fecha especificada, se deben aplicar varias tarifas: \n'
                                           f'Precio de la habitación por noche en temporada baja: {price}\n'
                                           f'Para {duracion_baja:.0f} días en temporada baja, el precio por esos días es: {duracion_baja*price}'
                                           f'Precio de la habitación por noche en temporada alta: {1.5*price}\n'
                                           f'Para {duracion_alta:.0f} días en temporada alta, el precio por esos días es: {duracion_alta*1.5*price}\n\n'
                                           f'Precio total de la estadía para {duracion:.0f} días: {(duracion_baja + 1.5*duracion_alta)*price}'}
                elif ts_fecha_inicio > ts_fecha_fin_hotel:
                    return {'Mensaje': f'Para la fecha especificada, recomendable aplicar tarifa de temporada baja.\n'
                                       f'Precio de la habitación por noche: {price}\n\n'
                                       f'Para {duracion:.0f} días, el precio total de la estadía es: {duracion*price}'}                                          
            else:
                raise HTTPException(status_code = 400,
                            detail = "En la ciudad indicada no existen sucursales de ese hotel.")
        else:
            raise HTTPException(status_code = 400,
                            detail = "En la ciudad indicada no hay hoteles registrados en el aplicativo.")
    else:    
        raise HTTPException(status_code = 400,
                            detail = "Debe especificar todos los parámetros de búsqueda.")

