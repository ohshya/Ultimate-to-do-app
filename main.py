from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from database import engine, create_db_and_tables
from models import Nota, Carpeta

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

def get_session():
    with Session(engine) as session:
        yield session

# --- Endpoints de CARPETAS ---
@app.post("/carpetas")
def crear_carpeta(carpeta: Carpeta, session: Session = Depends(get_session)):
    session.add(carpeta)
    session.commit()
    session.refresh(carpeta)
    return carpeta

@app.get("/carpetas")
def listar_carpetas(session: Session = Depends(get_session)):
    return session.exec(select(Carpeta)).all()

# --- Endpoints de NOTAS ---
@app.post("/notas")
def crear_nota(nota: Nota, session: Session = Depends(get_session)):
    session.add(nota)
    session.commit()
    session.refresh(nota)
    return nota

@app.get("/notas")
def listar_notas(session: Session = Depends(get_session)):
    return session.exec(select(Nota)).all()

@app.delete("/notas/{uid}")
def borrar_nota(uid: int, session: Session = Depends(get_session)):
    nota = session.get(Nota, uid)
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    session.delete(nota)
    session.commit()
    return {"mensaje": "Nota eliminada"}