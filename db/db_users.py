from pydantic import BaseModel
from typing import Dict

class usuarios(BaseModel):
    nombre_hotel: str
    name: str
    email: str
    password: str
    id: int
    cargo: str

db_users = dict[str, usuarios]

db_users = {
    'Tania': usuarios(**{
        'nombre_hotel': 'Dann Carlton',
        'name': 'Tania M',
        'email': 'tania@yopmail.com',
        'nick': 'Tania',
        'password': 'abc1234',
        'id': 123456,
        'cargo': 'Gerente'
    }),
    'Jaime': usuarios(**{
        'nombre_hotel': 'Dann Carlton',
        'name': 'Jaime',
        'email': 'jaime@yopmail.com',
        'nick': 'Jaime',
        'password': 'abc1234',
        'id': 123457,
        'cargo': 'Recepcionista'
    }),
    'Francisco': usuarios(**{
        'nombre_hotel': 'De Cameron',
        'name': 'Franciso',
        'email': 'franciso@yopmail.com',
        'nick': 'Francisco',
        'password': 'abc1234',
        'id': 123458,
        'cargo': 'Gerente'
    }),
    'Andres': usuarios(**{
        'nombre_hotel': 'De Cameron',
        'name': 'Andrés',
        'email': 'andres@yopmail.com',
        'nick': 'Andres',
        'password': 'abc1234',
        'id': 123459,
        'cargo': 'Recepcionista'
    }),
}