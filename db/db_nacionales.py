from pydantic import BaseModel
from typing import Dict

class temporada(BaseModel):
    ciudad: str
    fecha_inicio: str
    fecha_fin: str
    fiesta: str

db_temporada_alta = Dict[str, temporada]

db_temporada_alta = {
    'Cartagena': temporada(**{'ciudad': 'Cartagena',
                              'fecha_inicio': '2021-01-04',
                              'fecha_fin': '2021-01-07',
                              'fiesta': 'Festival Internacional de Música'
                                                }),
    'Pasto': temporada(**{'ciudad': 'Pasto, Nariño',
                              'fecha_inicio': '2021-01-04',
                              'fecha_fin': '2021-01-12',
                              'fiesta': 'Carnaval de Negros y Blancos'
                                                }),
    'Manizales': temporada(**{'ciudad': 'Manizales',
                              'fecha_inicio': '2021-01-04',
                              'fecha_fin': '2021-01-12',
                              'fiesta': 'Feria de Manizales'
                                                }),      
    'Cartagena': temporada(**{'ciudad': 'Cartagena',
                              'fecha_inicio': '2021-01-30',
                              'fecha_fin': '2021-02-02',
                              'fiesta': 'Hay Festival'
                                                }),
    'Cartagena': temporada(**{'ciudad': 'Cartagena',
                              'fecha_inicio': '2021-01-30',
                              'fecha_fin': '2021-02-02',
                              'fiesta': 'Fiesta de la Candelaria'
                                                }),
    'Boyacá': temporada(**{'ciudad': 'Boyacá',
                              'fecha_inicio': '2021-01-31',
                              'fecha_fin': '2021-02-02',
                              'fiesta': 'Fiestas de la Candelaria'
                                                }),
    'Tumaco': temporada(**{'ciudad': 'Tumaco',
                              'fecha_inicio': '2021-02-20',
                              'fecha_fin': '2021-02-25',
                              'fiesta': 'Carnaval del Fuego'
                                                }),                                                                                                                                                
}

def obtener_temporada():
    lista_temporadas = []
    for fiesta in db_temporada_alta:
        lista_temporadas.append(db_temporada_alta)
    return db_temporada_alta

def crear_temporada(temp: temporada):
    if temp.ciudad in db_temporada_alta:
        return False
    else:
        db_temporada_alta[temp.ciudad] = temp
        return True