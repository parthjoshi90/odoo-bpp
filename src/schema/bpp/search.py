from pydantic import BaseModel, Field
from typing import List
from schema.bpp.context import Context


class Image(BaseModel):
    description: str = Field(description="'Image of an object. <br/><br/> A url based image will look like <br/><br/>```uri:http://path/to/image``` <br/><br/> An image can also be sent as a data string. For example : <br/><br/> ```data:js87y34ilhriuho84r3i4```'") 

class Descriptor(BaseModel):
    name: str
    code: str
    symbole: str
    short_desc: str
    long_desc: str
    images: List[Image]


class Item(BaseModel):
    descriptor: Descriptor


class Location(BaseModel):
    gps: str


class End(BaseModel):
    location: Location = None


class Fulfillment(BaseModel):
    end:End = None


class Intent(BaseModel):
    item: Item
    fulfillment: Fulfillment


class Message(BaseModel):
    intent: Intent = None


class SearchRequest(BaseModel):
    context: Context = None
    message: Message = None