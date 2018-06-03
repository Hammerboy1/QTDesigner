
import test
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from skjerm import Ui_Form
#import smbus
import time
#import IO
#import Roof
#import LR

b = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,21,22,23,24,25,31,32,33,34,35,36,37]
a = [0,1,2,5,6,8,11,12,13,14]      
class MyFirstGuiProgram(Ui_Form):
    def __init__(self, dialog):
        Ui_Form.__init__(self)
        self.setupUi(dialog)

        self.Test.clicked.connect(self.test)
        self.Reset.clicked.connect(self.reset)
        
        for i in range(0,10):
            xsquare = getattr(self, "square_"+str(a[i]))            
            image = QtGui.QImage(QtGui.QImageReader("square.png").read())
            xsquare.setPixmap(QtGui.QPixmap(image))

        self.reset()
        
    def reset(self):

        for i in range(0,6):
            for a in range(1,8):
                xlabel = getattr(self, "label_"+str(i)+str(a))            
                image = QtGui.QImage(QtGui.QImageReader("gray.png").read())
                xlabel.setPixmap(QtGui.QPixmap(image))
                
        for a in range(0,30):
            xlabel = getattr(self, "lab_"+str(b[a]))            
            image = QtGui.QImage(QtGui.QImageReader("gray.png").read())
            xlabel.setPixmap(QtGui.QPixmap(image))

        image = QtGui.QImage(QtGui.QImageReader("logo.png").read())
        self.square_3.setPixmap(QtGui.QPixmap(image))
        image = QtGui.QImage(QtGui.QImageReader("logo.png").read())
        self.square_9.setPixmap(QtGui.QPixmap(image))

    def test(self):
        for i in range(0,6):
            for a in range(1,8):
                xlabel = getattr(self, "label_"+str(i)+str(a))            
                image = QtGui.QImage(QtGui.QImageReader("green.png").read())
                xlabel.setPixmap(QtGui.QPixmap(image))
                
        for a in range(0,30):
            xlabel = getattr(self, "lab_"+str(b[a]))            
            image = QtGui.QImage(QtGui.QImageReader("green.png").read())
            xlabel.setPixmap(QtGui.QPixmap(image))

        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = MyFirstGuiProgram(dialog)
    #dialog.show()
    dialog.showFullScreen()
    #sys.exit(app.exec_())
    app.exec_()
