from fastapi import APIRouter, HTTPException
from schemas.request_schema import ShayriRequest
from services.shayri_generator import ShayriService

router = APIRouter()
shayri_service = ShayriService()

@router.post("/generate")
def generate_shayri(request: ShayriRequest):
    try:
        user_data = request.dict()
        conversation = user_data.pop("latest_conversation")
        shayri = shayri_service.generate_shayri(user_data, conversation)
        return {"shayri": shayri}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
