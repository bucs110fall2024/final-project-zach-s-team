import json

class NameToCC:
    def get(self, country):
        """
        converts a country name to its 2 letter country code
        args:
            - country (str): country name
        return: str
        """
        file = open("etc/countries.json")
        data = json.load(file)
        file.close()
        for i in data:
            if i["name"] == country:
                return i["alpha2"]
            