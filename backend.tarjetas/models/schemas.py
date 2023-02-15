from typing import Union
from pydantic import BaseModel
from .tarjeta import TarjetaCredito


class TarjetaModel(BaseModel):
    titular: str
    numero_tarjeta: str
    fecha_expiracion: str
    cvv: str
