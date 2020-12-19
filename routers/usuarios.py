from typing import Optional
from fastapi import APIRouter, HTTPException
from db import db_users

router = APIRouter(
    tags = ["Users"],
    prefix = "/Users"
)

@router.get("/")
async def obtener_usuarios(nombre_usuario: Optional[str] = None):

    if nombre_usuario:
        usuarios = []
        if nombre_usuario in db_users.db_users.keys():
            usuarios.append(db_users.db_users[nombre_usuario])
        else:
            usuarios = {'Message': 'El usuario especificado no existe.'}
    else:
        usuarios = db_users.db_users
    return usuarios

@router.post("/Crear")
async def crear_usuario(usuario: db_users.usuarios):
    
    if usuario.nick in db_users.db_users:
        raise HTTPException(status_code = 400,
                            detail = "El usuario ya existe.")
    else:
        db_users.db_users[usuario.nick] = usuario
        return {'Message': f'Se ha creado correctamente el usuario {usuario.nick}'
                f'Corresponediente a {usuario.name}'}