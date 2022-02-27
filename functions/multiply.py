from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import *
import matrix
import sys
from main import mainFun

app = QtWidgets.QApplication([])

window = uic.loadUi("ui/add.ui")

def okayBtn():
    try:
        mtrixA = [[float(x) for x in y] for y in [x.split(" ") for x in window.matrix1.toPlainText().split("\n")]]
        mtrixB = [[float(x) for x in y] for y in [x.split(" ") for x in window.matrix2.toPlainText().split("\n")]]
        
        matrix_a = matrix.Matrix(len(mtrixA),len(mtrixA[0]))
        matrix_a.create(mtrixA)

        matrix_b = matrix.Matrix(len(mtrixB),len(mtrixB[0]))
        matrix_b.create(mtrixB)
        
        if(len(mtrixA[0]) != len(mtrixB)):
            QMessageBox.about(window,"Error","Matrices must be of same size")
            return 0
        window.result.setPlainText("\n".join([" ".join([str(x) for x in y]) for y in matrix_a.multiply_matrices(matrix_b)]))

    except Exception as e:
        QMessageBox.about(window, "Error", "Enter valid matrix")
        
def back():
    window.hide()
    sys.path.insert(0, "../")
    mainFun()
    
window.show()
window.okBtn_2.clicked.connect(okayBtn)
window.back.clicked.connect(back)