from fastapi import FastAPI, HTTPException
#import db_general
import db_nacionales


app = FastAPI()


@app.get("/Temporada/")
async def obtener_temporada():
    Temporada = db_nacionales.obtener_temporada()
    return  Temporada


@app.post("/Temporada/crear/")
async def crear_temporada(fiesta: db_nacionales.Fiesta):
    creada_exitosamente = db_nacionales.crear_temporada(fiesta)
    if creada_exitosamente:
        return {"mensaje": "Orden creada correctamenteo"}
    else:
        raise HTTPException(
            status_code=400, detail=" ya exisitia")