from sqlalchemy import Column, Integer, String
from database import Base


class TarjetaCredito(Base):
    __tablename__ = 'tarjetas'
    id = Column(Integer, primary_key=True, index=True)
    titular = Column(String(length=100), nullable=False)
    numero_tarjeta = Column(String(length=16), nullable=False)
    fecha_expiracion = Column(String(length=5), nullable=False)
    cvv = Column(String(length=3), nullable=False) 