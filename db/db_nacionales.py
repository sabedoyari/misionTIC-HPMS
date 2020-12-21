from pydantic import BaseModel
from typing import Dict

class temporada(BaseModel):
    ciudad: str
    fecha_inicio: str
    fecha_fin: str
    fiesta: str
    tipo_temp: str

db_temporada = Dict[str, temporada]

db_temporada = {
    'Cartagena': temporada(**{'ciudad': 'Cartagena',
                              'fecha_inicio': '2021-01-04',
                              'fecha_fin': '2021-01-07',
                              'fiesta': 'Festival Internacional de Música',
                              'tipo_temp': 'Alta'
                                                }),
    'Pasto': temporada(**{'ciudad': 'Pasto, Nariño',
                              'fecha_inicio': '2021-01-04',
                              'fecha_fin': '2021-01-12',
                              'fiesta': 'Carnaval de Negros y Blancos',
                              'tipo_temp': 'Alta'
                                                }),
    'Manizales': temporada(**{'ciudad': 'Manizales',
                              'fecha_inicio': '2021-01-04',
                              'fecha_fin': '2021-01-12',
                              'fiesta': 'Feria de Manizales',
                              'tipo_temp': 'Alta'
                                                }),      
    # 'Cartagena': temporada(**{'ciudad': 'Cartagena',
    #                           'fecha_inicio': '2021-01-30',
    #                           'fecha_fin': '2021-02-02',
    #                           'fiesta': 'Hay Festival',
    #                           'tipo_temp': 'Alta'
    #                                             }),
    'Boyacá': temporada(**{'ciudad': 'Boyacá',
                              'fecha_inicio': '2021-01-31',
                              'fecha_fin': '2021-02-02',
                              'fiesta': 'Fiestas de la Candelaria',
                              'tipo_temp': 'Alta'
                                                }),
    'Tumaco': temporada(**{'ciudad': 'Tumaco',
                              'fecha_inicio': '2021-02-20',
                              'fecha_fin': '2021-02-25',
                              'fiesta': 'Carnaval del Fuego',
                              'tipo_temp': 'Alta'
                                                }),                                                                                                                                                
}

def obtener_temporada():
    lista_temporadas = []
    for fiesta in db_temporada:
        lista_temporadas.append(db_temporada)
    return db_temporada

def crear_temporada(temp: temporada):
    if temp.ciudad in db_temporada:
        return False
    else:
        db_temporada[temp.ciudad] = temp
        return True