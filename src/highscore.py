class Highscore:
    def __init__(self):
        """
        initiates the highscore module
        args: None
        return: None
        """
        self.file = "etc/highscore.txt"

    def get(self):
        """
        gets the highscore
        args: None
        return: highscore (str)
        """
        data = open(self.file)
        highscore = data.read()
        data.close()
        return highscore
    
    def set(self, highscore):
        """
        sets the highscore
        args: highscore (any)
        return: None
        """
        data = open(self.file, 'w')
        data.write(str(highscore))
        data.close()
