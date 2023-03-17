from PyQt5.QtWidgets import QApplication
from controller import CalculatorController
import os


if __name__ == '__main__':
    app = QApplication([])
    controller = CalculatorController()
    controller.show()
    app.exec_()
