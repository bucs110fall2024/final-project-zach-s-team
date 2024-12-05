import random
import json

class Quiz:
    def __init__(self):
        """
        initializes a new quiz
        args: none
        return: none
        """
        self.unusedCountries = []
        data = json.load(open("etc/countries.json"))
        for i in data:
            self.unusedCountries.append(i["name"])
        self.newCountry()

    def newCountry(self):
        """
        chooses a random country whose flag is to be displayed
        args: none
        return: none
        """
        country = random.choice(self.unusedCountries)
        self.unusedCountries.remove(country)
        self.currentCountry = country