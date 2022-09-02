from pydantic import BaseModel


class Ack(BaseModel):
    status: str