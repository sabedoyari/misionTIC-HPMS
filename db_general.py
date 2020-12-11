from pydantic import BaseModel


class FiestaG(BaseModel):
    id:int
    fecha_inicio: str
    fecha_fin: str
    fiesta: str



Festividades_alta = {
    1: FiestaG( id=1,fecha_inicio="30-11-2020", fecha_fin="12-01-2021", fiesta="Navidad"),
    2: FiestaG( id=2,fecha_inicio="15-06-2021", fecha_fin="15-07-2021", fiesta="Mitad de año"),
    3: FiestaG( id=3,fecha_inicio="27-03-2021", fecha_fin="04-04-2021", fiesta="Semana santa")
}

Festividades_media = {
    1: FiestaG(id=1, fecha_inicio="09-01-2021", fecha_fin="11-01-2021", fiesta ="Festivo"),
    2: FiestaG(id=2, fecha_inicio="15-05-2021", fecha_fin="17-05-2021", fiesta ="Festivo"),
    3: FiestaG(id=3, fecha_inicio="05-06-2021", fecha_fin="07-06-2021", fiesta ="Festivo"),
    4: FiestaG(id=4,fecha_inicio = "12-06-2021", fecha_fin="14-06-2021", fiesta="Festivo"),
    5: FiestaG(id=5, fecha_inicio="03-07-2021", fecha_fin="05-07-2021", fiesta="Festivo"),
    6: FiestaG(id=6, fecha_inicio="17-07-2021", fecha_fin="20-07-2021", fiesta="Festivo"),
    7: FiestaG(id=7, fecha_inicio="14-08-2021", fecha_fin="16-08-2021", fiesta="Festivo"),
    8: FiestaG(id=8, fecha_inicio="16-09-2021", fecha_fin="18-09-2021", fiesta="Festivo"),
    9: FiestaG(id=9, fecha_inicio="30-10-2021", fecha_fin="01-11-2021", fiesta="Festivo"),
    10: FiestaG(id=10, fecha_inicio="13-11-2021", fecha_fin="15-11-2021", fiesta="Festivo"),
    11: FiestaG(id=11, fecha_inicio="04-12-2021", fecha_fin="08-12-2021", fiesta="Festivo")
}

def obtener_FiestaG():
    # Haga lo que tenga que hacer para conectarse a la base de datos y obtener todas las ordenes
    lista_FiestaG= []
    for e in Festividades_alta:
        lista_FiestaG.append(Festividades_alta)
        return lista_FiestaG