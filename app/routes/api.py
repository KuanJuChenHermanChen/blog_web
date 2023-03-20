from fastapi import APIRouter
from app.routes.modules import article

router = APIRouter()

router.include_router(article.router, prefix="/article", tags=["article"])
