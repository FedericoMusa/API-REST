# Instalación: pip install fastapi uvicorn
from typing import Optional, List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

# Modelo base
class Mensaje(BaseModel):
    id: Optional[int] = None
    user: str
    mensaje: str

# Inicialización de FastAPI
app = FastAPI()

# Base de datos simulada
mensaje_db = []
contador_id = 0  # para asegurar ids únicos

# Crear mensaje
@app.post("/mensajes/", response_model=Mensaje)
def crear_mensaje(mensaje: Mensaje):
    global contador_id
    mensaje.id = contador_id
    contador_id += 1
    mensaje_db.append(mensaje)
    return mensaje

# Obtener todos los mensajes
@app.get("/mensajes/", response_model=List[Mensaje])
def obtener_mensajes():
    return mensaje_db

# Obtener un mensaje específico por ID
@app.get("/mensajes/{mensaje_id}", response_model=Mensaje)
def obtener_mensaje(mensaje_id: int):
    for mensaje in mensaje_db:
        if mensaje.id == mensaje_id:
            return mensaje
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")

# Actualizar un mensaje existente
@app.put("/mensajes/{mensaje_id}", response_model=Mensaje)
def actualizar_mensaje(mensaje_id: int, mensaje: Mensaje):
    for index, _mensaje in enumerate(mensaje_db):
        if _mensaje.id == mensaje_id:
            # Actualizar los campos pero conservar el ID original
            mensaje_db[index].user = mensaje.user
            mensaje_db[index].mensaje = mensaje.mensaje
            return mensaje_db[index]
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")

# Eliminar un mensaje por su ID
@app.delete("/mensajes/{mensaje_id}")
def eliminar_mensaje(mensaje_id: int):
    for index, _mensaje in enumerate(mensaje_db):
        if _mensaje.id == mensaje_id:
            del mensaje_db[index]
            return {"message": "Mensaje eliminado"}
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")
