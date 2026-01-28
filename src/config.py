import os

class Settings:
    # Se debe definir la variable BUCKET_NAME en Cloud Run al desplegar
    BUCKET_NAME = os.getenv("BUCKET_NAME", "nombre-de-tu-bucket-por-defecto")
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")

settings = Settings()