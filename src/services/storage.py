from google.cloud import storage
from src.config import settings
from fastapi import UploadFile
import io

class StorageService:
    def __init__(self):
        # Al estar en Cloud Run, no hace falta service_account.json explícito
        # Usará la identidad del servicio automáticamente.
        self.client = storage.Client()
        self.bucket = self.client.bucket(settings.BUCKET_NAME)

    def list_files(self):
        """Lista todos los blobs en el bucket."""
        blobs = self.client.list_blobs(settings.BUCKET_NAME)
        return [{"name": blob.name, "size": blob.size} for blob in blobs]

    def upload_file(self, file: UploadFile):
        """Sube un archivo al bucket."""
        blob = self.bucket.blob(file.filename)
        # file.file es un objeto tipo SpooledTemporaryFile
        blob.upload_from_file(file.file, content_type=file.content_type)
        return {"message": f"Archivo {file.filename} subido exitosamente", "public_url": blob.public_url}

    def delete_file(self, filename: str):
        """Elimina un archivo del bucket."""
        blob = self.bucket.blob(filename)
        if not blob.exists():
            return False
        blob.delete()
        return True