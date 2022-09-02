
from fastapi import APIRouter
from routes.endpoints.partner import router as partner_routes
from routes.endpoints.products import router as product_routes
from routes.endpoints.company import router as company_routes

router = APIRouter()

router.include_router(partner_routes)
router.include_router(product_routes)
router.include_router(company_routes)

