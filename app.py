import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from MainWindow.MainWindow import MyWindow

if __name__=='__main__':
    app=QApplication(sys.argv)

    window=MyWindow()
    window.show()

    sys.exit(app.exec())