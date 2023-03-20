from app.models.schemas.articles import ArticleBase, ArticleDisplay
from app.models.domains.articles import Article
from sqlalchemy.orm.session import Session
from datetime import datetime


def create_new_article(db: Session, request: ArticleBase):
    new_article = Article(
        img_url=request.img_url,
        title=request.title,
        content=request.content,
        creator=request.creator,
        date=datetime.now()
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
