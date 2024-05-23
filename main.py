from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4, UUID

app = FastAPI()

# Pydantic models
class Article(BaseModel):
    id: UUID
    name: str
    tags: List[str]
    creation_date: datetime
    modification_date: Optional[datetime] = None
    publication_date: Optional[datetime] = None
    category: str
    content_path: str
    thumbnail: str
    subtitle: Optional[str] = None

# In-memory database
db: List[Article] = []

@app.post("/articles/", response_model=Article)
def create_article(article: Article):
    db.append(article)
    return article

@app.get("/articles/", response_model=List[Article])
def get_articles():
    return db

@app.get("/articles/{article_id}", response_model=Article)
def get_article(article_id: UUID):
    for article in db:
        if article.id == article_id:
            return article
    raise HTTPException(status_code=404, detail="Article not found")

@app.put("/articles/{article_id}", response_model=Article)
def update_article(article_id: UUID, updated_article: Article):
    for index, article in enumerate(db):
        if article.id == article_id:
            db[index] = updated_article
            return updated_article
    raise HTTPException(status_code=404, detail="Article not found")

@app.delete("/articles/{article_id}")
def delete_article(article_id: UUID):
    for index, article in enumerate(db):
        if article.id == article_id:
            del db[index]
            return {"message": "Article deleted successfully"}
    raise HTTPException(status_code=404, detail="Article not found")
