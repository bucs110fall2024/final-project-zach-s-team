import json

class NameToCC:
    def get(self, country):
        data = json.load(open("etc/countries.json"))
        for i in data:
            if i["name"] == country:
                return i["alpha2"]
            