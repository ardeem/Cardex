from tcgdexsdk import TCGdex
import json

tcgdex = TCGdex("en")
card = tcgdex.card.getSync("swsh3-136")

print(f"ID: {card.id}")
print(f"Name: {card.name}")
print(f"Image: {card.image}")
print(f"Set: {card.set.name if card.set else 'None'}")
