from fastapi import FastAPI, HTTPException
import db_nacionales
import db_general

app = FastAPI()

@app.get("/TemporadaNacionales/")
async def obtener_temporada():
    Temporada = db_nacionales()
    return  Temporada

@app.get("/TemporadaGenerales/")
async def obtener_temporada():
    Temporada = db_general()
    return  Temporada

@app.post("/TemporadaNacionales/crear/")
async def crear_fiesta(fiesta: db_nacionales):
    creada_exitosamente = db_nacionales(fiesta)
    if creada_exitosamente:
        return {"mensaje": "Fiesta creada correctamente"}
    else:
        raise HTTPException(
            status_code=400, detail="ERROR, esta fiesta ya existe")

