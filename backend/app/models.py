from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class CardMetadata(Base):
    __tablename__ = "card_metadata"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    image_url = Column(String)
    set_name = Column(String)

class InventoryItem(Base):
    __tablename__ = "inventory_items"

    id = Column(String, primary_key=True, default=generate_uuid)
    card_id = Column(String, ForeignKey("card_metadata.id"))
    condition = Column(String, nullable=True)
    location = Column(String, nullable=True)

    card = relationship("CardMetadata")

class Deck(Base):
    __tablename__ = "decks"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String)

    cards = relationship("InventoryItem", secondary="deck_cards", backref="decks")

class DeckCard(Base):
    __tablename__ = "deck_cards"

    deck_id = Column(String, ForeignKey("decks.id"), primary_key=True)
    inventory_item_id = Column(String, ForeignKey("inventory_items.id"), primary_key=True)

