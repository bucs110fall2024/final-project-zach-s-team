from restcountries import RestCountryApiV2 as api

class Flag:

    def __init__(self, country, x, y):
        """
        creates a Flag object
        args:
            - country (str): the country whose flag is to be displayed
            - x (int): the flag's x pos
            - y (int): the flag's y pos
        """
        self.x = x
        self.y = y
        code = api.get_countries_by_name(country, filters=["alpha2Code"])
        self.img = f"assets/flags/{code}.svg"
