from pydantic import BaseModel


class Fiesta(BaseModel):
    fecha_inicio: str
    fecha_fin: str
    ciudad: str
    fiesta: str



Festividades_alta= {
    1: Fiesta (id=1, fecha_inicio="02-01-2021", fecha_fin="07-01-2021", ciudad="Pasto", fiesta="Carnaval de Negros y Blancos"),
    2: Fiesta (id=2, fecha_inicio="04-01-2021", fecha_fin="12-01-2021", ciudad="Cartagena", fiesta="Festival Internacional de Música"),
    3: Fiesta (id=3, fecha_inicio="04-01-2021", fecha_fin="12-01-2021", ciudad="Manizales", fiesta="Feria de Manizales"),
    4: Fiesta (id=4, fecha_inicio="30-01-2021", fecha_fin="02-02-2021", ciudad="Cartagena", fiesta="Hay Festival"),
    5: Fiesta (id=5, fecha_inicio="30-01-2021", fecha_fin="02-02-2021", ciudad="Cartagena", fiesta="Fiesta de la Candelaria"),
    6: Fiesta (id=6, fecha_inicio="31-01-2021", fecha_fin="02-02-2021", ciudad="Boyacá", fiesta="Festivas de Astronomía"),
    7: Fiesta (id=7, fecha_inicio="20-02-2021", fecha_fin="25-02-2021", ciudad="Tumaco", fiesta="Carnaval del Fuego"),
    8: Fiesta (id=8, fecha_inicio="22-02-2021", fecha_fin="25-02-2021", ciudad="Barranquilla", fiesta="Carnaval de Barranquilla"),
    9: Fiesta (id=9, fecha_inicio="11-03-2021", fecha_fin="16-03-2021", ciudad="Cartagena", fiesta="Festival Internacional de Cine"),
    5: Fiesta (id=5, fecha_inicio="16-03-2021", fecha_fin="23-03-2020", ciudad="Ibagué", fiesta="Festival Nacional de la Música Colombiana"),
    6: Fiesta (id=6, fecha_inicio="28-03-2021", fecha_fin="29-03-2020", ciudad="Paipa", fiesta="Paipa Color Festival"),
    7: Fiesta (id=7, fecha_inicio="05-04-2021", fecha_fin="10-04-2020", ciudad="Popayán", fiesta= "Festival de Música Religiosa"),
    8: Fiesta (id=8, fecha_inicio="21-04-2021", fecha_fin="05-05-2020", ciudad="Bogotá", fiesta="Feria Internacional del Libro"),
    9: Fiesta (id=9, fecha_inicio="10-05-2021", fecha_fin="15-05-2020", ciudad="Uribia", fiesta="Festival de la cultura Wayuu"),
    10: Fiesta (id=10, fecha_inicio="11-05-2021", fecha_fin="14-05-2020", ciudad="Ginebra", fiesta="Festiva del Mono Nuñez"),
    11: Fiesta (id=11, fecha_inicio="19-05-2021", fecha_fin="05-06-2020", ciudad="Bogotá", fiesta="Festival Iberoamerivano de Teatro"),
    12: Fiesta (id=12, fecha_inicio="01-06-2021", fecha_fin="03-06-2020", ciudad="Sutamarchán", fiesta="La tomatina de Sutamarchán"),
    13: Fiesta (id=13, fecha_inicio="13-06-2021", fecha_fin="29-06-2020", ciudad="Neiva", fiesta="Festival Folclórico y Reinado Nacional del Bambuco"),
    14: Fiesta (id=14, fecha_inicio="01-08-2021", fecha_fin="09-08-2020", ciudad="Cartagena", fiesta="Festival Cartagena Pride"),
    15: Fiesta (id=15, fecha_inicio="07-12-2021", fecha_fin="08-12-2020", ciudad="Villa de Leyva", fiesta="Fiesval de Luces"),
    16: Fiesta (id=16, fecha_inicio="29-04-2021", fecha_fin="02-05-2020", ciudad="Valledupar", fiesta="Festival de la Leyenda Vallenata")
}


def obtener_temporada():
    # Haga lo que tenga que hacer para conectarse a la base de datos y obtener todas las ordenes
    lista_temporadas = []
    for e in Festividades_alta:
        lista_temporadas.append(Festividades_alta)
        return lista_temporadas

def crear_temporada(fiesta:Fiesta):
    if fiesta.ciudad in Festividades_alta:
        return False
    else:
        Festividades_alta[len(Festividades_alta)+1]=fiesta
        return True  

