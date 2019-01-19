from sqlalchemy import create_engine, Sequence, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/random_life', echo=True)
Base = declarative_base()

class Days(Base):
    __tablename__ = 'days'  # change to "days" in production

    id = Column(Integer, Sequence('day_id_seq'), primary_key=True)
    created_date = Column(DateTime, default=datetime.date.today())
    eating_style = Column(String(100))
    dietary_style = Column(String(100))
    end_date = Column(DateTime)
    fast_duration = Column(String(100))
    exercise_style = Column(String(100))

Base.metadata.create_all(engine)

