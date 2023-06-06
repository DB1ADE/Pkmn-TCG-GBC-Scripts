import os

# file paths
inFile = "arm.sav"
outfile = "armmax.sav"

# cards
cardsOffset = 0x4100
numCards = 228
firstCardOffset = 0x01

# decks: my Decks (4x) Diary
decksOffset = 0x4200
nextDeckOffset = 0x54
cardsInDeckOffset = 0x18
numCardsInDeck = 60

 # read file
with open(inFile, "rb") as file:
    data = bytearray(file.read())

# count cards in decks
cardsInDecks = [0] * (firstCardOffset + numCards)

for d in range(0,4):
    deckOffset = decksOffset + d * nextDeckOffset
    for c in range(0, numCardsInDeck):
        cardOffset = deckOffset + cardsInDeckOffset + c
        cardId = data[cardOffset]
        if cardId != 0x00:
            cardsInDecks[cardId] += 1

# maximaze cards in storage
for cardId in range(firstCardOffset, firstCardOffset + numCards):
    haveCardsInDecks = cardsInDecks[cardId]
    cardOffset = cardsOffset + cardId
    data[cardOffset] = 99 - haveCardsInDecks

# write file
with open(outfile, "wb") as file:
    file.write(data)
