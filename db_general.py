from pydantic import BaseModel


# Este es un cambio
# Y este será otro cambio

class Temporada(BaseModel):
    fecha_inicio: str
    fecha_fin: str
    ciudad: str
    fiesta: str



Festividades_alta = {
    1: Orden( fecha_inicio="02-01-2021", fecha_fin="07-01-2021", ciudad="Pasto", fiesta="Carnaval de Negros y Blancos"),
    2: Orden( fecha_inicio="02-01-2021", fecha_fin="07-01-2021", ciudad="Pasto", fiesta="Carnaval de Negros y Blancos")
}

Festividades_media = {
    1: Orden( fecha_inicio="02-01-2021", fecha_fin="07-01-2021", ciudad="Pasto", fiesta="Festivo"),
    2: Orden( fecha_inicio="02-01-2021", fecha_fin="07-01-2021", ciudad="Pasto", fiesta="Festivo")
}

def obtener_ordenes():
    # Haga lo que tenga que hacer para conectarse a la base de datos y obtener todas las ordenes
    lista_ordenes = []
    for e in ordenes:
        list