from pydantic import BaseModel


# Este es un cambio
# Y este será otro cambio

class Temporada(BaseModel):
    fecha_inicio: str
    fecha_fin: str
    fiesta: str



Festividades_alta = {
    1: Orden( fecha_inicio="30-11-2020", fecha_fin="12-01-2021", fiesta="Navidad"),
    2: Orden( fecha_inicio="15-06-2021", fecha_fin="15-07-2021", fiesta="Mitad de año")
}

Festividades_media = {
    1: Orden( fecha_inicio="09-01-2021", fecha_fin="11-01-2021",  fiesta="Festivo"),
    2: Orden( fecha_inicio="20-03-2021", fecha_fin="20-03-2021", fiesta="Festivo")
}

#def obtener_ordenes():
    # Haga lo que tenga que hacer para conectarse a la base de datos y obtener todas las ordenes
    #lista_ordenes = []
    #for e in ordenes:
    #    list