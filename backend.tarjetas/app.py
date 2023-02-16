from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models.schemas import TarjetaModel
from get_db import get_db
from services.service_tarjeta import TarjetaService

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:4000",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.host="0.0.0.0"

@app.get("/api/tarjeta")
def tarjeta(db: Session = Depends(get_db)):
    tarjeta_service = TarjetaService(db)
    tarjetas = tarjeta_service.fetch()
    return tarjetas

@app.get("/api/tarjeta/{id}")
def tarjeta(id: int, db: Session = Depends(get_db)):
    tarjeta_service = TarjetaService(db)
    tarjeta = tarjeta_service.retrieve(id)
    if(not tarjeta):
        raise HTTPException(detail=f"No se encontró tarjeta con id {id}", status_code=404)
    return tarjeta

@app.post("/api/tarjeta")
def create_tarjeta(tarjeta: TarjetaModel, db: Session = Depends(get_db)):
    tarjeta_service = TarjetaService(db)
    return tarjeta_service.create_tarjete(tarjeta)

@app.put("/api/tarjeta/{id}")
def modify_tarjeta(tarjeta: TarjetaModel, id: int, db: Session = Depends(get_db)):
    tarjeta_service = TarjetaService(db)
    success, model = tarjeta_service.update_tarjeta(tarjeta=tarjeta, id_tarjeta=id)
    if (not success):
        raise HTTPException(detail="Ocurrió un error al modificar la tarjeta intente de nuevo después por favor", status_code=500)
    return model

@app.delete("/api/tarjeta/{id}")
def delete_tarjeta(id: int, db: Session = Depends(get_db)):
    tarjeta_service = TarjetaService(db)
    tarjeta_service.remove(id)