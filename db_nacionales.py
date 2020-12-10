from pydantic import BaseModel


class Fiesta(BaseModel):
    fecha_inicio: str
    fecha_fin: str
    ciudad: str
    fiesta: str



Festividades_alta= {
    1: Fiesta ( fecha_inicio="02-01-2021", fecha_fin="07-01-2021", ciudad="Pasto", fiesta="Carnaval de Negros y Blancos"),
    2: Fiesta ( fecha_inicio="04-01-2021", fecha_fin="12-01-2021", ciudad="Cartagena", fiesta="Festival Internacional de Música"),
    4: Fiesta ( fecha_inicio="21-04-2021", fecha_fin="05-05-2021", ciudad="Bogota", fiesta="Feria del Libro"),
    5: Fiesta ( fecha_inicio="29-04-2021", fecha_fin="02-05-2020", ciudad="Valledupar", fiesta="Festival de la Leyenda Vallenata"),
    6: Fiesta ( fecha_inicio="21-04-2021", fecha_fin="05-05-2021", ciudad="Bogota", fiesta="Feria del Libro"),
    7: Fiesta ( fecha_inicio="21-04-2021", fecha_fin="05-05-2021", ciudad="Bogota", fiesta="Feria del Libro"),
    8: Fiesta ( fecha_inicio="21-04-2021", fecha_fin="05-05-2021", ciudad="Bogota", fiesta="Feria del Libro"),
    9: Fiesta ( fecha_inicio="21-04-2021", fecha_fin="05-05-2021", ciudad="Bogota", fiesta="Feria del Libro"),

}


def obtener_temporada():
    # Haga lo que tenga que hacer para conectarse a la base de datos y obtener todas las ordenes
    lista_temporadas = []
    for e in Festividades_alta:
        lista_temporadas.append(Festividades_alta)
        return lista_temporadas