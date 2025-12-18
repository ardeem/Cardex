import unittest
import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.database import Base
from backend.app.models import CardMetadata
from backend.app.services.card_service import get_card_details

class TestCardService(unittest.TestCase):
    def setUp(self):
        # Use in-memory SQLite for testing
        self.engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.db = self.Session()

    def tearDown(self):
        self.db.close()
        Base.metadata.drop_all(self.engine)

    def test_get_card_details_api_fetch_and_cache(self):
        # 1. Ensure DB is empty
        card_id = "swsh3-136"
        db_card = self.db.query(CardMetadata).filter(CardMetadata.id == card_id).first()
        self.assertIsNone(db_card)

        # 2. Fetch card (should hit API and save to DB)
        print(f"Fetching {card_id} from API...")
        card = get_card_details(self.db, card_id)
        
        self.assertIsNotNone(card)
        self.assertEqual(card.id, card_id)
        self.assertEqual(card.name, "Furret")
        
        # 3. Verify it's in DB now
        db_card_after = self.db.query(CardMetadata).filter(CardMetadata.id == card_id).first()
        self.assertIsNotNone(db_card_after)
        self.assertEqual(db_card_after.name, "Furret")

    def test_get_card_details_from_cache(self):
        # 1. Pre-populate DB
        card_id = "test-card"
        fake_card = CardMetadata(id=card_id, name="Test Card", image_url="http://test.com/img.png", set_name="Test Set")
        self.db.add(fake_card)
        self.db.commit()

        # 2. Fetch card (should return from DB)
        card = get_card_details(self.db, card_id)
        
        self.assertIsNotNone(card)
        self.assertEqual(card.name, "Test Card")

if __name__ == '__main__':
    unittest.main()
