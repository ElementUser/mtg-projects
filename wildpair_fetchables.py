# This script takes in a list of creature cards in a deck list, calculates the total power and toughness of each creature,
# then categorizes that creature depending on this number.

# Data structure: List of indexes, where the index equals the creature's total power and toughness.
# Each index contains a list of creatures. The creature will be placed in this list.

# Wild Pair card details: https://gatherer.wizards.com/pages/card/Details.aspx?multiverseid=416953

import scrython, requests

# Decklist from my Arcades deck: https://deckstats.net/decks/144326/1493742-arcades-wall-midrange-aggro/en

# Deckstats API calls
# URL = "https://deckstats.net/api.php"

# PARAMS = {
#     "action":  "get_deck",
#     "id_type": "saved",
#     "owner_id": 144326,
#     "id": 1493742,
#     "response_type": "json",
# }

# response = requests.get(url=URL, params=PARAMS)
# print(response.text)


# Temp stuff
deckCreatureList = [
    "Angelic Wall", "Arcades, the Strategist", "Axebane Guardian", "Birds of Paradise", "Carven Caryatid", "Consulate Skygate", "Crashing Drawbridge", "Drift of Phantasms", "Fortified Rampart", "Glacial Wall", "Hover Barrier", "Jeskai Barricade", "Jungle Barrier", 
    "Marble Titan", "Oathsworn Giant", "Orator of Ojutai", "Overgrown Battlement", "Perimeter Captain", "Resolute Watchdog", "Shield Sphere", "Stalwart Shield-Bearers", "Sunscape Familiar", "Tetsuko Umezawa, Fugitive", "Tree of Redemption",
    "Vine Trellis", "Wall of Blossoms", "Wall of Denial", "Wall of Frost", "Wall of Junk", "Wall of Mulch", "Wall of Omens", "Wall of Runes", "Wall of Shards", "Wall of Stolen Identity", "Wall of Tanglecord", "Wall of Tears", "Wall of Vines"
]

totalPowerToughnessDict = {}
finalString = "Power & Toughness Sum map for Wild Pair:\n"

for creature in deckCreatureList:
    card = scrython.cards.Named(fuzzy=creature)
    sumPowerToughness = int(card.power()) + int(card.toughness())
    if str(sumPowerToughness) not in totalPowerToughnessDict:
        totalPowerToughnessDict[str(sumPowerToughness)] = [card.name()]
    else:
        totalPowerToughnessDict[str(sumPowerToughness)].append(card.name())

# sorted(dict) sorts the dictionary by key (ascending)
for powerToughnessScore in sorted(totalPowerToughnessDict):
    finalString += "\n" + powerToughnessScore + ": "
    for creature in totalPowerToughnessDict[powerToughnessScore]:
        finalString += creature + ", "
    finalString = finalString.rstrip(', ')

print(finalString)