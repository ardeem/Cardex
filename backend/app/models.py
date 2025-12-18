from sqlalchemy import Column, String, Integer, Text
from .database import Base

class CardMetadata(Base):
    __tablename__ = "card_metadata"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    image_url = Column(String)
    set_name = Column(String)

