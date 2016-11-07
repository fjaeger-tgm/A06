import random

class Model:
    """
    Speicherort für alle Statistikvariablen
    """


    def __init__(self):
        self.random = random.random()
        self.M = 15
        self.__lButton = 0
        self.__gesamt = 0
        self.__offen = 15
        self.__richtig = 0
        self.__falsch = 0
        self.__spiele = 1

    def setMoeglichkeit(self,x):
        """
        :param x:
        :return: void
        """
        self.M = x

    def setlButton(self,x):
        """

        :param x:
        :return: void
        """
        self.__lButton = x

    def setGesamt(self,x):
        """

        :param x:
        :return: void
        """
        self.__gesamt = x

    def setOffen(self,x):
        """

        :param x:
        :return: void
        """
        self.__offen = x

    def setRichtig(self,x):
        """

        :param x:
        :return: void
        """
        self.__richtig = x

    def setFalsch(self,x):
        """

        :param x:
        :return: void
        """
        self.__falsch = x

    def setSpiele(self,x):
        """

        :param x:
        :return: void
        """
        self.__spiele = x

    def getlButton(self):
        """
        :return:den letzen gedrückten Button
        """
        return self.__lButton

    def getGesamt(self):
        """
        :return: die gesamte Anzahl an gedrückten Buttons
        """
        return self.__lButton

    def getOffen(self):
        """
        :return: Buttons die nicht gedrückt wurden
        """
        return self.__offen

    def getFalsch(self):
        """
        :return: Buttons die falsch gedrückt wurden
        """
        return self.__falsch

    def getRichtig(self):
        """
        :return:
        """
        return self.__richtig

    def getSpiele(self):
        """
        :return: Buttons die richtig gedrückt wurden
        """
        return self.__spiele