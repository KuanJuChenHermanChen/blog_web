from pydantic import BaseModel
from datetime import datetime


class ArticleBase(BaseModel):
    img_url: str
    title: str
    content: str
    creator: str


class ArticleDisplay(BaseModel):
    id: int
    img_url: str
    title: str
    content: str
    creator: str
    date: datetime

    class Config:
        orm_mode = True
