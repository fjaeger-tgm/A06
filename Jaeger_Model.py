import random

class Model:
    """
    Speicherort für alle Statistikvariablen
    """


    def __init__(self):
        self.random = random.random()
        self.m = 15
        self.lButton = -1
        self.__gesamt = 0
        self.__offen = 15
        self.__richtig = 0
        self.__falsch = 0
        self.__spiele = 1

        def setMoeglichkeit(x):
            self.m = x

        def setlButton(x):
            """

            :param x:
            :return:
            """
            self.lButton = x

        def setGesamt(x):
            """

            :param x:
            :return:
            """
            self.__gesamt = x

        def setOffen(x):
            """

            :param x:
            :return:
            """
            self.__offen = x

        def setRichtig(x):
            """

            :param x:
            :return:
            """
            self.__richtig = x

        def setFalsch(x):
            """

            :param x:
            :return:
            """
            self.__falsch = x

        def setSpiele(x):
            """

            :param x:
            :return:
            """
            self.__spiele = x

        def getlButton():
            """
            :return:
            """
            return self.lButton

        def getGesamt():
            """
            :return:
            """
            return self.__lButton

        def getOffen():
            """
            :return:
            """
            return self.__offen

        def getFalsch():
            """
            :return:
            """
            return self.__falsch

        def getRichtig():
            """
            :return:
            """
            return self.__richtig

        def getSpiele():
            """
            :return:
            """
            return self.__spiele