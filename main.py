from fastapi import FastAPI
from app.api.routers.beneficios import router as beneficios_router

# Crear la aplicación FastAPI
app = FastAPI()

# Incluir el router de beneficios sustentables
app.include_router(beneficios_router)

# Punto de entrada de la aplicación
if __name__ == "__main__":
    import uvicorn
    # Ejecutar la aplicación usando Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)