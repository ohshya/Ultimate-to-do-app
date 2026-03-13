# app/routes/notas.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import get_session
from app.models.notas import Nota, Carpeta

router = APIRouter()

# --- RUTAS DE NOTAS ---

@router.post("/notas", response_model=Nota)
def crear_nota(nota: Nota, session: Session = Depends(get_session)):
    session.add(nota)
    session.commit()
    session.refresh(nota)
    return nota

@router.get("/notas", response_model=list[Nota])
def leer_notas(session: Session = Depends(get_session)):
    notas = session.exec(select(Nota)).all()
    return notas

@router.delete("/notas/{uid}")
def eliminar_nota(uid: int, session: Session = Depends(get_session)):
    nota = session.get(Nota, uid)
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    session.delete(nota)
    session.commit()
    return {"message": "Nota eliminada"}

# --- RUTAS DE CARPETAS ---

@router.post("/carpetas", response_model=Carpeta)
def crear_carpeta(carpeta: Carpeta, session: Session = Depends(get_session)):
    session.add(carpeta)
    session.commit()
    session.refresh(carpeta)
    return carpeta

@router.get("/carpetas", response_model=list[Carpeta])
def leer_carpetas(session: Session = Depends(get_session)):
    carpetas = session.exec(select(Carpeta)).all()
    return carpetas