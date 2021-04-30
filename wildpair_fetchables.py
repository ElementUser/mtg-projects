# This script takes in a list of creature cards in a deck list, calculates the total power and toughness of each creature,
# then categorizes that creature depending on this number.

# Data structure: List of indexes, where the index equals the creature's total power and toughness.
# Each index contains a list of creatures. The creature will be placed in this list.

# Wild Pair card details: https://gatherer.wizards.com/pages/card/Details.aspx?multiverseid=416953

import requests
import scrython
import time

# Decklist from my Arcades deck: https://deckstats.net/decks/144326/1493742-arcades-wall-midrange-aggro/en

# Deckstats API calls
URL = "https://deckstats.net/api.php"

# Change the 'owner_id' and 'id' fields based on the deck you want to look up
PARAMS = {
    "action": "get_deck",
    "id_type": "saved",
    "owner_id": 144326,
    "id": 1493742,
    "response_type": "json",
}

response = requests.get(url=URL, params=PARAMS)
jsonBody = response.json()
totalPowerToughnessDict = {}

# Parse JSON response
for section in jsonBody.get("sections"):
    for deckstatsCard in section.get("cards"):
        # This call is the slowest step in the Script, but API rate limits have to be respected.
        # Reference: https://github.com/NandaScott/Scrython#key-notes
        time.sleep(0.1)
        card = scrython.cards.Named(fuzzy=deckstatsCard.get("name"))

        # Only proceed if the card type is a creature
        if "creature".lower() in card.type_line().lower():
            sumPowerToughness = int(card.power()) + int(card.toughness())
            if sumPowerToughness not in totalPowerToughnessDict:
                totalPowerToughnessDict[sumPowerToughness] = [card.name()]
            else:
                # TODO: Sort entries in the dictionary alphabetically in-place
                totalPowerToughnessDict[sumPowerToughness].append(card.name())

# sorted(dict) sorts the dictionary by key (ascending)
finalString = ""
for powerToughnessScore in sorted(totalPowerToughnessDict):
    finalString += "\n" + str(powerToughnessScore) + ": "
    for creature in totalPowerToughnessDict[powerToughnessScore]:
        finalString += creature + ", "
    finalString = finalString.rstrip(", ")

print(finalString)
