from sqlalchemy import DateTime, Text, Column, Integer, Float

from database import Base

class Novel_data(Base):
    __tablename__ = "novel_data"
    
    index = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    ncode = Column(Text)
    userid = Column(Integer)
    writer = Column(Text)
    story = Column(Text)
    genre = Column(Integer)
    keyword = Column(Text)
    general_firstup = Column(Text)
    general_lastup = Column(Text)
    novel_type = Column(Integer)
    end = Column(Integer)
    general_all_no = Column(Integer)
    length = Column(Integer)
    time = Column(Integer)
    global_point = Column(Integer)
    daily_point = Column(Integer)
    weekly_point = Column(Integer)
    monthly_point = Column(Integer)
    quarter_point = Column(Integer)
    yearly_point = Column(Integer)
    fav_novel_cnt = Column(Integer)
    novelupdated_at = Column(DateTime)
    searchbykey = Column(Text)