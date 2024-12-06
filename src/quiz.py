import random
import json

class Quiz:
    def __init__(self):
        """
        initializes a new quiz
        args: none
        return: none
        """
        self.correctCountries = 0
        self.unusedCountries = []
        file = open("etc/countries.json")
        data = json.load(file)
        file.close()
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
        print(self.currentCountry)