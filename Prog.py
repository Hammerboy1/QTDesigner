
import test
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from skjerm import Ui_Form
#import smbus
import time
#import IO
#import Roof
#import LR
            
class MyFirstGuiProgram(Ui_Form):
    def __init__(self, dialog):
        Ui_Form.__init__(self)
        self.setupUi(dialog)

        self.Test1.clicked.connect(self.test_1)
        self.Test2.clicked.connect(self.test_2)
        self.Test3.clicked.connect(self.test_3)

        a = [0,1,2,5,6,8,11,12,13,14]
        for i in range(0,10):
            xsquare = getattr(self, "square_"+str(a[i]))            
            image = QtGui.QImage(QtGui.QImageReader("square.png").read())
            xsquare.setPixmap(QtGui.QPixmap(image))
        
    def test_1(self):

        for i in range(0,6):
            for a in range(1,8):
                xlabel = getattr(self, "label_"+str(i)+str(a))            
                image = QtGui.QImage(QtGui.QImageReader("gray.png").read())
                xlabel.setPixmap(QtGui.QPixmap(image))

    def test_2(self):
        for i in range(0,6):
            for a in range(1,8):
                xlabel = getattr(self, "label_"+str(i)+str(a))            
                image = QtGui.QImage(QtGui.QImageReader("green.png").read())
                xlabel.setPixmap(QtGui.QPixmap(image))
            
    def test_3(self):
        for i in range(0,6):
            for a in range(1,8):
                xlabel = getattr(self, "label_"+str(i)+str(a))            
                image = QtGui.QImage(QtGui.QImageReader("red.png").read())
                xlabel.setPixmap(QtGui.QPixmap(image))

        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = MyFirstGuiProgram(dialog)
    #dialog.show()
    dialog.showFullScreen()
    #sys.exit(app.exec_())
    app.exec_()
