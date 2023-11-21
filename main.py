######  PROGRAM MEMANGGIL WINDOWS PYQT5 ##########################

####### memanggil library PyQt5 ##################################
#----------------------------------------------------------------#
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtQml import * 
from PyQt5.QtWidgets import *
from PyQt5.QtQuick import *  
import sys
import random
#----------------------------------------------------------------#

array_x = []
array_y = []
mirror = []
pilihan = ["true", "false"]
########## mengisi class table dengan instruksi pyqt5#############
#----------------------------------------------------------------#
class table(QObject):    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.app = QApplication(sys.argv)
        self.engine = QQmlApplicationEngine(self)
        self.engine.rootContext().setContextProperty("backend", self)    
        self.engine.load(QUrl("main.qml"))
        sys.exit(self.app.exec_())
        
    @pyqtSlot(result=list)
    def array_x(self):  return (array_x)
    
    @pyqtSlot(result=list)
    def array_y(self):  return (array_y)
    
    @pyqtSlot(result=list)
    def mirror(self):  return (mirror)
    
    
    @pyqtSlot(str)
    def tambah_ikan(self, message):
        array_x.append(random.randint(0,300))
        array_y.append(0)
        mirror.append("true")
    
    @pyqtSlot(str)
    def kurang_ikan(self, message):
        del array_x[0]
        del array_y[0]
        del mirror[0]
        
    @pyqtSlot(str)
    def mirror_orientation(self, message):
        global mirror
        global pilihan
        for s in range(len(mirror)):
            mirror[s] = str(random.choice(pilihan))
            
    
    @pyqtSlot(str)
    def shuffle(self, message):
        global array_x
        global array_y
        for i in range(len(array_x)):
            array_x[i] = array_x[i] + random.randint(-10, 10)
            if (array_x[i] < 0):
                array_x[i] = 0
            if (array_x[i] > 350):
                array_x[i] = 350
        
        for i in range(len(array_y)):
            array_y[i] = array_y[i] + random.randint(-10, 10)
            if (array_y[i] < 0):
                array_y[i] = 0
            if (array_y[i] > 350):
                array_y[i] = 350
        print(array_x, array_y)
        
#----------------------------------------------------------------#

########## memanggil class table di mainloop######################
#----------------------------------------------------------------#    
if __name__ == "__main__":
    main = table()
    
    
#----------------------------------------------------------------#