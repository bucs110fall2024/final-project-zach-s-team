class Card:

    def __init__(self, suit, value, side):
        """
        initializes a card object
        args:
            - suit (str): suit of the card
            - value (str): the numerical (2-9) or alphabetical (J, Q, K, A) value of the card
            - side (str): the side the card will initially be facing (either "up" or "down")
        return: Card
        """

        self.suit = suit
        self.value = value
        self.side = side


    def face(self, side):
        """
        sets the card object to be either face up or down. if no arguments are given, return the cards current orientation
        args:
            - side (str): side to face, either "up" or "down"
        return: str
        """

        if not side: return self.side
        
        self.side = side

        # add code to visually flip card
