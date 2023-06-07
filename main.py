from PyQt5.QtWidgets import QApplication
from disp import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = MainWindow()
    window.show()

    # Start the event loop
    app.exec_()
