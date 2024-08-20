from app.models.beneficio import BeneficioSustentable
from app.core.database import db
import uuid

class BeneficioService:
    @staticmethod
    async def create_beneficio(beneficio: BeneficioSustentable):
        """
        Crea un nuevo beneficio sustentable en la base de datos.

        Args:
            beneficio (BeneficioSustentable): Objeto de beneficio sustentable a crear.

        Returns:
            BeneficioSustentable: El beneficio sustentable creado.
        """
        beneficio_data = beneficio.model_dump()
        if beneficio_data['id'] is None:
            beneficio_data['id'] = str(uuid.uuid4())
        result = await db.beneficios.insert_one(beneficio_data)
        created_beneficio = await db.beneficios.find_one({"_id": result.inserted_id})
        return BeneficioSustentable(**created_beneficio)

    @staticmethod
    async def get_beneficios():
        """
        Obtiene todos los beneficios sustentables de la base de datos.

        Returns:
            List[BeneficioSustentable]: Lista de beneficios sustentables.
        """
        beneficios = []
        async for doc in db.beneficios.find():
            beneficios.append(BeneficioSustentable(**doc))
        return beneficios

    @staticmethod
    async def get_beneficio(id: str):
        """
        Obtiene un beneficio sustentable por su ID.

        Args:
            id (str): ID del beneficio sustentable.

        Returns:
            BeneficioSustentable: El beneficio sustentable encontrado.
        """
        beneficio = await db.beneficios.find_one({"_id": id})
        if beneficio:
            return BeneficioSustentable(**beneficio)
        return None

    @staticmethod
    async def update_beneficio(id: str, beneficio: BeneficioSustentable):
        """
        Actualiza un beneficio sustentable existente.

        Args:
            id (str): ID del beneficio sustentable a actualizar.
            beneficio (BeneficioSustentable): Objeto de beneficio sustentable actualizado.

        Returns:
            BeneficioSustentable: El beneficio sustentable actualizado.
        """
        result = await db.beneficios.update_one({"_id": id}, {"$set": beneficio.dict()})
        if result.modified_count == 1:
            updated_beneficio = await db.beneficios.find_one({"_id": id})
            return BeneficioSustentable(**updated_beneficio)
        return None

    @staticmethod
    async def delete_beneficio(id: str):
        """
        Elimina un beneficio sustentable existente.

        Args:
            id (str): ID del beneficio sustentable a eliminar.

        Returns:
            BeneficioSustentable: El beneficio sustentable eliminado.
        """
        result = await db.beneficios.delete_one({"_id": id})
        if result.deleted_count == 1:
            deleted_beneficio = await db.beneficios.find_one({"_id": id})
            return BeneficioSustentable(**deleted_beneficio)
        return None