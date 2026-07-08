from fastapi import APIRouter

router = APIRouter(
    tags=["Health"]
)

@router.get("/")
def health_check():
    return {"message" : "welcome to Expendo Backend."}