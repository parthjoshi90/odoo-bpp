from fastapi import APIRouter, Header, Depends
from service.bpp.search_service import search_service
from schema.bpp.search import SearchRequest
from schema.bpp.ack import Ack
from odoo.env import odoo_env
from odoo.env import Environment
from typing import Union

router = APIRouter(tags=["Protocol BPP"])

@router.post("/search", response_model=Ack)
async def protocol_search(request: SearchRequest, env: Environment = Depends(odoo_env), headers:  Union[str, None] = Header(default=None)):
    response = search_service(env, headers, request)
    return response
