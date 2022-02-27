from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import *
import matrix
import sys
from main import mainFun

app = QtWidgets.QApplication([])

window = uic.loadUi("ui/determinant.ui")

def okayBtn():
    try:
        mtrixA = [[float(x) for x in y] for y in [x.split(" ") for x in window.matrix1.toPlainText().split("\n")]]
        
        matrix_a = matrix.Matrix(len(mtrixA),len(mtrixA[0]))
        matrix_a.create(mtrixA)

        window.result.setPlainText("\n".join([" ".join([str(x) for x in y]) for y in matrix_a.transpose()]))
        
    except Exception as e:
        QMessageBox.about(window, "Error", "Enter valid matrix")

def back():
    window.hide()
    sys.path.insert(0, "../")
    mainFun()
    
window.show()
window.okBtn_2.clicked.connect(okayBtn)
window.back.clicked.connect(back)