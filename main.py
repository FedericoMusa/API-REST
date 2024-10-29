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