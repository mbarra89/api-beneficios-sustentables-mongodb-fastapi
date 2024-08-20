from fastapi import APIRouter, HTTPException
from typing import List
from app.models.beneficio import BeneficioSustentable
from app.services.beneficio_service import BeneficioService

router = APIRouter(
    prefix="/beneficios",
    tags=["Beneficios Sustentables"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=BeneficioSustentable, status_code=201)
async def create_beneficio(beneficio: BeneficioSustentable):
    """
    Crea un nuevo beneficio sustentable.

    Args:
        beneficio (BeneficioSustentable): Objeto de beneficio sustentable a crear.

    Returns:
        BeneficioSustentable: El beneficio sustentable creado.
    """
    return await BeneficioService.create_beneficio(beneficio)

@router.get("/", response_model=List[BeneficioSustentable])
async def get_beneficios():
    """
    Obtiene todos los beneficios sustentables.

    Returns:
        List[BeneficioSustentable]: Lista de beneficios sustentables.
    """
    return await BeneficioService.get_beneficios()

@router.get("/{id}", response_model=BeneficioSustentable)
async def get_beneficio(id: str):
    """
    Obtiene un beneficio sustentable por su ID.

    Args:
        id (str): ID del beneficio sustentable.

    Returns:
        BeneficioSustentable: El beneficio sustentable encontrado.
    """
    beneficio = await BeneficioService.get_beneficio(id)
    if not beneficio:
        raise HTTPException(status_code=404, detail=f"Beneficio con ID {id} no encontrado.")
    return beneficio

@router.put("/{id}", response_model=BeneficioSustentable)
async def update_beneficio(id: str, beneficio: BeneficioSustentable):
    """
    Actualiza un beneficio sustentable existente.

    Args:
        id (str): ID del beneficio sustentable a actualizar.
        beneficio (BeneficioSustentable): Objeto de beneficio sustentable actualizado.

    Returns:
        BeneficioSustentable: El beneficio sustentable actualizado.
    """
    updated_beneficio = await BeneficioService.update_beneficio(id, beneficio)
    if not updated_beneficio:
        raise HTTPException(status_code=404, detail=f"Beneficio con ID {id} no encontrado.")
    return updated_beneficio

@router.delete("/{id}", response_model=BeneficioSustentable)
async def delete_beneficio(id: str):
    """
    Elimina un beneficio sustentable existente.

    Args:
        id (str): ID del beneficio sustentable a eliminar.

    Returns:
        BeneficioSustentable: El beneficio sustentable eliminado.
    """
    deleted_beneficio = await BeneficioService.delete_beneficio(id)
    if not deleted_beneficio:
        raise HTTPException(status_code=404, detail=f"Beneficio con ID {id} no encontrado.")
    return deleted_beneficio