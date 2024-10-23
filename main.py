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
