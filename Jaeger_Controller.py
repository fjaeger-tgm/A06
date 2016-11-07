import sys,random
#from PySide.QtGui import *
from PySide import QtGui
import Jaeger_View, Jaeger_Model
b = 15

class Controller(QtGui.QWidget):
    def __init__(self,parent=None):
        """
        Konstruktor
        :param parent:
        """
        super().__init__(parent)

        # Initialisierung der View
        self.__v = Jaeger_View.Ui_MainWindow()
        self.__v.setupUi(self)
        # Initialisierung des Models
        self.__m = Jaeger_Model.Model()



        #Erstellung einer Liste
        self.__b = []
        #Befühlung der Liste mit Button-Values
        for i in range(self.__m.M):
            # Idee von Pierre
            b = getattr(self.__v,"B{0}".format(i))
            self.__b.append(b)
            #self.__b.append(self.__v.B+i) erste Idee, doch TypeError wegen QButton + int



        self.__v.neu.clicked.connect(self.start)
        self.__v.Beenden.clicked.connect(self.ende)
        #Verbindet alle Buttons mit der clickedButton-Funktion
        #Code von Pierre
        for b in self.__b:
            b.clicked.connect(lambda b=b:self.clickedButton(b))

        self.randomButtons()
        self.setStatistik()

    def ende(self):
        sys.exit(0)

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

        for i in self.__b:
            i.setEnabled(True)

        self.setStatistik()
        self.randomButtons()

    def randomButtons(self):
        """
        Erzeugt eine Liste mit der Anzahl der Buttonsmöglichkeiten und
        :return: void
        """
        M = list(range(self.__m.M))
        for i in self.__b:
            z = random.randint(0,len(M)-1)
            #Mit pop() wird wird die Zufallszahl aus der Liste "rausgeworfen" und übergeben
            zahl = M.pop(z)
            i.setText(str(str(zahl+1)))

    def clickedButton(self, b):
        """

        :param b: Ausgewählter Button
        :return: void
        """
        cButton = int(b.text())

        if cButton == self.__m.getlButton()+1:
            b.setEnabled(False)
            self.__m.setlButton(self.__m.getlButton()+1)
            self.__m.setRichtig(self.__m.getRichtig())
            self.__m.setOffen(self.__m.getOffen()-1)
        else:
            self.__m.setFalsch(self.__m.getFalsch()+1)
        self.setStatistik()

        if self.__m.getOffen() == 0:
            self.__v.textEdit.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">GG Mate! Du bist 1 cooler Dude</span></p></body></html>")

