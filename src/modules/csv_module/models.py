from sqlalchemy import Column, Integer, String, Float, Boolean, Date, Index
from src.database import Base

class CSVData(Base):
    __tablename__ = "csv_data"

    id = Column(Integer, primary_key=True)
    appid = Column(Integer)
    name = Column(String)
    release_date = Column(Date)
    required_age = Column(Integer)
    price = Column(Float)
    dlc_count = Column(Integer)
    about_the_game = Column(String)
    supported_languages = Column(String)
    windows = Column(Boolean)
    mac = Column(Boolean)
    linux = Column(Boolean)
    positive = Column(Integer)
    negative = Column(Integer)
    score_rank = Column(Integer, default=0)
    developers = Column(String)
    publishers = Column(String)
    categories = Column(String)
    genres = Column(String)
    tags = Column(String)

    __table_args__ = (
        Index('ix_csv_data_appid', 'appid'),
        Index('ix_csv_data_name', 'name'),
        Index('ix_csv_data_release_date', 'release_date'),
        Index('ix_csv_data_price', 'price'),
    )

    
