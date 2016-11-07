import random
from PySide.QtGui import *
import Jaeger_View, Jaeger_Model
b = 15

class Controller(QWidget):
    def __init__(self,parent=None):
        """
        Konstruktor
        :param parent:
        """
        super().__init__(parent)
        # Initialisierung des Models
        self.__m = Jaeger_Model.Model()
        # Initialisierung der View
        self.__v = Jaeger_View.Ui_MainWindow()
        self.__v.setupUi(self.__v)



        #Erstellung einer Liste
        self.__b = []
        #Befühlung der Liste mit Button-Values
        for i in range(self.__m.M):
            # Idee von Pierre
            b = getattr(self.__v,"B{0}".format(i))
            self.__b.append(b)
            #self.__b.append(self.__v.B+i) erste Idee, doch TypeError wegen QButton + int



        self.__v.neu.clicked.connect(self.start)
        self.__v.Beenden.clicked.connect(SystemExit(0))
        #Verbindet alle Buttons mit der
        for i in self.__b:
            b.clicked.connect(lambda b=b:self.clickedButton(b))

    def setStatistik(self):
        """
        Setzt die Statistikdaten in die jeweiligen Labels während des Spieles ein
        :return: void
        """
        self.__v.korrektV.setText(str(self.__m.getOffen()))
        self.__v.falschV.setText(str(self.__m.getFalsch()))
        self.__v.gesamtV.setText(str(self.__m.getGesamt()))
        self.__v.spieleV.setText(str(self.__m.getSpiele()))

    def start(self):
        """
        Setzt Statistiken zurück oder zählt hoch und enabled die Buttons bei Start einer Runde
        :return: void
        """
        #Setzung der Statistikdaten bei Start des Spieles oder einer neuen Runde
        self.__m.setlButton(-1)
        self.__m.setOffen(15)
        self.__m.setRichtig(0)
        self.__m.setFalsch(0)
        self.__m.setSpiele(self.__m.getSpiele()+1)

        for i in self.__b():
            b.setEnabled(True)

        self.setStatistik()
        self.randomButtons()

    def randomButtons(self):
        """
        Erzeugt eine Liste mit der Anzahl der Buttonsmöglichkeiten und
        :return: void
        """
        M = list(range(self.__m.M))
        for i in self.__b:
            z = random.randint(0,len(z)-1)
            #Mit pop() wird wird die Zufallszahl aus der Liste "rausgeworfen" und übergeben
            zahl = M.pop(z)
            i.setText(str(str(zahl+1)))

    def clickedButton(self, button):
        """

        :param button:
        :return:
        """
        cButton = int(button.text())

        if cButton == self.__m.getlButton()+1:
            button.setEnabled(False)
            self.__m.setlButton(self.__m.getlButton()+1)
            self.__m.setRichtig(self.__m.getRichtig())
            self.__m.setOffen(self.__m.getOffen())
        else:
            self.__m.setFalsch(self.m.getFalsch())
        self.setStatistik()

        if self.__m.getOffen() == 0:
            self.__v.textEdit.setText("GG Mate! Du bist 1 cooler Dude")

