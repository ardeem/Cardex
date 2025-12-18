from tcgdexsdk import TCGdex, Language

tcgdex = TCGdex() # Initialize with default language (English)

# Initialize with language as string
tcgdex = TCGdex("en")

# Sync usage
card = tcgdex.card.getSync("swsh3-136")

print(card.attacks)