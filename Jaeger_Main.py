import sys, Jaeger_Controller
from PySide.QtGui import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Jaeger_Controller.Controller()
    c.show()
    sys.exit(app.exec_())
