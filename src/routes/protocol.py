
from fastapi import APIRouter
from routes.protocol_endpoints.search import router as search_routes

router = APIRouter()

router.include_router(search_routes)
