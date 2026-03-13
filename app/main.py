# app/main.py
from fastapi import FastAPI
from app.database import engine
from sqlmodel import SQLModel
# Importas tus modelos para que SQLModel los reconozca
from app.models.notas import Nota, Carpeta 
# Importas tus rutas
from app.routes.notas import router as notas_router

app = FastAPI()

# Esto crea las tablas en tu database.db al iniciar si no existen
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(notas_router)