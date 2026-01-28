from fastapi import APIRouter, HTTPException, UploadFile, File
from src.services.storage import StorageService

router = APIRouter()
storage_service = StorageService()

@router.get("/files")
def list_files():
    try:
        return storage_service.list_files()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/files")
def upload_file(file: UploadFile = File(...)):
    try:
        return storage_service.upload_file(file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/files/{filename}")
def delete_file(filename: str):
    try:
        success = storage_service.delete_file(filename)
        if not success:
            raise HTTPException(status_code=404, detail="Archivo no encontrado")
        return {"message": f"Archivo {filename} eliminado"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/files/{filename}")
def update_file(filename: str, file: UploadFile = File(...)):
    try:
        result = storage_service.update_file(filename, file)
        if not result:
            raise HTTPException(status_code=404, detail="El archivo que intentas actualizar no existe")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))