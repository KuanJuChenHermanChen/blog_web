from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.models.schemas.articles import ArticleBase, ArticleDisplay
from app.db.sql_connection import get_db
from app.controllers import articles

router = APIRouter()


@router.get("/all")
def get_all_articles(db: Session = Depends(get_db)):
    return articles.get_all_articles(db)


@router.post("/")
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return articles.create_new_article(db, request)
