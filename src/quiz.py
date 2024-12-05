import random
import json

class Quiz:
    def __init__(self):
        self.unusedCountries = []
        data = json.load(open("etc/countries.json"))
        for i in data:
            self.unusedCountries.append(i["name"])

        self.newCountry()

    def newCountry(self):
        country = random.choice(self.unusedCountries)
        self.unusedCountries.remove(country)
        self.currentCountry = country