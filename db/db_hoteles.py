from pydantic import BaseModel
from typing import Dict
from typing import Optional

class hotel(BaseModel):
    nombre_hotel: str
    owner: str
    gerente: str
    sucursales: Optional[list] = []

db_hoteles = Dict[str, hotel]

# Bajo el supuesto de que en temporada alta el precio es 150%, media 125% y baja 100%.

db_hoteles = {
    'De Cameron': hotel(**{
        'nombre_hotel': 'De Cameron',
        'owner': 'Tania',
        'gerente': 'Tania',
        'sucursales': [
            'Medellín', 
            'Cali', 
            'Cartagena'
            ]
    }),

    'Dann Carlton': hotel(**{
        'nombre_hotel': 'Dann Carlton',
        'owner': 'Jairo',
        'gerente': 'Jairo',
        'sucursales': [
            'Medellín', 
            'Cali', 
            'Cartagena', 
            'Bogotá'
            ]
    })
}


class sucursal(BaseModel):
    nombre_hotel: str
    ciudad: str
    num_hab: int
    room_costs: float
    other_costs: float
    utility: float
    admin: str

db_sucursales = Dict[str, sucursal]

db_sucursales = {
    'Medellín': sucursal(**{
        'nombre_hotel': 'Dann Carlton',
        'ciudad': 'Medellín',
        'num_hab': 40,
        'room_costs': 400000,
        'other_costs': 100000,
        'utility': 0.30,
        'admin': 'Santiago'
    }),
    'Cartagena': sucursal(**{
        'nombre_hotel': 'Dann Carlton',
        'ciudad': 'Cartagena',
        'num_hab': 40,
        'room_costs': 400000,
        'other_costs': 100000,
        'utility': 0.30,
        'admin': 'Santiago'
    }),
}