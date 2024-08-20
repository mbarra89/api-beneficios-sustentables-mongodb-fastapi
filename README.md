# API de Beneficios Sustentables con MongoDB y FastAPI

API RESTful en español utilizando FastAPI y MongoDB para gestionar un catálogo de beneficios sustentables. Este proyecto implementa un CRUD completo siguiendo las mejores prácticas de desarrollo.

## Características

- Implementación de operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para beneficios sustentables.
- Conexión a una base de datos MongoDB utilizando el driver Pymongo.
- Estructura modular y organizada siguiendo buenas prácticas de desarrollo.
- Documentación detallada del código.
- Despliegue de la aplicación en una plataforma como Vercel (opcional).

## Requisitos

- Python 3.7 o superior
- MongoDB (local o en la nube, como MongoDB Atlas)
- Entorno virtual de Python (recomendado)

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/api-beneficios-sustentables-mongodb-fastapi.git
```

2. Entra al directorio del proyecto

```
cd api-beneficios-sustentables-mongodb-fastapi
```

3. Crea y activa un entorno virtual de Python:

```
python -m venv venv
source venv/bin/activate
```

4. Instala las dependencias:

```
pip install -r requirements.txt
```

5. Configura las variables de entorno:

- Crea un archivo _.env_ en la raíz del proyecto.
- Agrega las siguientes variables:

```
MONGODB_URI=mongodb+srv://<usuario>:<contraseña>@<cluster-url>/<base-de-datos>?retryWrites=true&w=majority
MONGODB_DATABASE=beneficios_sustentables
```

- Reemplaza _*<usuario>*_, _<contraseña>_, _<cluster-url>_ y _<base-de-datos>_ con tus credenciales de MongoDB Atlas.

6. Ejecuta la aplicación:

```
fastapi dev main.py
```

La aplicación estará disponible en _http://localhost:8000_.

## Endpoints

- **POST /beneficios**: Crea un nuevo beneficio sustentable.
- **GET /beneficios**: Obtiene todos los beneficios sustentables.
- **GET /beneficios/{id}**: Obtiene un beneficio sustentable por su ID.
- **PUT /beneficios/{id}**: Actualiza un beneficio sustentable existente.
- **DELETE /beneficios/{id}**: Elimina un beneficio sustentable.

##  Despliegue (opcional)

Crea una cuenta en Vercel: https://vercel.com/
Vincula tu repositorio de GitHub a Vercel.
Configura las variables de entorno en Vercel.
Despliega tu aplicación.

##  Contribución

Si encuentras algún problema o tienes sugerencias de mejora, no dudes en abrir un issue o enviar un pull request.
Licencia
Este proyecto se distribuye bajo la Licencia MIT.

## Licencia

Este proyecto se distribuye bajo la Licencia MIT.

```
Este README.md cubre los aspectos más relevantes de tu proyecto, incluyendo una descripción general, requisitos, instalación, endpoints, despliegue opcional y información de contribución y licencia. Puedes ajustar o ampliar el contenido según tus necesidades.
```
