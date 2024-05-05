import sys

from PyQt6.QtWidgets import QApplication

from controllers.login_controller import LogInController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LogInController()
    window.show()
    sys.exit(app.exec())
