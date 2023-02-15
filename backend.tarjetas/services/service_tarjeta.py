from sqlalchemy.orm import Session
from models.tarjeta import TarjetaCredito
from models.schemas import TarjetaModel


class TarjetaService:
    db: Session = None

    def __init__(self, db: Session) -> None:
        self.db = db

    def fetch(self):
        return self.db.query(TarjetaCredito).all()

    def retrieve(self, id):
        return self.db.query(TarjetaCredito).filter(TarjetaCredito.id == id).first()

    def create_tarjete(self, tarjeta: TarjetaModel):
        new_tarjeta = TarjetaCredito(titular=tarjeta.titular,
                                     numero_tarjeta=tarjeta.numero_tarjeta,
                                     fecha_expiracion=tarjeta.fecha_expiracion,
                                     cvv=tarjeta.cvv)
        self.db.add(new_tarjeta)
        self.db.commit()
        self.db.refresh(new_tarjeta)
        return new_tarjeta

    def update_tarjeta(self, tarjeta: TarjetaModel, id_tarjeta: int):
        tarjeta_entidad = self.retrieve(id_tarjeta)
        if (not tarjeta_entidad):
            return (False, None)
        for key, value  in dict(tarjeta).items():
            setattr(tarjeta_entidad, key, value)
        self.db.commit()
        self.db.refresh(tarjeta_entidad)
        return (True, tarjeta_entidad)
    
    def remove(self, id_tarjeta: int):
        tarjeta = self.retrieve(id_tarjeta)
        self.db.delete(tarjeta)
        self.db.commit()