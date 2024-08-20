from fastapi import FastAPI
from mangum import Mangum
from app.api.routers.beneficios import router as beneficios_router

# Crear la aplicación FastAPI
app = FastAPI()

# Incluir el router de beneficios sustentables
app.include_router(beneficios_router)

# Crear un manejador de Lambda usando Mangum
handler = Mangum(app)

# El punto de entrada para AWS Lambda
def lambda_handler(event, context):
    return handler(event, context)
