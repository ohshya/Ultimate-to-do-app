from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class Nota(SQLModel, table=True):
    uid: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    contenido: str
    archivado: bool = Field(default=False)
    fecha_creado: datetime = Field(default_factory=datetime.utcnow)
    tema: int
    carpeta_id: Optional[int] = Field(default=None, foreign_key="carpeta.uid")
    carpeta: Optional["Carpeta"] = Relationship(back_populates="notas")

class Carpeta(SQLModel, table=True):
    uid: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    color: str
    notas: List[Nota] = Relationship(back_populates="carpeta")