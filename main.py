# Instalación: pip install fastapi uvicorn
from typing import Optional, List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
#Modelo base
class Mensaje (ModeloBase):
    id: Optional[int] = None
    user: str
    mensaje: str
#Inicializacion de FastAPI
app = FastAPI()  
#Base de datos simulada 
mensaje_db =[]
contador_id = 0 #para asegurar ids unicos
#crear mensaje
@app.post("/mensajes/", response_model=Mensaje)
def crear_mensaje(mensaje:Mensaje):
    global contador_id
    mensaje.id = contador_id
    contador_id + = 1
    mensaje_db.append(mensaje)
    return mensaje
#obtener todos los mensajes
@app.get("/mensajes/", response_model=List[Mensaje])
def obtener_mensajes():
    return mensaje_db   
#obtener un mensaje especifico
@app.get("/mensajes/{mensaje_id}", response_model=Mensaje)
def obtener_mensaje(mensaje_id: int):
    for mensaje in mensaje_db:
        if mensaje.id == mensaje_id:
            return mensaje
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")
#actualizar un mensaje existente
@app.put("/mensajes/{mensaje_id}", response_model=Mensaje)
def actualizar_mensaje(mensaje_id: int, mensaje: Mensaje):
    for index, _mensaje in enumerate(mensaje_db):
        if _mensaje.id == mensaje_id:
            mensaje_db[index] = mensaje_actualizado.dict()#actualizar el mensaje
            mensaje_db[index].id = mensaje_id
            return mensaje_db[index]
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")	
