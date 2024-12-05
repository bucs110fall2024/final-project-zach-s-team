import json

class NameToCC:
    def get(self, country):
        """
        converts a country name to its 2 letter country code
        args:
            - country (str): country name
        return: str
        """
        data = json.load(open("etc/countries.json"))
        for i in data:
            if i["name"] == country:
                return i["alpha2"]
            