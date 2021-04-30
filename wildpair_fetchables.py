"""
This script takes in a list of creature cards in a deck list from the Deckstats API, 
    calculates the total power and toughness of each creature, then categorizes that creature depending on this number.

Data structure: dictionary, where the key equals the creature's total power and toughness, 
    and the value is a list of creatures (sorted alphabetically).

Wild Pair card details: https://gatherer.wizards.com/pages/card/Details.aspx?multiverseid=416953
"""

import bisect
import requests
import scrython
import time

# Decklist from my 'Arcades, the Strategist' deck: https://deckstats.net/decks/144326/1493742-arcades-wall-midrange-aggro/en

# Deckstats API call
URL = "https://deckstats.net/api.php"
PARAMS = {
    "action": "get_deck",
    "id_type": "saved",
    "owner_id": 144326,  # change this if you wish to look up a deck from another owner
    "id": 1493742,  # change this if you wish to look up a different deck
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
                # Adds the card name into the list, alphabetically sorted upon insertion
                bisect.insort(totalPowerToughnessDict[sumPowerToughness], card.name())

# sorted(dict) sorts the dictionary by key (ascending)
outputString = ""
for powerToughnessScore in sorted(totalPowerToughnessDict):
    outputString += "\n" + str(powerToughnessScore) + ": "
    for creature in totalPowerToughnessDict[powerToughnessScore]:
        outputString += creature + ", "
    outputString = outputString.rstrip(", ")

print(outputString)
