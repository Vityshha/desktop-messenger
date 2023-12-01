import sys
from PyQt5.QtWidgets import QApplication 
from client_controller import Controller

def main():
    app = QApplication(sys.argv)

    model = None
    controller = Controller(model)
    app.exec()

if __name__ == '__main__':
    sys.exit(main())