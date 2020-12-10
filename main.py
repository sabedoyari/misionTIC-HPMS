from fastapi import FastAPI, HTTPException
import db_general
import db_nacionales


app = FastAPI()


@app.get("/Temporada/")
async def obtener_Temporada():
    Temporada = db.obtener_Temporada()
    return  Temporada


@app.post("/ordenes/crear/")
async def crear_orden(orden: db.Orden):
    creada_exitosamente = db.crear_orden(orden)
    if creada_exitosamente:
        return {"mensaje": "Orden creada correctamenteo"}
    else:
        raise HTTPException(
            status_code=400, detail="error, orden con ese id ya exisitia")