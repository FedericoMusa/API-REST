# Instalación: pip install fastapi uvicorn
from typing import Optional, List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
#Modelo base
class Mensaje (ModeloBase):
    id: Optional[int] = None
    user: str
    mensaje: str
    