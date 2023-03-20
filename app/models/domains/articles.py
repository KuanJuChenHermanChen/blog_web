from app.db.sql_connection import Base
from sqlalchemy import Column, Integer, String


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    img_url = Column(String)
    title = Column(String)
    content = Column(String)
    creator = Column(String)
    date = Column(String)
