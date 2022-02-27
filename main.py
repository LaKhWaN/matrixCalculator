from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import *
app = QtWidgets.QApplication([])


def exitWindow():
    window.destroy()
    exit()

def addBtn():
    destroyWin()
    import functions.add as add

def multiplyBtn():
    destroyWin()
    import functions.multiply as multiply
    
def constBtn():
    destroyWin()
    import functions.const as const

def transposeBtn():
    destroyWin()
    import functions.transpose as transpose

def determinantBtn():
    destroyWin()
    import functions.determinant as determinant

def inverseBtn():
    destroyWin()
    import functions.inverse as inverse

def loadMain():
    global window
    window = uic.loadUi("ui/main.ui")
    window.show()

def destroyWin():
    global window
    window.hide()

def mainFun():
    loadMain()
    window.exitBtn.clicked.connect(exitWindow)
    window.addBtn.clicked.connect(addBtn)
    window.multiplyBtn.clicked.connect(multiplyBtn)
    window.constBtn.clicked.connect(constBtn)
    window.transposeBtn.clicked.connect(transposeBtn)
    window.determinantBtn.clicked.connect(determinantBtn)
    window.inverseBtn.clicked.connect(inverseBtn)

if __name__ == "__main__":
    mainFun()
    window.show()
    app.exec_()