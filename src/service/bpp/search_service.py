
from odoo.env import Environment
from fastapi import Header, Request
from security.validator import validateHeaders

def search_service(env: Environment, headers: Header, request: Request):
    isHeadersValid = validateHeaders(headers)
    if not isHeadersValid:
        return None
    return {'status': 'ACK'}