class GameData:

    def __init__(self):
        """
        initializes the GameData object
        args: None
        return: None
        """
        self.money = 0
        self.difficultyModes = {
            "easy" : {"initialMoney" : 5000, "targetMoney": 15000},
            "medium" : {"initialMoney" : 5000, "targetMoney": 30000},
            "hard" : {"initialMoney" : 5000, "targetMoney": 50000},
            "gambler" : {"initialMoney" : 1000, "targetMoney": 100000}
        }