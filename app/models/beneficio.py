from pydantic import BaseModel
from typing import Optional

class BeneficioSustentable(BaseModel):
    """
    Modelo de datos para un beneficio sustentable.

    Attributes:
        id (Optional[str]): ID único del beneficio sustentable.
        nombre (str): Nombre del beneficio sustentable.
        descripcion (str): Descripción del beneficio sustentable.
        tipo (str): Tipo de beneficio sustentable.
        impacto (float): Impacto del beneficio sustentable.
    """
    id: Optional[str] = None
    nombre: str
    descripcion: str
    tipo: str
    impacto: float