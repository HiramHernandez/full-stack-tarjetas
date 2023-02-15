from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models.schemas import TarjetaModel
from get_db import get_db
from services.service_tarjeta import TarjetaService


app = FastAPI()



@app.get("/tarjeta")
def tarjeta(db: Session = Depends(get_db)):
    tarjeta_service = TarjetaService(db)
    tarjetas = tarjeta_service.fetch()
    return tarjetas

@app.get("/tarheta/{id}")
def tarjeta(id: int, db: Session = Depends(get_db)):
    tarjeta_service = TarjetaService(db)
    tarjeta = tarjeta_service.retrieve(id)
    if(not tarjeta):
        raise HTTPException(detail=f"No se encontró tarjeta con id {id}", status_code=404)
    return tarjeta

@app.post("/tarjeta")
def create_tarjeta(tarjeta: TarjetaModel, db: Session = Depends(get_db)):
    tarjeta_service = TarjetaService(db)
    return tarjeta_service.create_tarjete(tarjeta)

@app.put("/tarjeta/{id}")
def modify_tarjeta(tarjeta: TarjetaModel, id: int, db: Session = Depends(get_db)):
    tarjeta_service = TarjetaService(db)
    success, model = tarjeta_service.update_tarjeta(tarjeta=tarjeta, id_tarjeta=id)
    if (not success):
        raise HTTPException(detail="Ocurrió un error al modificar la tarjeta intente de nuevo después por favor", status_code=500)
    return model

@app.delete("/tarjeta/{id}")
def delete_tarjeta(id: int, db: Session = Depends(get_db)):
    tarjeta_service = TarjetaService(db)
    tarjeta_service.remove(id)