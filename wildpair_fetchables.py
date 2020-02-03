# This script takes in a list of creature cards in a deck list, calculates the total power and toughness of each creature,
# then categorizes that creature depending on this number.

# Data structure: List of indexes, where the index equals the creature's total power and toughness.
# Each index contains a list of creatures. The creature will be placed in this list.

# Wild Pair card details: https://gatherer.wizards.com/pages/card/Details.aspx?multiverseid=416953

import scrython

# Decklist from my Arcades deck: https://deckstats.net/decks/144326/1493742-arcades-wall-midrange-aggro/en

deckCreatureList = [
    "Angelic Wall", "Axebane Guardian"
]

totalPowerToughnessDict = {}

for creature in deckCreatureList:
    card = scrython.cards.Named(fuzzy=creature)
    sumPowerToughness = int(card.power()) + int(card.toughness())
    if str(sumPowerToughness) not in totalPowerToughnessDict:
        totalPowerToughnessDict[str(sumPowerToughness)] = [card.name()]
    else:
        totalPowerToughnessDict[str(sumPowerToughness)].append(card.name())

for powerToughnessScore in totalPowerToughnessDict:
    for creature in totalPowerToughnessDict[powerToughnessScore]:
        print(powerToughnessScore)
        print(creature)