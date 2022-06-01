import re
from tkinter.tix import Tree
from fastapi import FastAPI, Depends, Header, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware

from gensim.models.doc2vec import Doc2Vec

from sqlalchemy.orm import Session
from sqlalchemy import or_
import models.novel_datas
import database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

m = Doc2Vec.load('./doc2vec/doc2vec.model')

    
@app.get("/api/novel/get_all")
async def getNovels(db: Session = Depends(database.get_db), page: int = 1):
    data = models.novel_datas.Novel_data
    stop = (page - 1) * 10
    nove  = db.query(data.id, data.title, data.general_lastup, data.writer, data.ncode, data.story).offset(stop).limit(10).all()
    return nove

@app.get("/api/novel/count")
async def countNovels(db: Session = Depends(database.get_db)):
    data = models.novel_datas.Novel_data
    count = db.query(data).count()
    return count

@app.get("/api/novel/get_by_keyword")
async def getNovelByKeyword(db: Session = Depends(database.get_db), page: int = 1, keyword: str = ""):
    data = models.novel_datas.Novel_data
    keyword = "%" + keyword + "%"
    stop = (page - 1) * 10
    nove = db.query(data.id, data.title, data.general_lastup, data.writer, data.ncode, data.story, data.keyword).filter(or_(data.title.like(keyword), data.story.like(keyword), data.keyword.like(keyword))).offset(stop).limit(10).all()
    return nove

@app.get("/api/novel_by_keyword/count")
async def countKeywordNovels(db: Session = Depends(database.get_db), keyword: str = ""):
    data = models.novel_datas.Novel_data
    keyword = "%" + keyword + "%"
    count = db.query(data.title, data.story, data.keyword).filter(or_(data.title.like(keyword), data.story.like(keyword), data.keyword.like(keyword))).count()
    return count

@app.get("/api/novel/get/{novel_id}")
async def getNovel(novel_id :int, db: Session = Depends(database.get_db)):
    data = models.novel_datas.Novel_data
    nove  = db.query(data).filter(data.id == novel_id).all()
    return nove



@app.get("/api/siminovel/get/{novel_id}")
async def getSimilarNovels(novel_id :int,):
    return m.docvecs.most_similar(novel_id)
    

