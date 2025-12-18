from sqlalchemy.orm import Session
from tcgdexsdk import TCGdex
from ..models import CardMetadata

tcgdex = TCGdex("en")

def get_card_details(db: Session, card_id: str):
    # 1. Check DB
    db_card = db.query(CardMetadata).filter(CardMetadata.id == card_id).first()
    if db_card:
        return db_card

    # 2. Fetch from API
    try:
        card = tcgdex.card.getSync(card_id)
        
        if not card:
            return None

        # Construct image URL
        image_url = f"{card.image}/high.png" if card.image else None

        new_card = CardMetadata(
            id=card.id,
            name=card.name,
            image_url=image_url,
            set_name=card.set.name if card.set else None
        )
        
        db.add(new_card)
        db.commit()
        db.refresh(new_card)
        return new_card
        
    except Exception as e:
        print(f"Error fetching card {card_id}: {e}")
        return None
